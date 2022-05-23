h = float(input("Enter hours? "))
r=float(input('Enter the Rate per Hour:'))
if h<=40:
    fee=h*r
    print('the fee is',fee)
elif h>40:
    fee=(40*r)+((h-40)*r*1.5)
    print('the fee is',fee)