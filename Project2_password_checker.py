import sys
import requests
import hashlib
import datetime


def request_api_data(query_chars):
    url = "https://api.pwnedpasswords.com/range/" + query_chars  # via api, query_chars = hashed version of first 5 chars of password
    response_url = requests.get(url)
    if response_url.status_code != 200:  # 200 = OK. So, if not 200: raise error (status)
        raise RuntimeError(f"There's an error: {response_url.status_code}")
    return response_url


def password_count(hashes, my_hash):  # hashes = all (full) hashes, my_hash = hash of first 5 chars
    hashes = (line.split(':') for line in hashes.text.splitlines())  # tuple comprehension: full_hash:hacked_count. So: seperate at ':'
    for hash, count in hashes:
        if hash == my_hash:
            return count  # return count of hash
    return 0


def pwned_api_check(password):  # actual password
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()  # sha1-hashing-algorithm version of our password
    first_five_chars, rest = sha1_password[:5], sha1_password[5:]  # split between first 5 chars & rest
    response = request_api_data(first_five_chars)  # select first 5 chars (data security: we don't want to enter full sha1-hashed version of our password)
    return password_count(response, rest)


def main(args):  # args = passwords that we want to check
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Your password ({password}) was found to be hacked {count} times')
        else:
            print(f'This password ({password}) has not been hacked at this moment.')
    return "Finished checking!"


print(datetime.date.today())

if __name__ == '__main__':  # only run this file if it's the main file being run (from cmd)
    sys.exit((main(sys.argv[1:])))

# cmd:
# C:\Users\Nicola\PycharmProjects\PycharmProject1>python Project2_password_checker.py password password123 PassWord123
# 2020-11-28
# Your password (password) was found to be hacked 3861493 times
# Your password (password123) was found to be hacked 126927 times
# Your password (PassWord123) was found to be hacked 874 times
# Finished checking!
