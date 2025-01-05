# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

num_list = [2,13,15,10,15,35,60]

result = list(filter(lambda a: (a % 5 == 0),num_list))

print("Numbers divisible by 5 are: ",result)