temp_list = list(map(int, input().split()))
commercials = temp_list[0]
cost = temp_list[1]
students = list(map(int, input().split()))
max_profit = 0

for i in range(len(students)):
    for j in range(i, len(students)):
        sub_list = students[i:j] # Iterate over every sublist
        profit = sum(sub_list) - (cost * len(sub_list))
        
        if profit > max_profit:
            max_profit = profit
        
        profit = 0

print(max_profit)
