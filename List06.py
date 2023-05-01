def main(fruits):
    """
    Given a list called Fruits, it contains at least one apple. Find how many apples are on the list and return.
    Args:
        fruits(list): parameter
    Returns:
        int: return answer
    """
    i=0
    n=0
    while i<len(fruits):
        if fruits[i]=="apple":
            n=n+1
        i=i+1 
    return n
print(main(["apple", "banana", "apple", "pear"]))