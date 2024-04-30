
def bubblesort(arr):
    for i in range (len(arr)-1):
        for j in range (i,len(arr)):
            if arr[i] >= arr[j]:
                tmp = arr[j]
                
                arr[j] = arr[i]
                arr[i] = tmp 
    
    return arr

# Example usage with print
my_array = [4, 2, 7, 1, 9, 10, 43, 15,7]
bubblesort(my_array)
print("Sorted array:", my_array)