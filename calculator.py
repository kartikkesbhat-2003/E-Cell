# EXERCISE 2 - FAULTY CALCULATOR
# DESIGN A CALCULATOR WHICH WILL CORRECRTLY SOLVE ALL
# THE PROBLEMS EXCEPT THE FOLLOWING ONES:
# 45 + 3 = 555, 56 - 9 = 77, 56/6 = 4
# YOUR PROGRAM SHOULD TAKE OPERATOR AND THE TWO NUMBERS
# AS INPUT FROM THE USER AND THEN RETURN THE RESULT

n1=int(input("enter your first number : "))
operator=input("enter your operator(+, -, /, *) : ")
n2=int(input("enter your second number : "))
if operator=="+":
    if (n1 == 45 and n2 == 3):
        print("YOUR ANSWER IS 555")
    else:
        print("YOUR ANSWER IS", n1+n2)
elif operator=="-":
    if (n1 == 56 and n2 == 9):
        print("YOUR ANSWER IS 77")
    else:
        print("YOUR ANSWER IS", n1-n2)
elif operator=="/":
    if (n1 == 56 and n2 == 6):
        print("YOUR ANSWER IS 4")
    else:
        print("YOUR ANSWER IS", n1/n2)
elif operator == "*":
    print("YOUR ANSWER IS", int(n1*n2))
else:
    print("error")
exit()