def jump_game2(array):
    max_reach = 0
    for i in range(0,len(array)):
        if i > max_reach:
            return False
        max_reach = max(max_reach,array[i]+i)
    print(max_reach)
    return max_reach >= len(array)-1

A = [2,0,0]
print(jump_game2(A))
