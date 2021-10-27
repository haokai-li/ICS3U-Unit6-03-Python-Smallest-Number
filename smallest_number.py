#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program calculate smallest number
import random


def calculated_smallest_number(calculate_my_numbers):
    # This function calculate smallest number
    loop_number_second = 0
    total_number = 100

    # process
    for loop_number_second in calculate_my_numbers:
        if loop_number_second < total_number:
            total_number = loop_number_second

    return total_number


def main():
    # This function calculate average
    my_numbers = []
    smallest_number = 0
    loop_number_first = 0

    # output
    print("Here is a list of random numbers:")
    print("")

    # process
    for loop_number_first in range(0, 10):
        calculate_number = random.randint(0, 100)
        my_numbers.append(calculate_number)
        # output
        print(
            "The random number {0} is {1}".format(
                loop_number_first + 1, calculate_number
            )
        )

    # call functions
    smallest_number = calculated_smallest_number(my_numbers)

    # output
    print("")
    print("The smallest number is: {0}".format(smallest_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
