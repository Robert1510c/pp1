text= 'X_DSPAM-Confidence: 0.8475'
x=text.find(":")
print(x)
letter=float(text[20:])
print(letter)
print(type(letter))