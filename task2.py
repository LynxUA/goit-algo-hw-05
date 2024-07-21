def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_limit = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_limit = arr[mid]
            right = mid - 1
    
    return iterations, upper_limit

sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
target_value = 4.5
result = binary_search(sorted_array, target_value)
print(f"Iterations: {result[0]}, Upper Limit: {result[1]}")
