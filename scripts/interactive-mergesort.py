import random
from string import ascii_uppercase


def merge_sort(data):
    """
    Sort the elements of list items using the merge-sort algorithm.
    """
    database = dict()

    def query(x, y) -> str:
        text = f"? {str(x)} {str(y)}"
        if text in database:
            reply = database[text]
        else:
            print(text)
            reply = input()
            database[text] = reply
        return reply

    def merge(left, right):
        """
        Merge two sorted lists 'left' and 'right' into sorted items.
        """
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            ans = query(left[i], right[j])
            if ans == "<":
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        if i < len(left):
            merged.extend(left[i:])
        if j < len(right):
            merged.extend(right[j:])
        return merged

    n = len(data)
    if n < 2:
        return data
    # Divide
    mid = n // 2
    first_half = data[:mid]
    latter_half = data[mid:]

    first_half = merge_sort(first_half)
    latter_half = merge_sort(latter_half)
    return merge(first_half, latter_half)


def ford_johnson(data):
    def query(x, y):
        print(f"? {x} {y}")
        return input()

    def binary_search_insertion(sorted_list, item):
        left = 0
        right = len(sorted_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if left == right:
                if query(sorted_list[mid], item) == "<":
                    left = mid + 1
                    break
                else:
                    break
            elif query(sorted_list[mid], item) == "<":
                left = mid + 1
            else:
                right = mid - 1
        sorted_list.insert(left, item)
        return sorted_list

    result = []

    def sort_list_2d(list_2d):

        def merge(left, right):
            while left and right:
                if query(left[0][0], right[0][0]) == "<":
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            return result + left + right

        length = len(list_2d)
        if length <= 1:
            return list_2d
        mid = length // 2
        return merge(sort_list_2d(list_2d[:mid]), sort_list_2d(list_2d[mid:]))

    if len(data) <= 1:
        return data
    two_paired_list = []
    is_surplus = False
    for i in range(0, len(data), 2):
        if i == len(data)-1:
            is_surplus = True
        else:
            if query(data[i], data[i + 1]) == "<":
                two_paired_list.append([data[i], data[i + 1]])
            else:
                two_paired_list.append([data[i + 1], data[i]])
    sorted_list_2d = sort_list_2d(two_paired_list)
    result = [i[0] for i in sorted_list_2d]
    result.append(sorted_list_2d[-1][1])

    if is_surplus:
        pivot = data[-1]
        result = binary_search_insertion(result, pivot)

    is_surplus_inserted_before_this_index = False
    for i in range(len(sorted_list_2d) - 1):
        if result[i] == data[-1]:
            is_surplus_inserted_before_this_index = True
        pivot = sorted_list_2d[i][1]
        if is_surplus_inserted_before_this_index:
            result = result[:i+2] + binary_search_insertion(result[i+2:], pivot)
        else:
            result = result[:i+1] + binary_search_insertion(result[i+1:], pivot)
    return result


if __name__ == "__main__":
    # Read the first line
    N, Q = map(int, input().split())

    # Generate labels
    elements = list(ascii_uppercase[:int(N)])
    random.shuffle(elements)

    # Merge sort
    if len(elements) < 11:
        # Reference: https://github.com/decidedlyso/merge-insertion-sort.git
        sorted_elements = ford_johnson(elements)
    else:
        sorted_elements = merge_sort(elements)

    # Print answer
    answer = "".join(sorted_elements)
    print(f"! {answer}")
