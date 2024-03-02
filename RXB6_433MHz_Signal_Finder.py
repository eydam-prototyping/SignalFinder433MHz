from machine import Pin
from time import ticks_us

class Princeton_24bit_Signal:
    def __init__(self):
        self._value = 0
        self._raw = []
        self.valid = True

    def _feed(self, cycle):
        self._raw.append(cycle)
        length = cycle[0] + cycle[1]
        self._value <<= 1

        if 0.15 < cycle[0]/length < 0.35:
            pass
        elif 0.65 < cycle[0]/length < 0.85:
            self._value |= 1
        else:
            self.valid = False

    def is_valid(self):
        return self.valid & (len(self._raw)==24)
    
    def __str__(self) -> str:
        return f"Princeton_24bit_Signal: 0x{self._value:06x}, Length:{len(self._raw):2d}, Valid:{self.valid}, Mean Cycle Time: {sum([x[0]+x[1] for x in self._raw])/len(self._raw):.2f}us"

    def __repr__(self) -> str:
        return self.__str__()
    
class SignalFinder:
    _t = 0
    _t_on = 0
    _t_off = 0
    _reading = False
    _old_cycle_time = 0
    _t_delta = 300
    _min_signal_length = 20
    _buffer = []
    
    def __init__(self, _pin, _signal_cb=None, _raw = False):
        self.pin = Pin(_pin, Pin.IN, Pin.PULL_UP)
        self.raw = _raw
        self.pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.interrupt)
        self.signal_cb = _signal_cb

    def interrupt(self, pin):
        dt = ticks_us() - self._t
        self._t = ticks_us()
        v = pin.value()

        if not self._reading:
            return
        
        # cycle starts with a low signal and ends with a high signal
        if v:
            self._t_on = dt
        else:
            self._t_off = dt
            self._t_on = 0

        if self._t_on != 0 and self._t_off != 0:
            if self.raw:
                # if raw, then store on and off time in buffer
                self._buffer.append((self._t_off, self._t_on))
            else:
                
                cycle_time = self._t_on + self._t_off
                if abs(cycle_time - self._old_cycle_time) < self._t_delta:
                    self._buffer.append((self._t_off, self._t_on))
                else:
                    if len(self._buffer) > self._min_signal_length:
                        signal = Princeton_24bit_Signal()
                        for cycle in self._buffer:
                            signal._feed(cycle)
                        if signal.is_valid():
                            if self.signal_cb:
                                self.signal_cb(signal)
                    self._buffer = [(self._t_off, self._t_on)]
                self._old_cycle_time = cycle_time

    def listen(self):
        self._reading = True

    def stop_listening(self):
        self._reading = False