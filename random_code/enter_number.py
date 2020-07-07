n = int(input("Enter Number: "))
c = 0
for i in range(1,n+1):
    print(" "*(n-1), end="")
    for j in range (1, i+1):
        print(chr(65+(c%26)),end=" ")
        c+=1
    print("")