print("***********Exercise 1*************")
n = int(input("Please enter the height of the tree:"))
print('Look!')
for i in range(n+1):
    print(' ' * (n - i) + 'o' * i * 2 + ' ' * (n - i))
print(' ' * (n - 1) + '|' * 2 + ' ' * (n - 1))


print("***********Exercise 2*************") 
import math
def change_digit(n,l):
    if n < 4:
        return l[0]*n
    elif n < 6:
        return l[0]*(5-n)+l[1]
    elif n < 9:
        return l[1]+l[0]*(n-5)
    else:
        return l[0]+l[2]
        
def roman_number(x):
    if x > 99 or x < 1:
        return 'Number is out of range'
    else:
        l = [['I','V','X'],['X','L','C']]
        if len(str(x)) == 2:
            if x % 10 == 0:
                return change_digit(math.floor(x/10),l[1])
            else:
                return change_digit(math.floor(x/10),l[1]) + change_digit(x%10,l[0])
        else:
            return change_digit(x%10,l[0])

test_case = [-1, 0, 24, 44, 49, 10000]
for i in test_case:
    print(roman_number(i))  
expected = ['Number is out of range', 'Number is out of range', 'XXIV', 'XLIV',
                    'XLIX', 'Number is out of range']
        
print("***********Exercise 3*************")     
def toMinutes(Dur):
    return Dur[0]*60*24 + Dur[1]*60 + Dur[2]

def setDuration(M):
    Dur = [0,0,0]
    Dur[0] = M // (24 * 60)
    Dur[1] = (M % (24 * 60)) // 60
    Dur[2] = (M % (24 * 60)) % 60
    return Dur

def printDuration(Dur):
    print("{} days {} hours {} minutes".format(Dur[0],Dur[1],Dur[2]))
 
Dur1 = setDuration(int(input("Enter duration #1 (in minutes):")))     
Dur2 = setDuration(int(input("Enter duration #2 (in minutes):")))           
print("Duration #1: {} days {} hours {} minutes".format(Dur1[0],Dur1[1],Dur1[2]))
print("Duration #2: {} days {} hours {} minutes".format(Dur2[0],Dur2[1],Dur2[2]))
print("The two durations are {} minutes apart.".format(toMinutes(Dur2)-toMinutes(Dur1)))

print("***********Exercise 4*************")
def recursive_pow(x,n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return recursive_pow(x * x, n/2)
    else:
        return x * recursive_pow(x, n-1)
    
