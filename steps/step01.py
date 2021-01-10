import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data


class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, x):
        raise NotImplementedError()


class Sqaure(Function):
    def forward(self, x):
        return x ** 2


x = Variable(np.array(3.0))
f = Sqaure()
y = f(x)

print(type(y))
print(y.data)
