#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Oct 2019
# This program 



def main():
    # this function 

    # input
    integer_as_string = input("Enter your age (integer): ")

    # process
    try:
        integer_as_number = int(integer_as_string)
        if integer_as_number >= 25 and integer_as_number <= 40:
            print("Grandmother: You can date my grandchild.")
        else:
            print("Grandmother: You can't date my grandchild.")
    except Exception:
        print("It is not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
