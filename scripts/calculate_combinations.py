import sys


TARGET_VALUE = 1500


def calc_comb(items, target_value):
    """ Calculate a combination of numbers whose total value is the target value. """
    def calc(i, comb, res, target):
        if target == sum(comb):
            res.append(comb)
        elif target < sum(comb):
            return
        for j in range(i, len(items)):
            calc((j + 1), (comb + [items[j]]), res, target)
        return res
    return calc(0, [], [], target_value)


if __name__ == "__main__":
    # Receive standard inputs
    args = sys.argv
    potato = [float(i) for i in args[1:]]

    # Calculate combinations
    patterns = calc_comb(potato, TARGET_VALUE)

    # Return the result
    result = "yes" if len(patterns) != 0 else "no"
    print(result)
