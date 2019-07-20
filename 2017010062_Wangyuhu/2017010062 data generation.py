import random

import string



class DataGeneration:

    """Generate random data"""



    STR = [chr(i) for i in range(65, 91)]

    str = [chr(i) for i in range(97, 123)]

    number = [chr(i) for i in range(48, 58)]

    initspecial = string.punctuation



    @staticmethod

    def str_generation():  # 生成字符串

        special = []

        for i in DataGeneration.initspecial:

            special.append(i)

        total = DataGeneration.STR + DataGeneration.str + DataGeneration.number + special

        return ''.join(random.sample(total, random.randint(1, 10)))



    @staticmethod

    def dict_key_generation():  # 生成键值对

        total = DataGeneration.STR + DataGeneration.str

        str = ''.join(random.sample(total, random.randint(1, 10)))

        length = len(str)

        mydict = {str: length}

        return mydict



    @staticmethod

    def data_generation(filename, size):  # 生成随机数据,起始id为start_id，包含0-100的随机整数、随机浮点数、随机字符串、随机键值对

        f = open(filename, "w")

        for i in range(0, size):

            data = {"_id": i,

                    "random_int": random.randint(0, 100),

                    "random_float": random.uniform(0, 100),

                    "random_string": DataGeneration.str_generation(),

                    "random_dict": DataGeneration.dict_key_generation()}

            s = str(data)

            f.write(s + '\n')