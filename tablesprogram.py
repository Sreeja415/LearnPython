# using for loop 
A = int(input("choose a number  :"))
if A == 0 : 
 print ("invalid input")
else:
 for B in range (1,11) :
  print (f"{A} X {B} = {A*B}")


# using while loop
A = int (input("choose a number : "))
if A == 0 :
    print ("invalid input")
else :
    B = 1
    while B <= 10 :
        print (f"{A} X {B} = {A * B}")
        B += 1 