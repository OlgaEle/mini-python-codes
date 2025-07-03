if __name__ == '__main__':
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        if not (2 <= n <= 10):
            raise ValueError('n must be between 2 and 10')
        if not all(-100 <= i <= 100 for i in arr):
            raise ValueError('i in array must be between -100 and 100')
        max_value = max(arr)
        res = [val for idx, val in enumerate(arr) if val != max_value]
        result = max(res)
        print(result)
        
    except ValueError as e:
        print(e)
