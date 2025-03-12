import sys

def shrink(s):
    """Displays the first 8 characters of the string."""
    print(s[:8])

def enlarge(s):
    """Appends 'Z' characters to make the string 8 characters long and displays it."""
    print(s.ljust(8, 'Z'))

def main():
    """Main function to handle command-line arguments."""
    args = sys.argv[1:]  # Get command-line arguments excluding script name
    
    if len(args) < 1:
        print("none")
        return
    
    i = 0
    while i < len(args):
        arg = args[i]
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
        i += 1  # Move to the next argument

if __name__ == "__main__":
    main()
