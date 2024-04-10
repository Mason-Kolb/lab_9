#Mason Kolb

def encode(num):
    #converts from string to int
    num = [int(digit) for digit in num]
    #adding encoded digits to a list
    encoded_digits = [(digit + 3) % 10 for digit in num]
    #converts list back to a string
    encoded_str = ''.join(map(str, encoded_digits))
    return encoded_str

def decode(passencoded):
    decoder = {"2":"9","1":"8","0":"7","9":"6","8":"5","7":"4","6":"3","5":"2","4":"1","3":"0"}
    passdecode = ""
    for num in passencoded:
        passdecode += decoder[num]
    return passdecode


if __name__ == '__main__':
    passcode = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Exit")

        choice = input("Please enter an option: ")
        if choice == "1":
            num = input("Please enter your password to encode: ")
            passcode = encode(num)
        if choice == "2":
            print("The encoded password is ",passcode," and the original password is ",decode(passcode),".",sep="")
        elif choice == "3":
            quit()