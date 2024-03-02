import RXB6_433MHz_Signal_Finder as signal_finder

s = signal_finder.SignalFinder(14, lambda s: print(s))
s.listen()