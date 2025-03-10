import sys

if len(sys.argv) > 1:
    print("none")

else:

    for i in range(13):
        print(f"Table de {i}: ", end="")
        for j in range(13):
            print(i * j, end=" ")
        print()
