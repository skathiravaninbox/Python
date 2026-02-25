class multipleFunctions():
    def oddEven():
        num=int(input("Enter a value"))
        if((num%2)==0):
            print("Even")
            msg="Even"
        else:
            print("Odd")
            msg="Odd"
        return msg

    def BMI():
        bmi=int(input("Enter the int value BMI Index: "))
        if(bmi<17):
            print("You are Serverly Underweight")
            message="Serverly Underweight"
        elif(bmi<19):
            print("You are Underweight")
            message="Underweight"
        elif(bmi<26):
            print("You are Healthy")
            message="Healthy"
        elif(bmi<31):
            print("You are Overweight")
            message="Overweight"
        else:
            print("You are Serverly Overweight")
            message="Serverly Overweight"
        return message