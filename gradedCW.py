def problem1():
    arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem2[3])
    print(arrayForProblem2.__len__())
    arrayForProblem2.remove("Erin")
    print(arrayForProblem2)
    print(arrayForProblem2[2])

problem1()

def problem2():
    userinput= input("Enter a word")
    while(userinput!="q"):
        userinput=input("Try again")
problem2()

#Problem 4
number=[1,2,3,4,5]
for x in range(number[4],0,-1):
        print(x)

#Problem 5

def problem5():
    array=[0,2,4,6,8,16,]
    numUser=int(input("Enter a number"))
    high=0
    low=0
    equal=0
    for element in array:
         if numUser<element:
            high=high+1
         elif numUser>element:
            low=low+1
         else:
            equal=equal+1
    print(f"There are {high} numbers higher than {numUser}")
    print(f"There are {low} numbers lower than {numUser}")
    print(f"There are {equal} numbers equal to {numUser}")


problem5()