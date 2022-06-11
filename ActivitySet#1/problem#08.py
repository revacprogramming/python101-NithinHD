f=open(input('Enter the file name:'))
count=0
total=0
a=[]
for line in f:
    if line.startswith("X-DSPAM-Confidence:"):
        n=line.find(':')
        b=float(line[n+1:])
        a.append(b)
for i in a:
    count=count+1
    total=total+i
avg=total/count
print('average spam confidence =',avg)