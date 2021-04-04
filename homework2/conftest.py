from calculator import Calculator
import pytest


@pytest.fixture(scope="class")
def calculateadd():
    print("开始相加计算")
    caladd = Calculator()
    yield caladd
    print("结束相加计算")


@pytest.fixture(scope="class")
def calculatesub():
    print("开始相减计算")
    calsub = Calculator()
    yield calsub
    print("结束相减计算")


@pytest.fixture(scope="class")
def calculatemul():
    print("开始相乘计算")
    calmul = Calculator()
    yield calmul
    print("结束相乘计算")


@pytest.fixture(scope="class")
def calculatediv():
    print("开始相除计算")
    caldiv = Calculator()
    yield caldiv
    print("结束相除计算")
