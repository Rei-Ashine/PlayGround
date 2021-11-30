import sys


def main(lines):
    _ = lines.pop(0)

    for i, v in enumerate(lines):
        h = int(v[:-2]) + 9
        m = int(v[-2:])
        if h >= 24:
            h = h - 24
        print("{} {}".format(h, m))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

