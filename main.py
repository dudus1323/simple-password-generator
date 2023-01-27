def password_generator():
    import random

    letters_lower = 'abcdefghijklmnopqrstuvwxyz'
    letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    password = ''

    for i in range(3):
        password += (letters_lower[random.randint(0, len(letters_lower) - 1)])
    for i in range(3):
        password += (letters_upper[random.randint(0, len(letters_upper) - 1)])
    for i in range(3):
        password += (digits[random.randint(0, len(digits) - 1)])
    for i in range(3):
        password += (punctuation[random.randint(0, len(punctuation) - 1)])

    passwd = list(password)
    random.shuffle(passwd)

    password = ''.join(passwd)
    return (password)


