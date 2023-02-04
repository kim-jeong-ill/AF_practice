arr = [8, 3, 0, 9, 1, 6, 2, 4, 7, 5]

n = len(arr) # 10

for i in range(n): # 0-9 10개
    
    min_idx = i
    
    for j in range(i+1, n): #1-10 9개
        if (arr[min_idx] > arr[j]):
            min_idx = j
            
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
