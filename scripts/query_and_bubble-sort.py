import sys
import string


def loader() -> list:
    """
    Read standard input.
    """
    data = [[str(c) for c in line.split()] for line in sys.stdin]
    if len(data) == 0:
        data = [[]]
    return data


def ask(x, y):
    text = "? " + str(x) + " " + str(y)
    print(text)
    operator = loader()
    return operator[0]


def bubble_sort(data):
    step = 0
    for i in range(len(data)):
        for j in range(len(data)-1, i, -1):
            ans = ask(data[j-1], data[j])
            step += 1
            if ans == ">":
                data[j], data[j-1] = data[j-1], data[j]
    answer = "".join(data)
    print("!" + answer)


if __name__ == "__main__":
    constraint = loader()
    # Read the first line
    constraint = constraint[0]
    num = constraint.pop(0)
    query = constraint.pop(0)

    labels = list(string.ascii_uppercase)
    labels = labels[0:int(num)]
    bubble_sort(labels)
