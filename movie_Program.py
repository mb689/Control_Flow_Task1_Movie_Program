# age = input("What is your age? ")
#
# if age.isdigit() and -1 < int(age) < 177:
#     if int(age) < 12:
#         print("You can watch U and PG movies")
#     elif 12 < int(age) < 15:
#         print("You can watch 12 or 12A movies")
#     elif 14 < int(age) < 18:
#         print("You can watch 15 years movies")
#     else:
#         print("You can watch 18+ movies")
# else:
#     age = input("What is your age? ")


def check_age_cinema(age):
    if age.isdigit() and -1 < int(age) < 177:
        if int(age) < 12:
            return print("You can watch U and PG movies")
        elif 12 <= int(age) < 15:
            return print("You can watch 12 or 12A movies")
        elif 14 < int(age) < 18:
            return print("You can watch 15 years movies")
        else:
            return print("You can watch 18+ movies")
    else:
        age = input("What is your age? ")
        check_age_cinema(age)


age = input("What is your age? ")
check_age_cinema(age)
