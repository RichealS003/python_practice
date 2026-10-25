"""
price = 300
number_purchased = 4
total_cost = price * number_purchased
print(f"Total cost is {total_cost} francs.")

first_score = 78
second_score = 91
difference = second_score -first_score
print(difference)

maths = 80
english = 75
science = 90
number_of_subjects = 3
total_score = (maths + english + science)
print(total_score / number_of_subjects)

print(17 / 5)
print(17 // 5)
print(17 % 5)

pens = 150
books = 300
total_cost = (pens * 2) + ( books * 3)
print(total_cost)

user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

user_age = input("Enter your age: ")
print(f"You are {user_age} years old.")

whole1 = int(input("Enter a whole number: "))
whole2 = int(input("Enter another whole number: "))
total = whole1 + whole2
print(f"The sum of the numbers are {total}")





age = int(input("Enter your age: "))
age_next_year = age + 1
print(f"You will be {age_next_year} years old next year!")

hour = int(input("Enter a whole number for hours: "))
minutes = hour * 60
print(minutes)



number = int(input("Enter a number: "))
if number == 0:
    print("This number is zero")
elif number < 0:
    print("This number is a negative number")
else:
    print("This number is positive")



score = int(input("Enter your score: "))
if score >= 50:
    print("You passed!")
else:
    print("You failed")



number = int(input("Enter a number: "))
if number % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")



number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
if number1 == number2:
    print(f"{number1} is equal to {number2}")
elif number1 > number2:
    print(f"{number1} is greater than {number2}")
else:
    print(f"{number2} is greater than {number1}")



age = int(input("Enter a number: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")



one_bundle = 2000
user_purchase = int(input("How many bundles do you want to buy? "))
total = user_purchase * one_bundle
print(total)



ama_goal = 50000
ama_current_savings = 32000
to_reach_goal = ama_goal - ama_current_savings
print(f"Ama needs {to_reach_goal} to reach goal.")
user_savings_goal = int(input("Enter your savings goals: "))
user_current_savings = int(input("Enter your current savings: "))
to_reach_user_goal = user_savings_goal - user_current_savings
print(f"User needs {to_reach_user_goal} to reach goal.")


discount = 10 / 100
price = int(input("Enter the original price: "))
discount_price = price * discount
amount_after_discount = price - discount_price
print(f"The final price after the discount is {amount_after_discount}")



electricity_price = 200
units_consumed = int(input("Enter the units of electricity consumed: "))
bill = electricity_price * units_consumed
print(f"Your total bill is {bill}.")
if bill > 10000:
    print("High bill!")
else:
    print("Bill within limit")



number1 = int(input('Enter a number: '))
number2 = int(input("Enter another number: "))
total = number1 + number2
difference = number1 - number2
product = number1 * number2
if number2 != 0:
    division = number1 / number2
    print(f"Division: {division}")
else:
    print("Cannot divide by zero.")
print(f"Addition: {total}. Subtraction: {difference}. Multiplication: {product}.")






children_ticket = 2000
teenager_ticket = 3500
adult_ticket = 5000
age = int(input("Enter your age: "))
if age < 13:
    print(f"Your ticket price is {children_ticket}.")
elif age <= 19:
    print(f"Your ticket price is {teenager_ticket}.")
else:
    print(f"Your ticket price is {adult_ticket}.")



score = int(input("Enter your score: "))
if score >= 0 and score <= 100:
    if score >= 80: # 80 and above up to 100
        print("A")
    elif score >= 70: #70 and above but stops at 79 because the previous conditional requires the number be 80 or above
        print("B")
    elif score >= 60: #60 and above but stops at 69 because the previous conditional requires the number be 70 or above
        print("C")
    elif score >= 50: #Same idea for this and the others
        print("D")
    else:
        print("F")
else:
    print("Number should be greater than 0 and less than or equal to 100.")



user_password = input("Enter a password: ")
if user_password == "python123":
    print("Access Granted")
else:
    print("Access Denied")



fees_per_term = 150000
outstanding = int(input("Enter how many terms' fees you need to pay for: "))
paid = int(input("Enter how many terms' fees you've paid: ")) #This variable unused. It'd have been useful if there was like total terms and then I'd have subtracted the outstanding from it, but as it stands there's no use for it.
balance = outstanding * fees_per_term
print(f"Your balance is {balance}.")
if balance == 0:
    print("Fully paid")
else:
    print("Payment outstanding")



number1 = int(input("Enter a number: "))
number2 = int(input("Enter a second number: "))
number3 = int(input("Enter a third number: "))
if number1 >= number2 and number1 >= number3:
    print(f"Number 1({number1}) is greater.") #It check if the number1 is greater than or equal to the other two numbers. If it is greater then it means that it is greater and if it is equal to then it means that they're both bigger.
elif number2 >= number1 and number2 >= number3:
    print(f"Number 2({number2}) is greater.")
else:
    print(f"Number 3({number3}) is greater.")

"""

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a second number: "))
number3 = int(input("Enter a third number: "))
if number1 >= number2 and number1 >= number3:
    print(f"Number 1({number1}) is greater.") #It check if the number1 is greater than or equal to the other two numbers. If it is greater then it means that it is greater and if it is equal to then it means that they're both bigger.
elif number2 >= number1 and number2 >= number3:
    print(f"Number 2({number2}) is greater.")
else:
    print(f"Number 3({number3}) is greater.")

    

score1 = int(input("Enter a number: "))
score2 = int(input("Enter a second number: "))
score3 = int(input("Enter a third number: "))
if score1 <= score2 and score1 <= score3:
    print(f"Score 1({score1}) is the lowest score.") 
elif score2 <= score1 and score2 <= score3:
    print(f"Score 2({score2}) is the lowest score.")
else:
    print(f"Score 3({score3}) is the lowest score.")

