from fractions import gcd
import sys

def main(argv):
    if len(argv) is 1:
        x=5.0
        y=26.0
    else:
        x = float(argv[1])
        y = float(argv[2])
    hcf = gcd(x,y)
    lcm = (x*y)/hcf
    print 'lcm is: '+str(lcm)
    InverseX = 1/x
    InverseY = 1/y
    InverseGCD = gcd(InverseX,InverseY)
    print 'inverse of gcd of inverse is: '+str(1.0/InverseGCD)
    print (lcm - 1.0/InverseGCD)
    
if __name__ == "__main__":
    sys.exit(main(sys.argv))
