x=int(input('Introduceti numarul x='))
y=int(input('Introduceti numarul y='))
z=int(input('Introduceti numarul z='))
if (x<y+z) and (y<x+z) and (z<x+y):
    if x==z and x==y and y==z:
        print('Triunghiul este echilateral')
    elif x==z or x==y or y==z:
        print('Triunghiul este isoscel')
    else:
        print('Triunghiul este scalen')
  
  