def is_strong_password(password):
    # Rule 1: at least 8 characters
    if len(password) < 8:
        return False

    # Rule 2: at least one uppercase letter
    if re.search(r'[A-Z]', password) is None:
        return False

    # Rule 3: at least one lowercase letter
    if re.search(r'[a-z]', password) is None:
        return False

    # Rule 4: at least one digit
    if re.search(r'\d', password) is None:
        return False

    return True