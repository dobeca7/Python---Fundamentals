def password_validation(password1):
    pass_is_valid = True
    if len(password1) < 6 or len(password1) > 10:
        print(f"Password must be between 6 and 10 characters")
        pass_is_valid = False

    if not password1.isalnum():
        print('Password must consist only of letters and digits')
        pass_is_valid = False
    digit_counter = 0
    for character in password1:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        pass_is_valid = False
    return pass_is_valid


password = input()
validation_password = password_validation((password))
if validation_password:
    print("Password is valid")

