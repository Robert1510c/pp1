import re
sum=0
text='Przykładowe lkiczbt parzyste to 16, 2, 114 ahfau@gmail.com oraz 1014, a także 8 ale  aipo'
liczby=re.findall(r'\b\w+@[\w]+.\w+\b',text,re.IGNORECASE)
print(liczby)

