import sys


database = dict()
for i in range(12):
    database[i] = []


if __name__ == "__main__":
    # Target
    food = int(sys.argv[1])

    # Pairs
    path = "./data/pairs.txt"
    with open(path, 'r') as f:
        pairs = f.read().split("\n")
    pairs = [i for i in pairs if i != ""]

    # Database
    for i in pairs:
        h, t = map(int, i.split())
        if h == t:
            continue
        else:
            temp = database[h]
            temp.append(t)
            database[h] = list(set(temp))
            temp = database[t]
            temp.append(h)
            database[t] = list(set(temp))

    # Query
    answer = []
    q = database[food]
    if len(q) != 0:
        for i in q:
            res = database[i]
            answer.extend(res)

    answer = list(set(answer))
    answer.remove(food)
    answer = map(str, answer)

    print(" ".join(answer))

