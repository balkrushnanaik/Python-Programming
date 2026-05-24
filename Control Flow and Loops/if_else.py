age = int(input("Enter your age: "))

if age > 18 : print("You are eligible for driving")
elif age == 18: print("Apply for driving license")
else:  print("You are not eligible for driving")

print("------------------------------------------------------------------")

age = int(input('Enter your age: '))
if age <= 12: print("Child.")
elif age <= 19: print("Teenager.")
elif age <= 35: print("Young adult.")
else: print("Adult.")


print("-----------------------------------------------------------------------")
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

print('-----------------------------------------------------------------------')

# Ternary Conditional Statement

age = 20
s = 'Adult' if age >= 18 else 'Teenager'
print(s)