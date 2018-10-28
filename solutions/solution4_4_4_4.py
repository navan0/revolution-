def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    length = int(input("length=:\n"))
    arr = []
    print("Enter elements:")
    for i in range(length):
        arr.append(int(input()))

    sorted_arr = bubble_sort(arr)

    print ("Sorted array is:")
    for i in range(length):
        print(arr[i])
