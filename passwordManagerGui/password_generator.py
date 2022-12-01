import random

letters = [
    letter for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
numbers = [number for number in "1234567890"]
symbols = [symbol for symbol in "~!@#$%^&*()_+}{:<>?/.,';][=-`|"]


def generate_password():

    nr_letters = random.randint(8, 12)
    nr_numbers = random.randint(6, 12)
    nr_symbols = random.randint(6, 12)

    let = [random.choice(letters) for _ in range(nr_letters)]
    num = [random.choice(numbers) for _ in range(nr_numbers)]
    sym = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = let+num+sym
    random.shuffle(password_list)

    password = "".join(password_list)

    return password
