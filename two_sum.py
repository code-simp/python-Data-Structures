def two_sum(array,target):
    temp = set()
    for i in range(len(array)):
        if array[i] in temp:
            return True
        else:
            temp.add(target - array[i])
    return True

A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum(A,target))

