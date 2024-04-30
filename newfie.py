def frequency(array, k):

    dictionary={}
    for i in range(len (array)):
        element = array[i]
        
        if element in dictionary:
            dictionary[element]+=1
        else:
            dictionary[element] = 1
    
    return dictionary

print(frequency([1,1,1,2,2,3],1))


        