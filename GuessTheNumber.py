import random
x = random.randint(1,100)
i = int(input("Guess the Number (1-100):"))
while x >= i:
    print(f"Wrong! The Number is Greater than {i} ")
    i = int(input("Guess the Number (1-100):"))
while x<= i:
    print(f"Wrong! The Number is Lesser than {i}")
    i = int(input("Guess the Number (1-100):"))
while x==i:
    print("null")

print(f"{i} is Correct!!!!!")