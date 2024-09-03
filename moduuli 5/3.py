
userinput = int(input("Enter a number: "))

tru = True

for i in range(2, userinput):

    if(userinput % i == 0):
        print("ei oo alkis")
        tru = False
        break
if(tru == True):
    print("on alkis")

