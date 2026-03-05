import sys

# Function for Linear Search
def linear_search(input_li: list, target: int) -> int:
    for i, value in enumerate(input_li):
        if value == target:
            return i
    return -1

# Read list from command line argument
li = sys.argv[1].strip('[]').split(',')
li = [int(i) for i in li]

# Read target value
target = int(sys.argv[2])

# Call the function and print result
result = linear_search(li, target)
print(result)