from setuptools import setup
from Cython.Build import cythonize

setup(
    name="toolslab",
    version="0.1.0",
    description="python程序员的工具箱",
    author="tc0512",
    author_email="tancheng_0812@qq.com",
    license="MIT",
    packages=["toolslab"],
    ext_modules=cythonize("toolslab/*.pyx"),
    install_requires=[],
    python_requires=">=3.8",
)
