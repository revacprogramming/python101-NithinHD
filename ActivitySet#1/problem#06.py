s=int(input('Enter Smallest number:'))
l=int(input("Enter Largest Number number:"))
while True:
    n=int(input('Enter a number'))
    if n>=s and n<=l:
        print(n)
        break
    else:
        print('Enter Number within the Range')