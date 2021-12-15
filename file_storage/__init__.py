from copy import copy


class a:

    def __init__(self):
        self.b = 5


a1 = a()
a2 = copy(a1)

print(a1 == a2, a1 is a2)

