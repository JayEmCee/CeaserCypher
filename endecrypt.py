result = ''
message = ''
choice = ''

while choice != 0:
    choice = input("\nEnter 1 to encrypt message, 2 to decrypt, 0 to exit: ")

    if choice == '1':
        message = input("\nEnter Message to encrypt: ")
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 4)

        print(result + '\n\n')
        result = ''

    elif choice == '2':
            message = input("\nEnter message to decrypt: ")
            for i in range(0, len(message)):
                result = result + chr(ord(message[i]) + 4)

            print(result + '\n\n')
            result = ''

    elif choice =='0':
                print("Please enter a valid value:  \n\n")

