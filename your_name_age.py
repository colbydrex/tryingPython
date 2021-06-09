first_name = input("what is your name? ")
print("hello,", first_name)
if first_name == "colby":
    print(first_name, "is learning Python")
elif first_name == "julia":
    print(first_name, "is learing along with other students")
else:
    age = int(input("how old are you "))
    if age <= 6:
        print("wow, {} is a little number...".format(age))
    elif age == 36:
        print("HEY,thats how old I am!!!")
    elif age >= 37:
        print("LOL, {}. {} you are an old fukker!".format(age, first_name))
    print("RUN FROM THIS SHIT, {}!!!".format(first_name))
print("have a great day {}!".format(first_name))
