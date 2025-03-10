response = input("What you gotta say? : ")

print("I got that! Anything else? : ", response)

while True:
    response = input("I got that! Anything else? : ")
    
    if response.lower() == "stop":
        break

