print("***********Exercise 1*************\n")
print("I'm a CUHK msC IN FinTech student.\nHello everybody in this course!\nLet's solve problems by programming in Python.")

print("\n***********Exercise 2*************\n")
a = int(input("Input 1:"))
b = int(input("Input 2:"))
c = int(input("Input 3:"))
d = int(input("Input 4:"))
print("The minimum value is ", min(a,b,c,d),"whereas the maximum value is ", max(a,b,c,d))

print("\n***********Exercise 3*************\n")
minutes = int(input("Please input minutes:"))
D = minutes // (24 * 60)
H = (minutes % (24 * 60)) // 60
M = (minutes % (24 * 60)) % 60
print(D,"Days",H,"Hours",M,"Minutes")

print("\n***********Exercise 4*************\n")
import getpass
print("Player 1, write down your number secretly:")
num = int(getpass.getpass())
a = int(input("Player 2, input your guess:"))
n = 1
while a != num:
    if a < num:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
    a = int(input("Player 2, input your guess:"))
    n += 1

print("You are right after trying for",n,"times. Program ends.")
