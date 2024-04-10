#Mason Kolb

def encode(num):
    #converts from string to int
    num = [int(digit) for digit in num]
    #adding encoded digits to a list
    encoded_digits = [(digit + 3) % 10 for digit in num]
    #converts list back to a string
    encoded_str = ''.join(map(str, encoded_digits))
    return encoded_str


if __name__ == '__main__':
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("Please enter an option: ")
        if choice == "1":
            num = input("Please enter your password to encode: ")
            encode(num)
        if choice == "2":
            pass
        elif choice == "3":
            quit()