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