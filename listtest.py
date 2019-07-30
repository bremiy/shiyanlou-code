import sys 

a, b = [], []

for argv in sys.argv[1:]:
    if len(argv) > 3:
        a.append(argv)
    else:
        b.append(argv)

'''
print(' '.join(a))
print(' '.join(b))
'''

for i in a:
    print(i, end=' ')
print()
for i in b:
    print(i, end=' ')
print()
