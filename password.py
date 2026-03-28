import string
def validate_password(password):
    # Check if password is at least 8 characters long
    if len(password) >= 8:
        # Check if password contains a special character
        for char in password:
            if char in string.punctuation:
                return True
    return False

# Call the function and store the result
is_valid = validate_password("P@ssw0rd")
print("Is the password valid? ", is_valid)