import math
from __casac__.componentlist import componentlist
print("fafasfas")

cl=componentlist()

def spec(v,a2,a1,a0):
    x=math.log(v/100E6)
    return math.exp(a0+a1*x+a2*x**2)

for line in open('component.txt'):
    items=line.split('|')
    ra=(items[1].strip())
    dec=(items[2].strip())
    ra=float(ra)
    dec=float(dec)
    ra=math.radians(ra)
    dec=math.radians(dec)
    a2=float(items[3])
    a1=float(items[4])
    a0=float(items[5])
    I100=spec(100E6,a2,a1,a0)
    #print(I100)
    print('J2000 {0} {1}'.format(ra,dec))
    cl.addcomponent(flux=I100,fluxunit='Jy',shape='point',dir='J2000 {0}rad {1}rad'.format(ra,dec), freq=100E6,spectrumtype='spectral index',index=a1)

cl.rename("components.cl")
cl.close()


