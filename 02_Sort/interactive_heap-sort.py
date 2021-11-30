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


def swap(array, x, y):
    tmp = array[x]
    array[x] = array[y]
    array[y] = tmp


def heap_sort(array):
    i = 0
    n = len(array)
    while i < n:
        up_heap(array, i)
        i += 1
    while i > 1:
        i -= 1
        swap(array, 0, i)
        down_heap(array, i - 1)
    return array


def up_heap(array, n):
    while n != 0:
        parent = int((n - 1) / 2)
        ans = query(array[n], array[parent])
        if ans == ">":
            swap(array, n, parent)
            n = parent
        else:
            break


def down_heap(array, n):
    if n == 0:
        return
    parent = 0
    while True:
        child = 2 * parent + 1
        if child > n:
            break
        ans = query(array[child], array[child + 1])
        if (child < n) and ans == "<":
            child += 1
        ans = query(array[parent], array[child])
        if ans == "<":
            swap(array, child, parent)
            parent = child
        else:
            break


if __name__ == "__main__":
    # Read the first line
    N, Q = map(int, input().split())

    # Generate labels
    elements = list(ascii_uppercase[:int(N)])
    random.shuffle(elements)

    # Bubble sort
    sorted_elements = heap_sort(elements)

    # Print answer
    answer = "".join(sorted_elements)
    print(f"! {answer}")
