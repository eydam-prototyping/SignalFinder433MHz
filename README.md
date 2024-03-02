# SignalFinder433MHz

```python
import RXB6_433MHz_Signal_Finder as signal_finder

s = signal_finder.SignalFinder(14, lambda s: print(s))
s.listen()
```

```bash
Princeton_24bit_Signal: 0x000015, Length:24, Valid:True, Mean Cycle Time: 1441.75us
Princeton_24bit_Signal: 0x000015, Length:24, Valid:True, Mean Cycle Time: 1442.17us
Princeton_24bit_Signal: 0x000014, Length:24, Valid:True, Mean Cycle Time: 1443.58us
Princeton_24bit_Signal: 0x000014, Length:24, Valid:True, Mean Cycle Time: 1442.21us
Princeton_24bit_Signal: 0x000014, Length:24, Valid:True, Mean Cycle Time: 1441.83us
Princeton_24bit_Signal: 0x000014, Length:24, Valid:True, Mean Cycle Time: 1441.92us
Princeton_24bit_Signal: 0x000014, Length:24, Valid:True, Mean Cycle Time: 1441.92us
Princeton_24bit_Signal: 0xf23d54, Length:24, Valid:True, Mean Cycle Time: 1592.17us
Princeton_24bit_Signal: 0xf23d54, Length:24, Valid:True, Mean Cycle Time: 1591.63us
Princeton_24bit_Signal: 0xf23d54, Length:24, Valid:True, Mean Cycle Time: 1592.13us
Princeton_24bit_Signal: 0xf23d54, Length:24, Valid:True, Mean Cycle Time: 1593.58us
```