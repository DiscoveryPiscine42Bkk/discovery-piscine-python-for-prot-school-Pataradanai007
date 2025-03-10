a = int(input("Enter a number less than 25: "))
if a > 25:
    print("Error")
else:
    while a <= 25:
        print(f"Inside the loop, my variable is {a}")
        a += 1