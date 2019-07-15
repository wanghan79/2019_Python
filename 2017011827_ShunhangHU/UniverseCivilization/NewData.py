import random


class Civilization:
    name = ''
    age = 0
    grade = ''
    type = ''
    position = {'X': 0, 'Y': 0, 'Z': 0}

    def __init__(self):
        tempName = random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(5, 10))
        self.name = ''.join(tempName).capitalize()
        self.age = random.uniform(0, 13820000)
        self.grade = random.choice(['A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E'])
        self.type = random.choice(['碳基生命', '硅基生命', '硼基生命',  '金属生命', '电磁生命', '恒星生命'])
        self.position['X'] = random.randint(-5000, 5000)
        self.position['Y'] = random.randint(-5000, 5000)
        self.position['Z'] = random.randint(-5000, 5000)

    def war(self):
