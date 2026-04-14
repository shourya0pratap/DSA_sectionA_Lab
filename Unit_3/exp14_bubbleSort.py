def bubbleSort(arr):
    n = len(arr)
    swaps , comparisons = 0 , 0
    for i in range(n-1):
        for j in range(n-1-i):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swaps += 1
    
    print(f"Sorted List: {arr}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")


def main():
    lis = [67, 0, 13, -45, 314]
    bubbleSort(lis)

if __name__ == "__main__":
    main()