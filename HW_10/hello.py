from faker import Faker
fake = Faker()


def hello(name, password):
    if not name:
        name = fake.name()
    if not password:
        password = fake.password()
        return f"Hello, {name}, your password is {password}"

    if len(password) < 8:
        return "Password not valid: must contain at least 8 characters."

    help_value = 0
    for char in password:
        if char.isalpha():
            help_value += 1
            if password.count(char) > 2:
                return "Password not valid: contains more than two repeated characters."

    if help_value < 4:
        return "Password not valid: must contain at least four alphabetic characters."

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
            break
    if not digit:
        return "Password not valid: must contain at least one digit"
    return f"Hello, {name}, your password is {password}"
