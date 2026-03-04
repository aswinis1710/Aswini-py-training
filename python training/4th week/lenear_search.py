# Simple Linear Search

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
search = int(input("Enter number to search: "))

found = False

for num in numbers:
    if num == search:
        found = True
        break

if found:
    print("Number found")
else:
    print("Number not found")