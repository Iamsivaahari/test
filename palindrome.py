n = (input("Enter any string: "))

check = n[::-1]

if n == check:
    print("The given word is a PALINDROME.")
else:
    print("The given word is a NOT A PALINDROME.")

