salary=int(input("enter your salary"))
age=int(input("enter your age"))
if(salary<=20000 or age<=25):
    loan=int(input("enter the loan required amount"))
    if(loan<50000):
        print("you are eligible for the loan")
    else:
        print("maximum amount for the loan is Rs.50000")
else:
    print("Not eligible for the loan amount")
      
  