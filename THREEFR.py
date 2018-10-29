##There are three friends; let's call them A, B, C. They made the following statements:
##
##A: "I have x Rupees more than B."
##B: "I have y rupees more than C."
##C: "I have z rupees more than A."
##You do not know the exact values of x,y,z. Instead, you are given their absolute values, i.e. X=|x|, Y=|y| and Z=|z|. Note that x, y, z may be negative; "having −r rupees more" is the same as "having r rupees less".
##
##Find out if there is some way to assign amounts of money to A, B, C such that all of their statements are true.

def getAns( t):
    d = t[:]
    x = (d[0] + d[1] +d[2])
    y = ((-1*d[0]) + (-1 * d[1]) + (-1*d[2]))
    if(x==0):
        return True
    if(y==0):
        return True
    for i in range(3):
        d = t[:]
        d[i] = -1*d[i]
        x = (d[0] + d[1] +d[2])
        y = ((-1*d[0]) + (-1 * d[1]) + (-1*d[2]))
        if(x==0):
            return True
        if(y==0):
            return True
    return False

def main():
    t = int(input())
    for i in range(t):
        d = input().split()
        d = list(map(int, d))
        if(getAns(d)):
            print("yes")
        else:
            print("no")

if __name__=="__main__":
    main()
