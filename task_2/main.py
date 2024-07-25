def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return (iterations, mid_val)

        if mid_val < target:
            left = mid + 1
        else:
            upper_bound = mid_val
            right = mid - 1

    return (iterations, upper_bound)

def main():
	# Тестування
	sorted_array = [0.1, 0.5, 1.1, 2.3, 3.7, 4.4, 5.5]

	print(binary_search(sorted_array, 3))   # (3, 3.7)
	print(binary_search(sorted_array, 4.4)) # (2, 4.4)
	print(binary_search(sorted_array, 0.1)) # (3, 0.1)
	print(binary_search(sorted_array, 6))   # (3, None)

if __name__ == "__main__":
    main()