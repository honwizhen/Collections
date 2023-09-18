import string

def find_pin(pin):
    for i in range(0, 9999):
        if i == pin:
            return i
        else:
            print(i)

def find_password(pin):
# test every combination of letters until we find the password
    letters = list(string.printable)
    for i in letters:
        for j in letters:
            for k in letters:
                password = i + j + k 
                if password == pin:
                    return password
                else:
                    print(password)

def main():
    #  pin can be only length of 4 characters
    pin = input("Enter a 3 digit pin: ")
    if len(pin) == 3:
        print("your password is ",find_password(pin))
    else :
        print("Invalid pin")
        main()

if __name__ == "__main__":
    main()