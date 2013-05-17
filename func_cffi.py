from cffi import FFI
ffi = FFI()
ffi.cdef("""
    typedef struct _A
    {
        int age;
        double income;
    }A;

    typedef struct _B
    {
        int total_age;
        double total_income;
    }B;

    B func(A *a, int len);
""")

# lib = ffi.verify('./t.h')
lib = ffi.dlopen('./t.so')


def func(args):
    fmt = "A[%d]" % len(args)
    arg = ffi.new(fmt)
    for i in range(len(args)):
        arg[i].age = i
        arg[i].income = i
    b = lib.func(arg, len(args))
    return (b.total_age, b.total_income)


def test_func():
    import sys
    c = int(sys.argv[1])
    for i in xrange(c):
        args = [(i, i) for i in range(1)]
        func(args)


if __name__ == '__main__':
    test_func()
