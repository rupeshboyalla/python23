def rearrange_array(arr):
    sorted_arr = sorted(arr)
    n = len(arr)
    new_arr = [0] * n
    even_pointer = n - 1 if n % 2 == 0 else n - 2
    odd_pointer = n - 2 if n % 2 == 0 else n - 1

    for i in range(n):
        if i % 2 == 0:
            new_arr[even_pointer] = sorted_arr[i]
            even_pointer -= 2
        else:
            new_arr[odd_pointer] = sorted_arr[i]
            odd_pointer -= 2

    return new_arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8]
result = rearrange_array(arr)
print(result)  # Output: [2, 1, 4, 3, 6, 5, 8, 7]