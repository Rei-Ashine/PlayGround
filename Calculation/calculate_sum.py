import sys


def calculate_sum(txt):
    a = txt.pop(0)
    b, c = txt.pop(0).split()
    name = txt.pop(0)
    answer = int(a) + int(b) + int(c)
    print(f"{answer} {name}")


if __name__ == "__main__":
    inputs = []
    for line in sys.stdin:
        inputs.append(line)
    calculate_sum(inputs)

