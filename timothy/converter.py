>>> %Run 05_01_converter.py
Convert inches to mm
converting 2 inches
50mm
>>> c2 = ScaleConverter('feet', 'yards', 0.333)
>>> print(str(c2.convert(3)) + c2.units_to)
0.9990000000000001yards
>>> c2 = ScaleConverter('feet', 'yards', 1/3)
>>> print(str(c2.convert(3)) + c2.units_to)
1.0yards
>>> print(str(c2.convert(10)) + c2.units_to)
3.333333333333333yards