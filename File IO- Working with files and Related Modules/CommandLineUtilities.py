import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("num1", type =float, help="First Number")
parser.add_argument("num2", type =float, help="Second Number")
parser.add_argument("operations", choices=["add", "sub", "mul", "div"])

args = parser.parse_args()

if args.operations == "add":
    print(f"The result is {args.num1 + args.num2}")
elif args.operations == "sub":
    print(f"The result is {args.num1 - args.num2}")
elif args.operations == "mul":
    print(f"The result is {args.num1 * args.num2}")
elif args.operations == "div":
    print(f"The result is {args.num1 / args.num2}")
else:
    print("Invalid Operation")