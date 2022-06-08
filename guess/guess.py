import random


class GuessColor():

    def __init__(self, n=100):
        self.colors = ('blue', 'green', 'red')
        self.distribution = {'blue': 80, 'green': 15, 'red': 5}
        self.n = n
        temp = []
        memo = {}
        for key, val in self.distribution.items():
            temp.extend([key] * val)
        for item in temp:
            memo[random.random()] = item
        self._box = []
        for key in sorted(memo.keys()):
            self._box.append(memo[key])

    def guess(self):
        guess = random.randint(0, self.n)
        if guess > (self.distribution['green'] + self.distribution['red']):
            return 'blue'
        elif guess > self.distribution['red']:
            return 'green'
        else:
            return 'red'

    def check(self,k):
        chk = self.guess()
        return chk, chk == self._box[k]
