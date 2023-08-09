a = int(input())
b = int(input())
output = 0

if ((b % a) == 0) and ((b // a) > 0) :
    output = 1
elif ((a % b) == 0) and ((a // b) > 0) :
    output = 2
else :
    output = 3

print(output)