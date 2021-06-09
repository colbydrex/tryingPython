import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("there must be at least two people to split a check")
    return math.ceil(total / number_of_people)
    
try:
    total_due = float(input("what is the total? "))
    number_of_people = int(input("how many people? "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("LOL, Thats not gonna work. Please enter an actual number")
    print("({})".format(err))

else:
    print ("each person owes about ${}".format(amount_due))


