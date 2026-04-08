#/root/toolslab/toolslab/StringAlgo.pyx
#cython: language_level=3
cpdef str to_upper(str string): #小写转大写
    return string.upper()
cpdef str to_lower(str string): #大写转小写
    return string.lower()
cpdef str trim(str string): #去掉首尾空格
    return string.strip()
cpdef str trim_left(str string): #去掉左侧空格
    return string.lstrip()
cpdef str trim_right(str string): #去掉右侧空格
    return string.rstrip()
cpdef str trim_copy(str string): #副本
    return string.strip()
cpdef tuple find_first(str s, str sub): #首次出现
    cdef int start = s.find(sub)
    if start==-1:
        return (-1, -1)
    cdef int end = start+len(sub)
    return (start, end) #区间=[start, end)
cpdef tuple find_last(str s, str sub): #最后一次出现
    cdef int start = s.rfind(sub)
    if start==-1:
        return (-1, -1)
    cdef int end = start+len(sub)
    return (start, end) #区间=[start, end)
cpdef tuple find_nth(str s, str sub, int n): #第n+1次出现
    cdef int start = 0
    cdef int pos
    cdef int count = 0
    while True:
        pos = s.find(sub, start)
        if pos == -1:
            return (-1, -1)
        if count == n:
            return (pos, pos + len(sub)) #区间=[start, end)
        count += 1
        start = pos + 1
cpdef str replace_all(str s, str old, str new): #替换所有
    return s.replace(old, new)
cpdef str replace_first(str s, str old, str new): #替换第一个目标字符串
    cdef int pos = s.find(old)
    if pos == -1:
        return s
    return s[:pos] + new + s[pos + len(old):]
cpdef str replace_last(str s, str old, str new): #替换最后一个目标字符串
    cdef int pos = s.rfind(old)
    if pos == -1:
        return s
    return s[:pos] + new + s[pos + len(old):]
cpdef str erase_all(str s, str sub): #删除所有目标字符串
    return s.replace(sub, '')
cpdef str starts_with(str s, str prefix): #是否以...开头
    length = len(prefix)
    sub = s[:length]
    return sub==prefix
cpdef str ends_with(str s, str suffix): #是否以...结尾
    length = len(suffix)
    sub = s[-length:]
    return sub==suffix
