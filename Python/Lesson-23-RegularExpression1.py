import re #import regular expression

mytext = "Vasya aaaaaa 1972, Kolya - 1972: Olesya 1981," \
         "aaaaaa@intel.com, bbbbbbb@intel.com, Petya ggggg," \
         "1997 Stepan, Iryna 1999 aaaa, ggggggg@gmail.com," \
         "eeeeee@gmail.com, Vasyl 1999, 11231231, Aaa Stepan Bbb"

"""
\d  = Any Digit (tsifra) 0-9
\D  = Any non Digit (ne tsifra)
\w  = Any Alphabet symbol [A-Z a-z]
\W  = Any non Alpabet symbol
\s  = breakspace (probel)
\S  = non breakspace
[0-9]{3} ###  3 pidryad tsifry
[A-Z][a-z]+ #Перший символ велика літера, друга маленька, + - скільки завгодно символів після
"""


textlookfor = r"@\w+\.\w+"
allresults = re.findall(textlookfor, mytext)

print(allresults)