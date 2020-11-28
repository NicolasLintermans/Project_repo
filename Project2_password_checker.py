import sys
import requests
import hashlib
import datetime


def request_api_data(query_chars):
    url = "https://api.pwnedpasswords.com/range/" + query_chars
    response_url = requests.get(url)
    if response_url.status_code != 200:
        raise RuntimeError(f"There's an error: {response_url.status_code}")
    return response_url


def password_count(hashes, my_hash):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == my_hash:
            return count
    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_chars, rest = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first_five_chars)
    return password_count(response, rest)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Your password ({password}) was found to be hacked {count} times')
        else:
            print(f'This password ({password}) has not been hacked at this moment.')
    return "Finished checking!"


print(datetime.date.today())

if __name__ == '__main__':
    sys.exit((main(sys.argv[1:])))

# cmd:
# C:\Users\Nicola\PycharmProjects\PycharmProject1>python Project2_password_checker.py password password123 PassWord123
# 2020-11-28
# Your password (password) was found to be hacked 3861493 times
# Your password (password123) was found to be hacked 126927 times
# Your password (PassWord123) was found to be hacked 874 times
# Finished checking!
