num = int(input('Enter a number between 1 and 10: '))

match num:
    case 1:
        print("You won the Car")
    case 4:
        print("You won the trip to Thailand")
    case 9:
        print('You won the new Iphone ')
    case 10:
        print("You won the New Ipad")
    case _:
        print("You lost")

print('----------------------------------------------------------')
# Grade Program using match-case

# Taking grade input from user
grade = input("Enter your grade (A/B/C/D/F): ").upper()

# match checks the value of grade
match grade:

    # If grade is A
    case 'A':
        print("Excellent")

    # If grade is B
    case 'B':
        print("Very Good")

    # If grade is C
    case 'C':
        print("Good")

    # If grade is D
    case 'D':
        print("Pass")

    # If grade is F
    case 'F':
        print("Fail")

    # Default case if no match found
    case _:
        print("Invalid Grade")

print('---------------------------------------------------------------')

marks = int(input('Enter your marks between 1 to 100: '))

match marks:

    case _ if marks >= 90:
        print('Grade A')

    case _ if marks >= 80:
        print('Grade B')

    case _ if marks >= 70:
        print('Grade C')

    case _ if marks >= 35:
        print('Grade D')

    case _:
        print('Invalid Marks')
