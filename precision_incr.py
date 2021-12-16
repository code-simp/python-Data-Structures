def precision_incr(array):
    carry = 0
    array.reverse()
    for i in range(0,len(array)):
        if carry == 1:
            if array[i] + 1 == 10:
                array[i] = 0
                carry = 0
                continue
            array[i] = array[i]+1
            carry = 0
            break
        if array[i] + 1 == 10 and carry == 0:
            array[i] = 0
            carry = 1
    if carry ==1:
        array.append(1)
    return(array[::-1])

A1 = [9, 9, 9]
print(precision_incr(A1))       