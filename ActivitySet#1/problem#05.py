def computepay(h,r):
    if  r<=40:
        r=h*r
        return r
    elif h>40:
        r=40*r+((h-40)*r*1.5)
        return r
hrs=int(input('Enter the number of hours:'))
rate=float(input("Eter the rate per hour:"))
print('Pay=',computepay(hrs,rate))