#toolslab/LexicalCast.pyx
#cython: language_level=3
from cython cimport floating
cpdef int lexical_cast_int(str string): #字符串转整数
    return int(string)
cpdef double lexical_cast_double(str string): #字符串转双精度浮点数
    return float(string)
cpdef str lexical_cast(floating num): #数字转字符串
    return str(num)
