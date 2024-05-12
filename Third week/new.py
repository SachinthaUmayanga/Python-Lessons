# val = (input("Enter true or false: "))

# def chang_mode(val : str) -> bool:
#     var = None
#     if val == "true":
#         var = False
#     if val == "false":
#         var = True

#     return var

# print(chang_mode(val))


# for num in range(1,10,3):
#     print("Odd numbers: ",num)

# for num in range(1,11,2):
#     print("Even numbers: ",num)


# =============== print the even and odd numbers between 1 to 10=============================
start_no = input("Enter start no: ")
end_no = input("Enter end no: ")

numbers = [i for i in range(int(start_no),int(end_no),1)]
print(numbers)

def checked_odd_or_even(numbers: list) -> dict:
    odd_list = []
    eve_list = []
    for number in numbers:
        if float(number)%2 == 0:
            eve_list.append(number)
        else:
            odd_list.append(number)
    return{
        "odd list": odd_list,
        "even list": eve_list
    }

print(checked_odd_or_even(numbers))