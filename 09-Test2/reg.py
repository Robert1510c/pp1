import re

tekst='Pain in spain'
x=re.findall(r'\b\w*ai\w*\b',tekst,re.IGNORECASE)
print(x)
print(len(x))