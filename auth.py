from os import path
from random import randint

runned = True


def main():
    while runned:
        reg_or_auth = input("type log/reg: ")
        if reg_or_auth.lower() in ("log", "login", "l"):
            while True:
                username = input("username: ")
                with open("users.txt") as users:
                    all_users = users.readlines()
                    for line in all_users:

                        decryptUser = decrypt(line).split()
                        user_name = decryptUser[0]
                        user_pass = decryptUser[1]
                        user_key = decryptUser[2]

                        if user_name == username:
                            password = input("password: ")

                            if user_pass == password:
                                print(f"You are welcome your secret key is {user_key}")
                                input("Press enter to end ")
                                exit()
                            else:
                                print("Wrong password!")
                                break

                    print("incorrect username\n")

        elif reg_or_auth.lower() in ("reg", "register", "r", "куп"):
            print("[REGISTRATION]")

            username = input("Enter username: ")
            password = input("Enter password: ")
            secret_key = "".join([chr(randint(33, 126)) for _ in range(10)])
            crypted = crypt(f"{username} {password} {secret_key}")

            with open("users.txt", "a") as users:
                users.writelines(f"{crypted}\n")

            print(f"You are registered now your secret key is {secret_key}")

        break


def crypt(info):
    key = 131
    bar = f"{''.join([str(randint(0, 9)) for _ in range(4)])}"
    chars = [bar]

    for char in info:

        sym = ord(char) ^ key
        chars.append(sym)
        chars.append(f"{bar[0:2]}{randint(100, 999)}{bar[2:]}")

    joined = "".join([str(num) for num in chars])

    return joined


def decrypt(data):
    bar = data[0:4]
    data = data[4:]
    chars = []
    sym_ord = ""
    skip = 0

    for ind, val in enumerate(data):
        if ind < len(data) - 7:
            if data[ind] + data[ind+1] == bar[0:2] and data[ind+5] + data[ind+6] == bar[2:4]:
                chars.append(chr(int(sym_ord) ^ 131))
                sym_ord = ""
                skip = 6
            else:
                if skip == 0:
                    sym_ord += val
                else:
                    skip -= 1

    return "".join(chars)


if __name__ == "__main__":

    if not path.exists("users.txt"):
        with open("users.txt", "w") as _:
            print("[USERS FILE CREATED]")
    else:
        print("[USERS FILE DETECTED]")

    main()
