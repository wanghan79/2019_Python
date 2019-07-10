import ast

import matplotlib.pyplot as plt

filename = 'gen_data.txt'
add1 = 0
add2 = 0
add3 = 0
add4 = 0
add5 = 0
add6 = 0
add7 = 0
add8 = 0
add9 = 0

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0


def read_data(filename):
    result = []
    file = open(filename)
    for line in file:
        dict = ast.literal_eval(line)
        result = tuple(dict.values())
        yield result


def pre_data(filename):
    for result in read_data(filename):
        if result[2] == '湖南':
            global add1
            global count1
            add1 = add1 + result[1]
            count1 = count1 + 1
        elif result[2] == '青海':
            global add2
            global count2
            add2 = add2 + result[1]
            count2 = count2 + 1
        elif result[2] == '河南':
            global add3
            global count3
            add3 = add3 + result[1]
            count3 = count3 + 1
        elif result[2] == '四川':
            global add4
            global count4
            add4 = add4 + result[1]
            count4 = count4 + 1
        elif result[2] == '江西':
            global add5
            global count5
            add5 = add5 + result[1]
            count5 = count5 + 1
        elif result[2] == '湖北':
            global add6
            global count6
            add6 = add6 + result[1]
            count6 = count6 + 1
        elif result[2] == '贵州':
            global add7
            global count7
            add7 = add7 + result[1]
            count7 = count7 + 1
        elif result[2] == '广东':
            global add8
            global count8
            add8 = add8 + result[1]
            count8 = count8 + 1
        else:
            global add9
            global count9
            add9 = add9 + result[1]
            count9 = count9 + 1


if __name__ == '__main__':
    pre_data(filename)
    province = ['hunan', 'qinghai', 'henan', 'sichuan', 'jiangxi', 'hubei', 'guizhou', 'guangdong', 'guangxi']
    average = [add1 / count1, add2 / count2, add3 / count3, add4 / count4, add5 / count5, add6 / count6, add7 / count7,
               add8 / count8, add9 / count9]
    plt.barh(range(len(average)), average, tick_label=province)
    plt.show()
