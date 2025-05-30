numbers=[1,2,3,4]
target = 10
found = False
for i in range (0,len(numbers)) :
    for j in range (i+1, len(numbers)):
        if numbers[i]+numbers[j]==target :
            found=True
if found == True :
    print ("target found")  
else  :
    print ("target not found")   
            


    
