class class2Assignments():
    def subfields():
        print("Sub-fields in AI are: \n Machine Learning \n Neural Networks \n Vision \n Robotics \n Speech Processing \n Natural Language Processing")

    def oddEven():
        num=int(input("Enter a value"))
        if((num%2)==0):
            print(num," is Even number")
        else:
            print(num," is Odd number")

    def isEligibleForMarriage():
        gender=input("Enter your Gender (male/female): ")
        age=int(input("Enter your Age : "))
        print("Your Gender: ",gender)
        print("Your Age:  ",age)
        if gender=='male' and age>21:
            print("Eligible")
        elif gender=='female' and age>17:
            print("Eligible")
        else:
            print("Not Eligible")

    def percentage():
        total=0
        for temp in range(1,6):
            mark=int(input(f"Enter you Mark for subject {temp}:"))
            total+=mark
        avg=total/5
        print("Total :",total)
        print("Avg :",avg)

    def triangle():
        h1=int(input("Enter the Height for find the Area of Triangle"))
        b1=int(input("Enter the Breadth for find the Area of Triangle"))
        
    
        h2_1=int(input("Enter the Height-1 for find the Perimeter of Triangle"))
        h2_2=int(input("Enter the Height-2 for find the Perimeter of Triangle"))
        b2=int(input("Enter the Breadth for find the Perimeter of Triangle"))
    
        print("Height: ",h1)
        print("Breadth: ",b1)
        print("Area formula: (Height*Breadth)/2")
        at=(h1*b1)/2
        print("Area of Triangle: ",at)
        
        print("Height1: ",h2_1)
        print("Height2: ",h2_2)
        print("Breadth: ",b2)
        print("Perimeter formula: Height1+Height2+Breadth ")
        pt=h2_1+h2_2+b2
        print("Perimeter of Triangle: ",pt)

    