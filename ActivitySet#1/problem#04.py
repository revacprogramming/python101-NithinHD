hrs=float(input('Enter the number of hours:'))
rate=float(input('Enter the rate per hour'))
if hrs<40:
  fee=hrs*rate
  print('The Fee is ',fee)
if not hrs<40:
  h=hrs-40
  fee=(40*rate)+(h*1.5*rate)
  print('The Fee is ',fee)