import string

def how_many_times(msg):
    count = 0
    alpha_list = list(string.ascii_lowercase)

    for alpha in list(msg):
        count += alpha_list.index(alpha) + 1

    return count

print(how_many_times("abde"))
