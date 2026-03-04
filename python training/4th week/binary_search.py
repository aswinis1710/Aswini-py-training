# Simple Binary Search

numbers = list(map(int, input("Enter sorted numbers separated by space: ").split()))
search = int(input("Enter number to search: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == search:
        found = True
        break
    elif numbers[mid] < search:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Number found")
else:
    print("Number not found")