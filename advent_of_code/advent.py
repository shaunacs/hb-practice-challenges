expense_file = open('expenses.txt')
expense_file = expense_file.readlines()
expenses = []

for line in expense_file:
    expenses.append(int(line.rstrip()))

expenses_set = set(expenses)

desired_sum = 2020

def check_for_sum(num_lst, num_set, sum_num):
    """Checks if there are two numbers that equal desired sum"""

    for num in num_lst:
        num = int(num)
        num_lookup = sum_num - num
        if num_lookup in num_lst:
            print(f'{num} & {sum_num - num}')

num_to_reach_sum = []
for num in expenses:
    num_to_reach_sum.append(2020 - num)
    # print(f'{num} {2020 - num}')

for num in num_to_reach_sum:
    if num in expenses:
        print(f'{num}')

def find_three_num_sum(expense_lst):
    """Takes in a list of numbers and finds three nums that sum to 2020"""

    three_nums = []
    adder = 0
    while len(three_nums) < 3:
        for num in expense_lst:
            adder = adder + num
        