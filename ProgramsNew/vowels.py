ch = input("Enter a character: ")



for cha in ch:
    if ch in 'aeiouAEIOU':
        print("It is a vowel", ch)
        break
    else:
        print("It is a consonant", ch)
