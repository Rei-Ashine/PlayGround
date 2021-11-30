import sys
import csv

def main(argv):
    out = []
    for i, v in enumerate(argv):
        with open(v) as f:
            reader = csv.reader(f)
            data = [row for row in reader]
            out += data

    out = sorted(out)
    for i in out:
        print("{},{},{}".format(i[0], i[1], i[2]))


if __name__ == '__main__':
    main(sys.argv[1:])

