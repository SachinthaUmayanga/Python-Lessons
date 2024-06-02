def check_zeros (values: list)->int:
    count = 0
    for val in values:
        if val == 0:
            count = count+ 1
    return count

print(check_zeros([0,1,2,0,5]))

def check_zeros_2(values: list)-> int:
    return values.count(0)

print(check_zeros_2([0,0,1,0]))