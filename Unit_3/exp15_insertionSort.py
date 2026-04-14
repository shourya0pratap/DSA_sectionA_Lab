def insertionSort(arr):
    n = len(arr)
    swaps , comparisons = 0 , 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                swaps += 1
                arr[j+1] = arr[j]
                j -= 1
            else:
                break

        arr[j+1] = key

    print(f"Sorted List: {arr}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")


def main():
    lis = [67, 0, 13, -45, 314]
    insertionSort(lis)

if __name__ == "__main__":
    main()