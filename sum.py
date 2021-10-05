#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program adds positive numbers


def main():
    # this function adds the numbers
    loop_counter = 0
    the_sum = 0

    # input
    user_input = input("How many numbers are you going to add: ")

    # process & output
    try:
        amount_of_numbers = int(user_input)
        for loop_counter in range(amount_of_numbers):
            user_input_2 = input("Enter a number to add: ")
            try:
                numbers_to_be_added = int(user_input_2)
                if numbers_to_be_added < 0:
                    continue
                the_sum = the_sum + numbers_to_be_added
            except Exception:
                print("Invalid input.")
                break
            finally:
                print("")
        else:
            print("The sum of all of the positive numbers is = {0}.".format(the_sum))
            print("")
    except Exception:
        print("Invalid input.")
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
