from cffi import FFI
ffi = FFI()
ffi.cdef("""
    typedef struct _A
    {
        char name[50];
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

#lib = ffi.verify('./t.h')
lib = ffi.dlopen('./t.so')
# args = [ffi.new("A*", ['bidong', 5, 100.0]) for i in range(100)]
args = ffi.new("A[100]")
for i in range(100):
    args[i].age = i
    args[i].income = i

b = lib.func(args, len(args))
print b.total_age, b.total_income


def func_cffi():
    pass


def func_ctypes():
    pass


def func_cython():
    pass
