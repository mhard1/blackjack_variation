"""
Background
In a set of numbers, the mean is the average, the mode is the number that occurs the most,
and if you rearrange all the numbers numerically, the median is the number in the middle.

Goal
Create three functions that allow the user to find the mean, median, and mode of a list of numbers.
If you have access or know of functions that already complete these tasks, do not use them.
Subgoals
In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
If there is an even number of numbers in the list, return both numbers that could be considered the median.
If there are multiple modes, return all of them.
"""
#takes in and sorts a list of values from the user, and quits when user types in "q".
def get_numbers():

    print("Please input a number to add to the list. Press 'q' when you are finished.")
    set_of_values = []
    list_value = input(">")

    if list_value != "q":
        set_of_values.append(int(list_value))

    while list_value != "q":

        list_value = input(">")
        if list_value == "q":
            break
        set_of_values.append(int(list_value))

    print("These are your values:")
    print(sorted(set_of_values))
    return sorted(set_of_values)

# Calculate the average based on the user`s list. User inputs how many places to round the number to.
def calc_mean(user_list):
    num_of_values = len(user_list)
    round_to = int(input("Please enter how many decimal places you want the answer rounded to:"))
    total_sum = 0
    for i in range(len(user_list)):
        total_sum += user_list[i]
    mean = round(total_sum / num_of_values, round_to)
    print("Your average is:", mean)

# calculates the mode of a group of numbers. If there are more than one mode, it gives back all modes.
def calc_mode(user_list):
    potential_mode_group = []
    potential_mode_set = {}

    mode_is = {}

    for i in range(len(user_list)):
        potential_mode_group.append(user_list.count(user_list[i]))
        potential_mode_set[user_list[i]] = user_list.count(user_list[i])

    mode_key_group = [x for x in (potential_mode_set.keys())]
    max_value = max(potential_mode_set.values())

    for i in range(len(mode_key_group)):
        if potential_mode_set.get(mode_key_group[i]) == max_value:
            mode_is[mode_key_group[i]] = max_value

    mode_value_group =[x for x in (mode_is.keys())]

    if len(mode_value_group) > 1:
        print("Here are the modes:")
        for i in range(len(mode_value_group)):
            print(mode_value_group[i])
    else:
        print("The mode is", mode_value_group[0])

# calculates the median number in the list of numbers input from the user.
def calc_median(user_list):
    list_length = len(user_list)

    if (list_length) % 2 == 0:
        median_index = int(list_length / 2)
        median_index_2 = median_index - 1
        print("The medians are:", user_list[median_index_2], "and", user_list[median_index])

    else:
        median_index = int((list_length - 1) / 2)
        print("The median is", user_list[median_index])

user_list = get_numbers()
calc_mean(user_list)
calc_mode(user_list)
calc_median(user_list)
