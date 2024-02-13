import random
def test_create_random():
    num_list = []
    for i in range(0, random.randint(1, 10), 1):
        num_list.append(random.randint(1, 100))
    print(num_list)
    new_list = []
    pos = 0
    if len(num_list) == 1:
        print(num_list[0])
    else:
        for i in num_list:
            pos += 1
            if pos == 1:
                print(i, ":", num_list[len(num_list) - 1], "+", num_list[pos], "=", int(num_list[len(num_list) - 1]) + int(num_list[pos]))
                new_list.append(int(num_list[len(num_list) - 1]) + int(num_list[pos]))
            elif pos == len(num_list):
                print(i, ":", num_list[pos - 2], "+", num_list[0], "=", int(int(num_list[pos - 2]) + int(num_list[0])))
                new_list.append(int(num_list[pos - 2]) + int(num_list[0]))
            else:
                print(i, ":", num_list[pos - 2], "+", num_list[pos], "=", int(num_list[pos - 2]) + int(num_list[pos]))
                new_list.append(int(num_list[pos - 2]) + int(num_list[pos]))

