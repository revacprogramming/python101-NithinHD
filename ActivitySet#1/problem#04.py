h = float(input("Enter hours? "))
if h<=40:
    fee=h*1.5
    print('the fee is',fee)
elif h>40:
    h1=h-40
    fee=(40*10.50)+(h1*10.5)
    print('the fee is',fee)