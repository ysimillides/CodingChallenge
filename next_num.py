import random
import numpy as _np
epsilon = _np.finfo(float).eps # to avoid floating_point errors

class RandomGen(object):
#takes parameters random_numbs and probabilities
    def __init__(self, random_nums, probabilities):
        self._random_nums = random_nums  #  Values that may be returned by next_num()
        self._probabilities = probabilities  # Probability of the occurence of random_nums
        # the following lines are to sanitize the input, ie make sure the probabilities exist and correspond to the numbers
        if len(probabilities) != len(random_nums):
            raise ValueError("Random numbers must correspond to probabilities")
        total = 0
        for p in (probabilities):
            total = total + p
            if p>1 or p<0:
                raise ValueError("probabilities must be between 0 and 1")
        if total-1 > abs(epsilon):
            raise ValueError("Sum of probabilities must be 1 ")

    @property
    def probabilities(self):
        return self._probabilities

    @property
    def random_nums(self):
        return self._random_nums

    def next_num(self):
        random_prob = random.random()
        count_prob = 0
        for position, prob in enumerate(self.probabilities):
            count_prob += prob
            if random_prob < count_prob:
                number = self.random_nums[position]
                return number

