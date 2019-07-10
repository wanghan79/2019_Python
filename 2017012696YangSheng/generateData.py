import random


def gen_id():
    list = range(201701000000, 201701999999)
    return random.sample(list, 200000)


def gen_score():
    return round(random.random() * 100, 1)


def gen_origin():
    list = ['湖南', '青海', '河南', '四川', '江西', '湖北', '贵州', '广东', '广西']
    return random.choice(list)


def gen_sex():
    a = random.randint(0, 1)
    if a == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    id = gen_id()
    score = []
    origin = []
    sex = []
    for i in range(0, 200000):
        score.append(gen_score())
        origin.append(gen_origin())
        sex.append(gen_sex())

    file = open('gen_data.txt', 'w')
    for i in range(0, 200000):
        data = {'id': id[i], 'score': score[i], 'origin': origin[i], 'sex': sex[i]}
        file.write(str(data) + '\n')
    file.close()
