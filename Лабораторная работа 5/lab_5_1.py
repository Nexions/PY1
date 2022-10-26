# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
d = []
for i in range(0, 16):
    d.append({"bin":bin(i),
              "dec":i,
              "oct":oct(i),
              "hex":hex(i)})

pprint(d)




#рубрика эээээксперименты
#for i in range(0, 16):
#    d.setdefault("bin", bin(i))
#    d.setdefault("oct", oct(i))
#    d.setdefault("dec", i)
#    d.setdefault("hex", hex(i))
#    pprint(d)
#    d.clear()