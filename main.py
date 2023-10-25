#made by Benjamin Gneter
Menu_continue = True

while Menu_continue:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    menu_selection = int(input("Please enter an option: "))
    if menu_selection == 1:
        og_password = input("Please enter your password to encode: ")
        encoded_password = ""
        # iterates through digits in og_password and adds 3 to each of them
        for digit in og_password:
            digit = int(digit)
            if digit >= 7:
                digit = digit - 7
            else:
                digit += 3
            encoded_password = encoded_password + str(digit)
        print("Your password has been encoded and stored!\n")
    if menu_selection == 2:
        #Made By Tyler Brodnicki
        decoded_password = ""
        for digit in encoded_password:
            digit = int(digit)
            if digit < 3:
                digit += 7
            else:
                digit -= 3
            decoded_password += str(digit)
        print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
    if menu_selection == 3:
        break

