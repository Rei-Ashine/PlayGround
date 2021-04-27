import time
import string
import zipfile
import argparse
from tqdm import tqdm
from itertools import product


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True,
                        help="Set target zip file")
    args = parser.parse_args()
    input_path = args.input
    # Brute-Force attack
    attacker(input_path)


def attacker(path):
    with zipfile.ZipFile(path, "r") as zf:
        chars = string.ascii_letters + string.digits + string.punctuation
        length = 4
        pws = product(chars, repeat=length)
        num= len(chars) ** length
        count = 0
        for pw in tqdm(pws, total=num, position=0, leave=False, ncols=80):
            pwd = bytes("".join(pw), "UTF-8")
            try:
                zf.extractall(path=".", pwd=pwd)
                print("\n\nSolved: ", pwd)
                break
            except Exception as e:
                count += 1
    print("The number of trials: ", count)


if __name__ == "__main__":
    main()
