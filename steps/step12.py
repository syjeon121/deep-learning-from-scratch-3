import numpy as np
import unittest


class SqaureTest(unittest.TestCase):
    def test_forward(self):
        x = Variable(np.array(2.0))
        y = sqaure(x)
        expected = np.array(4.0)
        self.assertEqual(y.data, expected)

    def test_backward(self):
        x = Variable(np.array(3.0))
        y = sqaure(x)
        y.backward()
        expected = np.array(6.0)
        self.assertEqual(x.grad, expected)

    def test_gradient_check(self):
        x = Variable(np.random.rand(1))
        y = sqaure(x)
        y.backward()
        num_grad = numerical_diff(sqaure, x)
        flg = np.allclose(x.grad, num_grad)
        self.assertTrue(flg)


class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError('{}은(는) 지원하지 않습니다. '.format(type(data)))

        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)

        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            gys = [output.grad for output in f.outputs]
            gxs = f.backward(*gys)
            if not isinstance(gxs, tuple):
                gxs = (gxs,)

            for x, gx in zip(f.inputs, gxs):
                x.grad = gx

                if x.creator is not None:
                    funcs.append(x.creator)


class Function:
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)  # 별표를 붙여 언팩
        if not isinstance(ys, tuple):  # 튜플이 아닌 경우 추가 지원
            ys = (ys,)
        outputs = [Variable(as_array(y)) for y in ys]

        for output in outputs:
            output.set_creator(self)

        self.inputs = inputs
        self.outputs = outputs

        # 리스트의 원소가 하나라면 첫 번째 원소를 반환한다.
        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, xs):
        raise NotImplementedError()

    def backward(self, gys):
        raise NotImplementedError()


class Add(Function):
    def forward(self, x0, x1):
        y = x0 + x1
        return y

    def backward(self, gy):
        return gy, gy


class Sqaure(Function):
    def forward(self, x):
        return x ** 2

    def backward(self, gy):
        x = self.inputs[0].data
        gx = 2 * x * gy
        return gx


# class Exp(Function):
#     def forward(self, x):
#         return np.exp(x)

#     def backward(self, gy):
#         x = self.input.data
#         gx = np.exp(x) * gy
#         return gx


def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)


def add(x0, x1):
    return Add()(x0, x1)


def sqaure(x):
    return Sqaure()(x)


# def exp(x):
#     return Exp()(x)


def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x


x = Variable(np.array(2))
y = Variable(np.array(3))
z = add(sqaure(x), sqaure(y))
z.backward()
print(z.data)
print(x.grad)
print(y.grad)
