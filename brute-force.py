import time
import string
import argparse
from itertools import product


def check(target, chars, length):
    pws = product(chars, repeat=length)
    for pw in pws:
        if "".join(pw) == target:
            return "".join(pw)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--password", required=True,
                        help="Set password to attack")
    args = parser.parse_args()

    target = args.password
    chars = string.ascii_letters + string.digits + string.punctuation
    length = len(target)

    pw = check(target, chars, length)

    if (pw is None):
        print("Failure...")
    else:
        print("Solved: ", pw)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time() - start
    print(end, " sec.");

