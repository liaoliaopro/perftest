cdef extern from "t.h":
    ctypedef struct A:
        pass
    ctypedef struct B:
        pass
    
    B _func(A *a, int len)

