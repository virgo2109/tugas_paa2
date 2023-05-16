def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Contoh penggunaan
arr = [67, 74, 15, 10, 27, 18, 99]
bubble_sort(arr)
print("Hasil Bubble Sort:")
for i in range(len(arr)):
    print(arr[i])