def quickSort(lis, low=0, high=None):
    if high is None:
        high = len(lis) - 1
    if low < high:
        pivot_index = partition(lis, low, high)
        quickSort(lis, low, pivot_index-1)
        quickSort(lis, pivot_index+1, high)

def partition(lis, low, high):
    pivot = lis[high]
    i = low - 1
    for j in range(low, high):
        if lis[j] <= pivot:
            i += 1
            lis[i], lis[j] = lis[j], lis[i]
    lis[i+1], lis[high] = lis[high], lis[i+1]
    return i+1

def main():
    lis = [67, 0, 13, -45, 314]
    quickSort(lis)

if __name__ == "__main__":
    main()