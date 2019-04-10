#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import string
import random
from pynamesgenerator import gen_two_words, gen_year

class dataGenerate:
  """dataGenerate
  This class is used to generate random data, this class includes two functions.

  No attributes needed.
  """

  def genInt(self):
    """Generate random integers between 60 and 100."""
    return random.randint(60, 100)

  def dGen(self, size=100000):
    """Generate a random dict."""
    for i in range(size):
      name = gen_two_words()
      birth = gen_year(1970, 2000)
      flnum = random.uniform(20, 50)    # Generate a float number
      salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))    # Generate a random string
      data = {'name': name, 'birth': birth, 'floatnum': flnum, 'salt': salt, 'A': self.genInt(), 'B': self.genInt(), 'C': self.genInt()}
      yield data

# The following main method is only for test purpose, it shouldn't be used in
# the final program. So wrap it in `if __name__ == '__main__'` to prevent it
# run in the final program.

if __name__ == '__main__':
  f = open("randomGen_output.txt", "w")
  for i in dataGenerate().dGen():
    s = str(i)
    f.write(s + '\n')
  f.close()