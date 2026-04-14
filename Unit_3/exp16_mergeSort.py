def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    L = arr[:mid]
    R = arr[mid:]
    SL = mergeSort(L)
    SR = mergeSort(R)
    return merge(SL, SR)

def merge(SL, SR):
    m = len(SL)
    n = len(SR)
    i , j = 0 , 0
    res = []
    while i < m and j < n:
        if SL[i] < SR[j]:
            res.append(SL[i])
            i += 1
        else:
            res.append(SR[j])
            j += 1
    res.extend(SL[i:])
    res.extend(SR[j:])
    return res

def main():
    lis = [67, 0, 13, -45, 314]
    lisSorted = mergeSort(lis)
    print(lisSorted)

if __name__ == "__main__":
    main()