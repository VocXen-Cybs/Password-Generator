import random
import string

def generate_password(length, choices): 
    # Define character pools based on user choices
    pools = []
    if 'u' in choices:
        pools.append(string.ascii_uppercase)
    if 'l' in choices:
        pools.append(string.ascii_lowercase)
    if 'd' in choices:
        pools.append(string.digits)
    if 's' in choices:
        pools.append(string.punctuation)

    # Check that at least 3 character pools are selected
    if len(pools) < 3:
        raise ValueError("Please choose at least 3 character types")

    # Generate the password
    password = ''
    for i in range(length):
        pool = random.choice(pools)
        password += random.choice(pool)


    return password

while True:

# Ask user for preferences and length
    try:
        choices = input("Enter character types to include (u=uppercase, l=lowercase, d=digits, s=symbols): ")
        length = int(input("Enter password length: "))
        num_pass = int(input("How many passwords should be generated: "))

        for _ in range(num_pass): 
            password = generate_password(length, choices)
            print("Generated password:", password)

        break
    except ValueError as e:
        print("Error:", e)
