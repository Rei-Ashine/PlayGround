import random
from string import ascii_uppercase

database = dict()


def query(x, y) -> str:
    text = f"? {str(x)} {str(y)}"
    inverse = f"? {str(y)} {str(x)}"
    if text in database:
        reply = database[text]
    elif inverse in database:
        opposite = database[inverse]
        if opposite == ">":
            reply = "<"
        else:
            reply = ">"
    else:
        print(text)
        reply = input()
        database[text] = reply
    return reply


def bubble_sort(data):

    step = 0
    for i in range(len(data)):
        for j in range(len(data)-1, i, -1):
            ans = query(data[j-1], data[j])
            step += 1
            if ans == ">":
                data[j], data[j-1] = data[j-1], data[j]
    return data


if __name__ == "__main__":
    # Read the first line
    N, Q = map(int, input().split())

    # Generate labels
    elements = list(ascii_uppercase[:int(N)])
    random.shuffle(elements)

    # Bubble sort
    sorted_elements = bubble_sort(elements)

    # Print answer
    answer = "".join(sorted_elements)
    print(f"! {answer}")
