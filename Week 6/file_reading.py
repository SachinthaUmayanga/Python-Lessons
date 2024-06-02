# f = open('sample.txt',"r")
# print(type(f),f)
# lines = f.readlines()
# print(type(lines))

# print(lines[5])
# for line in lines:
#     if line != "":
#         print(line)

# lines = f.strip().readlines()
# print(lines)


# =========== with statement ===================
# with open ("sample.txt") as my_file:
#     print(my_file.read())

# with open ("sachintha.txt","w")as my_file:
#     my_file.write("Hello world \n")
#     my_file.write("I hope you're doing well today \n")

# with open ("sachintha.txt")as my_file1:
#     print(my_file1.read())
#####################################################


############ chaeck the emails are valid or invalid ################
# email = input("Email Address: ")

# def validate_email(email:str)-> bool:
#     if email.count("@") == 1:
#         split_email = email.split('@')
#         if len(split_email[0]) > 3 and len(split_email[1]) > 3:
#             return True
#         else:
#             False
#     else:
#         False

# print(f"Your Email is {validate_email(email)}")


from email_validation import Validation

print(Validation.is_valid_email("sachinthaumayanga3@gmail.com"))