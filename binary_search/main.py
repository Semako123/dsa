def binary_search(arr, target):
    mid = (len(arr)) // 2

    if len(arr) == 1:
        return target == arr[0] 
    
    if len(arr) == 0:
        return False
    
    if arr[mid] == target:
        return True
    elif target > arr[mid]:
        return binary_search(arr[mid + 1 :], target)
    else:
        return binary_search(arr[:mid], target)


def main():
    arr = list(range(1, 10001))
    print(binary_search(arr, 10003))


if __name__ == "__main__":
    main()
