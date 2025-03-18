import random

lowers="qwerrtyuioplkjhgfdsazxcvbnm"
uppers=lowers.upper()
symbol="!@#$%^&*><"
number="1234567890"
char=lowers + uppers + symbol + number
length=8
password="".join(random.sample(char,length))
print("password:",password)
