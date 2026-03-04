# Simple Ternary Search

numbers = list(map(int, input("Enter sorted numbers separated by space: ").split()))
search = int(input("Enter number to search: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3

    if numbers[mid1] == search or numbers[mid2] == search:
        found = True
        break
    elif search < numbers[mid1]:
        high = mid1 - 1
    elif search > numbers[mid2]:
        low = mid2 + 1
    else:
        low = mid1 + 1
        high = mid2 - 1

if found:
    print("Number found")
else:
    print("Number not found")