import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    lst = []
    
    while len(lst) != 100:
        Val = random.randint(0, 1)
        if Val == 0:
            lst.append('T')
        elif Val == 1:
            lst.append('H')   
            
    # Code that checks if there is a streak of 6 heads or tails in a row
    count = 1;
    for i in range(1, 100):
        if lst[i] == lst[i-1]:
            count += 1
            if count >= 6:
                number_of_streaks += 1
                break
        else:
            count = 1



print('Chance of streak: %s%%' % (number_of_streaks / 100))