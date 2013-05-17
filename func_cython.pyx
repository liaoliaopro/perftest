#from func_cython cimport A, B, _func
cimport func_cython
from libc.stdlib cimport malloc, free

def func(args):
    cdef func_cython.A* arg = <func_cython.A*>malloc(sizeof(func_cython.A)*len(args))
    for i in range(len(args)):
        arg[i].age = i
        arg[i].income = i
    #func_cython._func(<func_cython.A*>arg, len(args))
    cdef func_cython.B b = func_cython._func(<func_cython.A*>arg, len(args))
    free(arg)
    #return (b.total_age, b.total_income)
