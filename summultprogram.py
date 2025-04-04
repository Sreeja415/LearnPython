n = int(input("enter the number :"))
total = 1
for number in range(1,n+1): 
    total *= number
print("The sum is:", total)

n = int(input("enter the number :"))
total = 0
for number in range(1,n+1): 
    total += number
print("The sum is:", total)
