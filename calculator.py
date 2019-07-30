import sys

shouru = int(sys.argv[1])
shui = shouru - 5000

if shui < 0:
     nashui = 0
elif shui < 3000:
    nashui = shui * 0.03 - 0
elif shui <= 12000:
    nashui = shui * 0.1 - 210
elif shui <= 25000:
    nashui = shui * 0.2 -1410
elif shui <= 35000:
    nashui = shui * 0.25 -2660
elif shui <= 55000:
    nashui = shui * 0.3 - 4410
elif shui <= 80000:
    nashui = shui * 0.35 - 7160
else:
    nashui = shui* 0.45 - 15160

a = format(nashui,".2f")
print(a)

