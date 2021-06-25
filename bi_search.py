
def binary_search(arr, low, high, x):
	if high >= low:

		mid = (high + low) // 2


		if arr[mid] == x:
			return mid


		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)


		else:
			return binary_search(arr, mid + 1, high, x)

	else:

		return False

# Test array
arr1 =list( map(int,input('Enter your list : ').split()))
arr=arr1.copy()

arr.sort()

x = int(input('Enter the number you want to find : '))

result = binary_search(arr, 0, len(arr)-1, x)

if result != False:
	print("Element is present at index",arr1.index(arr[result]))
else:
	print("Element is not present in array")
