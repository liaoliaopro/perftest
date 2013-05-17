from ctypes import *


class A(Structure):
    _fields_ = [('age', c_int),
                ('income', c_double)]


class B(Structure):
    _fields_ = [('total_age', c_int),
                ('total_income', c_double)]

dll = CDLL('./t.so')
dll.func.argtypes = [POINTER(A), c_int]
dll.func.restype = B


def func(args):
    buf = (A * len(args))()
    buf_p = pointer(buf)
    a_p = cast(buf_p, POINTER(A))

    for i, a in enumerate(args):
        buf[i].age = a[0]
        buf[i].income = a[1]
    b = dll.func(a_p, len(args))
    return (b.total_age, b.total_income)


def test_func():
    import sys
    c = int(sys.argv[1])
    for i in xrange(c):
        args = [(i, i) for i in range(1)]
        func(args)


if __name__ == '__main__':
    test_func()
