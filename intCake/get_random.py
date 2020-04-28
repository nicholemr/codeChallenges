import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    shuffled = []

    for item in the_list:
        pick = pick_random(shuffled, the_list)
        shuffled.append(pick)
    print('shuffled', shuffled)
    return shuffled


def pick_random(shuf, origlist):
    rem_nums = []
    for num in origlist:
        if num not in shuf:
            rem_nums.append(num)
    return random.choice(rem_nums)


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
