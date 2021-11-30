import sys


def check_records(txt):
    _ = txt.pop(0)
    eve = txt.pop(0)
    for record in txt:
        the_day = record
        if the_day == eve:
            print(f"stay")
        elif the_day < eve:
            print(f"down {eve - the_day}")
        elif the_day > eve:
            print(f"up {the_day - eve}")
        eve = the_day


if __name__ == "__main__":
    inputs = []
    for line in sys.stdin:
        inputs.append(int(line))
    check_records(inputs)
