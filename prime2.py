lower = int(input("Enter a number: "))
upper = int(input("Enter a number: "))

for n in range (lower, upper+1):
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                break
        else:
            print(n)
