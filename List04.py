def main(numbers,i):
    """
    You are given a list of numbers. i Delete and return the number in the index.
    Args:
        numbers(list): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    w=numbers.pop(i)

    return w
print(main([1, 2, 3, 4, 5], i = 2))
