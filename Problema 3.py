m=int(input('Introduceti numarul m='))
n=int(input('Introduceti numarul n='))
while n%m==0:
    n=n//m
if n==1:
    print('Numarul n este putere a lui m')
else:
    print('Numarul n nu este putere a lui m')