
# In each iteration print the sum of the current number and previous number

list = [1,2,3,4,5,6,7,8,9,10]

prev_number = 0

for i in range(1,11):
    x_sum = prev_number + i
    print("Current number", i ,"previous number", "sum", x_sum)

    prev_number = i


