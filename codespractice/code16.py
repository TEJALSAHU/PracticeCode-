

#Cal the sum of three given no.s, if the val are equal then return thrice of their sum
def sum_thrice(x,y,z):
    sum = x+y+z#cal the sum of x,y,z
    if x==y==z:
        sum = sum*3
        return sum #if they are equal, triple the sum
print(sum_thrice(1,2,3))
print (sum_thrice(3,3,3))
