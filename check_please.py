import math

def split_check(total, number_of_people):
      return math.ceil(total / number_of_people)

try:
    total_due = float(input("what is the total? "))
    number_of_people = int(input("how many people? "))
except ValueError:
        print("LOL, Thats not gonna work. Please enter an actual number")

else:
    amount_due = split_check(total_due, number_of_people)
    print ("each person owes about ${}".format(amount_due))



