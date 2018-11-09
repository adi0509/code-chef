##  _________________method -1_______________


##n, q = list(map(int, input().split()))
##a = []
##a.append(0)
##for i in range(n):
##    a.append(int(input(), 2))
##for i in range(q):
##    l, r, x = list(map(int, input().split()))
##    x = str(x)
##    x = int(x,2)
##    minI = l>r and r or l
##    maxI = l>r and l or r
##    maxAns = a[minI]^x
##    maxAnsIndex = minI
##    for j in range(minI+1, maxI+1, 1):
##        temp = a[j]^x
##        if(maxAns<temp):
##            maxAns = temp
##            maxAnsIndex = j
##    print(maxAnsIndex)

##  __________________Method -2_________________________


##def binaryToDecimal(binary): 
##      
##    binary1 = binary 
##    decimal, i, n = 0, 0, 0
##    while(binary != 0): 
##        dec = binary % 10
##        decimal = decimal + dec * pow(2, i) 
##        binary = binary//10
##        i += 1
##    return decimal
##
##n, q = list(map(int, input().split()))
##a = []
##a.append(0)
##for i in range(n):
##    a.append(binaryToDecimal(int(input())))
##for i in range(q):
##    l, r, x = list(map(int, input().split()))
##    x = str(x)
##    x = binaryToDecimal(int(x))
##    minI = l>r and r or l
##    maxI = l>r and l or r
##    maxAns = a[minI]^x
##    maxAnsIndex = minI
##    for j in range(minI+1, maxI+1, 1):
##        temp = a[j]^x
##        if(maxAns<temp):
##            maxAns = temp
##            maxAnsIndex = j
##    print(maxAnsIndex)


##  __________________Method -3_________________________
def xor(x, y):
    ans = ""
    for i in range(len(x)):
        if x[i] == "0" and y[i] == "1" or x[i] == "1" and y[i] == "0":
            ans += "1"
        else:
            ans += "0"
    ans = int(ans , 2)
    return ans


n, q = list(map(int, input().split()))
a = []
a.append(0)
maxL = 0
for i in range(n):
    s = input()
    length = len(s)
    if(maxL<length):
        maxL = length
    a.append(s)

for i in range(q):
    l, r, x = list(map(int, input().split()))
    x = str(x)
    length = len(x)
    if(length>maxL):
        maxL = length
    for j in range(maxL-length):
        x = "0" + x
    for i in range(n):
        length = len(a[i+1])
        for j in range(maxL-length):
            a[i+1] = "0" + a[i+1]
    minI = l>r and r or l
    maxI = l>r and l or r
    maxAns = xor(a[minI],x)
    maxAnsIndex = minI
    for j in range(minI+1, maxI+1, 1):
        temp = xor(a[j],x)
        #print(j, " == ", temp)
        if(maxAns<temp):
            maxAns = temp
            maxAnsIndex = j
    print(maxAnsIndex)
