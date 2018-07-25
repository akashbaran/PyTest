"""Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.

Hints:
Use if/elif to deal with conditions.

"""
lst = [1,3,5,8,12,17,34,67,89]
item = int(input("enter the search item "))
end = len(lst)-1
start = 0
while(start <= end):
    mid = int((end + start)/2)
    if lst[mid] == item:
        print(mid)
        break
    elif item > lst[mid]:
        start = mid +1
    elif item < lst[mid]:
        end = mid - 1



