import os
os.system('CLS')

def kwadratowa (a,b,c,x):
    return (a*x**2+b*x+c)

def miejsca_zerowe (a,b,c):
    delta=b**2-4*a*c
    if delta>0:
        return [(-b+(delta)**0.5)/2*a, (-b-(delta)**0.5)/2*a]
    elif delta==0:
        return [-b/2*a]
    else:
        return []
 
print(miejsca_zerowe(1,-2,5))
print(miejsca_zerowe(-1,-2,3))
print(miejsca_zerowe(2,-4,2))

for i in range(-10,11):
    print(str(kwadratowa(1,1,-3,i)))
