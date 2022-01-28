import random

# Bill Splitter
# Project courtesy of JetBrains Academy
#
# My first project in Python just to help me learn the basics
# Program intended to help split the bill for a group out to dinner 
#
# Author: Anders Gilliland
# Last Updated: 28-1-2022

print('Enter the number of friends joining (including you):')
num_friends = int(input())

if num_friends < 1:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), '
          'each on a new line:')
    friend_dict = dict()
    for _ in range(num_friends):
        friend_dict[input()] = 0

    print('Enter the total bill value:')
    bill_value = int(input())
    split_value = round(bill_value / num_friends, 2)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_choice = input()
    if lucky_choice == 'Yes':
        lucky_friend = random.choice(list(friend_dict))
        print(lucky_friend, ' is the lucky one!')

        split_value = round(bill_value / (num_friends - 1), 2)

        for friend in friend_dict:
            if friend == lucky_friend:
                friend_dict[friend] = 0
            else:
                friend_dict[friend] = split_value
    else:
        print('No one is going to be lucky')

        for friend in friend_dict:
            friend_dict[friend] = split_value

    print(friend_dict)
