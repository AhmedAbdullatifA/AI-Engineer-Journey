def is_email(email):

    if '@' in email:
        email = email.split('@')[-1]
        if '.' in email and email[-4] == '.': 
            return True
    return False

print(is_email("abc@.com"))  # Output: True
print(is_email("abc@com."))  # Output: False