"""

{"apple": 2, "baby": 3, "ball": 5}
apple has weight 2, baby has weight 3 and ball has weight 5
Write a function that accepts the above input and randomly returns
a string based on its weight. For eg:
apple must be returned 20% of the times a function is called
baby must be returned 30% fo the times a function is called
ball must be returned 50% of the times a function is called

Also write the code to test distribution of the names
"""
import random


class randomGeneration:
    def __int__(self, values):
        self.names =[]
        self.weight = []
        for k, v in values.items():
            self.names.append(k)
            self.weight.append(v)
    def generateRandom(self):
        randomList = random.choice(self.names, self.weight, len(self.names))
        print(randomList)

obj = randomGeneration({"apple": 2, "baby": 3, "ball": 5})
obj.generateRandom()
