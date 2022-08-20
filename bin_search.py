def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) #python automatically round down if it's an odd number
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]

ex1= binary_search(my_list, 3) #should print 1
ex2= binary_search(my_list, 1) #should print 0
ex3= binary_search(my_list, 2) #should return None

print(ex1, ex2, ex3) #that's it
