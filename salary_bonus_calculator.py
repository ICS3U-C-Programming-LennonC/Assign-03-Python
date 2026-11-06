#!/usr/bin/env python3
# Created By: Lennon Cehajic
# Date: November 6th, 2026
# This program calculates the user's new salary bonus
# with their years of service and current salary.
#
def main():
    # Get the info from the user as a string.
    user_salary_string = input(
        "Welcome to Lennon’s salary bonus calculator. Please enter your current salary (Please round to the nearest dollar): "
    )
    user_years_string = input(
        "Please enter how many years you have worked at the company: "
    )

    # Try converting the inputs to an integer, calculate the user's salary bonus,
    # then display the user's new salary, rounded to two decimal places..
    try:
        user_salary_int = int(user_salary_string)
        if user_salary_int < 0:
            print(
                "{} is not a positive number. Please enter a valid number.".format(
                    user_salary_int
                )
            )
        else:
            try:
                user_years_int = int(user_years_string)
                if user_years_int > 5 and user_years_int < 110:
                    new_salary = user_salary_int * 1.05
                    print(
                        "Congrats! You have earned a 5% bonus. Your new salary is: ${:.2f}".format(
                            new_salary
                        )
                    )
                elif user_years_int <= 5:
                    print(
                        "Sorry, you have not earned a bonus. Your salary is still: ${:.2f}".format(
                            user_salary_int
                        )
                    )
                elif user_years_int < 0:
                    print(
                        "{} is not a positive number. Please enter a valid number.".format(
                            user_years_int
                        )
                    )
                elif user_years_int > 110:
                    print(
                        "{} is not a valid number. Please enter a valid number".format(
                            user_years_int
                        )
                    )
                else:
                    print(
                        "{} is not a valid number. Please enter a valid number".format(
                            user_years_int
                        )
                    )
            except Exception:
                print("{} is not a valid integer".format(user_years_string))
    except Exception:
        print("{} is not a valid integer".format(user_salary_string))


if __name__ == "__main__":
    main()
