#toolslab/LexicalCast.pyx
#cython: language_level=3
from cython cimport floating
cpdef int lexical_cast_int(str string): #字符串转整数
    return int(string)
cpdef double lexical_cast_double(str string): #字符串转双精度浮点数
    return float(string)
def lexical_cast_string(num): #数字转字符串
    if isinstance(num, (int, float)):
        return str(num)
    raise TypeError("Expected int or float")
cpdef bool lexical_cast_bool(str string): #字符串转布尔值
    s = string.lower()
    if s in ["true", "yes", "1", "on"]:
        return True
    elif s in ["false", "no", "0", "off"]:
        return False
    raise ValueError("cannot convert this string to bool")
