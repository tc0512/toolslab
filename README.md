# toolslab

python程序员的工具箱

## 安装
```bash
pip install git+https://ghproxy.net/https://github.com/tc0512/toolslab.git #目前未发布
```

## 快速开始
```python
from toolslab import StringAlgo as sa
from toolslab import LexicalCast as lc
print(sa.trim("  hello  ")) #hello
print(lc.lexical_cast_int("666")) #666
```

## 模块介绍
### 字符串处理模块`toolslab.StringAlgo`
- `to_upper` `to_lower` 大小写转换
- `trim` `trim_left` `trim_right` 修剪字符串
- `find_first` `find_last` `find_nth` 查找功能
- `replace_all` `replace_first` `replace_last` 替换功能
- `starts_with` `ends_with` 谓词功能
### 简单类型转换`toolslab.LexicalCast`
- 整数，双精度浮点数
- 字符串，布尔值

## 示例代码
```python
from toolslab import StringAlgo as sa
from toolslab import LexicalCast as lc
print(sa.is_num("30")) #True
print(sa.icequals("hello", "HELLO")) #True
print(lc.lexical_cast_bool("YES")) #True
```

## 许可证
MIT
