import allure
import pytest
import yaml


# 从yaml文件中获取测试数据
def get_datas():
    with open(r"D:\Users\PycharmProjects\Test\lagou\datas\calc.yml") as f:
        datas = yaml.safe_load(f)
    return datas


# 定义一个相加类
@allure.feature("相加运算")
class TestCaladd:
    # 编写测试用例：整数相加
    @allure.title("整数相加")
    @pytest.mark.parametrize('a, b, expect', get_datas()['add']['int'])
    def test_add_int(self, calculateadd, a, b, expect):
        assert expect == calculateadd.add(a, b)

    # 编写测试用例：小数相加
    @allure.title("小数相加")
    @pytest.mark.parametrize('a, b, expect', get_datas()['add']['float'])
    def test_add_float(self, calculateadd, a, b, expect):
        assert expect == round(calculateadd.add(a, b), 2)

    # 编写测试用例： 整数和小数相加
    @allure.title("整数和小数相加")
    @pytest.mark.parametrize('a, b, expect', get_datas()['add']['infloat'])
    def test_add_infloat(self, calculateadd, a, b, expect):
        assert expect == round(calculateadd.add(a, b), 2)

    # 编写测试用例：负整数相加
    @allure.title("负整数相加")
    @pytest.mark.parametrize('a, b, expect', get_datas()['add']['fint'])
    def test_add_fint(self, calculateadd, a, b, expect):
        assert expect == calculateadd.add(a, b)

    # 编写测试用例：负小数相加
    @allure.title("负小数相加")
    @pytest.mark.parametrize('a, b, expect', get_datas()['add']['ffloat'])
    def test_add_ffloat(self, calculateadd, a, b, expect):
        assert expect == round(calculateadd.add(a, b), 2)

    # 编写测试用例：整数和零相加
    @allure.title("整数和0相加")
    @pytest.mark.parametrize('a, b, expect', get_datas()['add']['zint'])
    def test_add_zint(self, calculateadd, a, b, expect):
        assert expect == calculateadd.add(a, b)

    # 编写测试用例：小数和零相加
    @allure.title("小数和0相加")
    @pytest.mark.parametrize('a, b, expect', get_datas()['add']['zfloat'])
    def test_add_zfloat(self, calculateadd, a, b, expect):
        assert expect == round(calculateadd.add(a, b), 2)

    # 编写测试用例：负整数和零相加
    @allure.title("负整数和0相加")
    @pytest.mark.parametrize('a, b, expect', get_datas()['add']['fzint'])
    def test_add_fzint(self, calculateadd, a, b, expect):
        assert expect == calculateadd.add(a, b)

    # 编写测试用例：负小数和零相加
    @allure.title("负小数和0相加")
    @pytest.mark.parametrize('a, b, expect', get_datas()['add']['fzfloat'])
    def test_add_fzfloat(self, calculateadd, a, b, expect):
        assert expect == round(calculateadd.add(a, b), 2)


# 定义一个相减类
@allure.feature("相减运算")
class TestCalsub:
    # 整数相减
    @allure.title("整数相减")
    @pytest.mark.parametrize('a, b, expect', get_datas()['sub']['int'])
    def test_sub_int(self, calculatesub, a, b, expect):
        assert expect == calculatesub.sub(a, b)

    # 小数相减
    @allure.title("小数相减")
    @pytest.mark.parametrize('a, b, expect', get_datas()['sub']['float'])
    def test_sub_float(self, calculatesub, a, b, expect):
        assert expect == round(calculatesub.sub(a, b), 2)

    # 负数相减
    @allure.title("负数相减")
    @pytest.mark.parametrize('a, b, expect', get_datas()['sub']['fint'])
    def test_sub_fint(self, calculatesub, a, b, expect):
        assert expect == calculatesub.sub(a, b)


# 定义一个相乘类
@allure.feature("相乘运算")
class TestCalmul:
    # 整数相乘
    @allure.title("整数相乘")
    @pytest.mark.parametrize('a, b, expect', get_datas()['mul']['int'])
    def test_mul_int(self, calculatemul, a, b, expect):
        assert expect == calculatemul.mul(a, b)

    # 小数相乘
    @allure.title("小数相乘")
    @pytest.mark.parametrize('a, b, expect', get_datas()['mul']['float'])
    def test_mul_float(self, calculatemul, a, b, expect):
        assert expect == round(calculatemul.mul(a, b), 2)

    # 乘数有0时
    @allure.title("乘数含0")
    @pytest.mark.parametrize('a, b, expect', get_datas()['mul']['zero'])
    def test_mul_zero(self, calculatemul, a, b, expect):
        assert expect == calculatemul.mul(a, b)

    # 正负相乘
    @allure.title("正负相乘")
    @pytest.mark.parametrize('a, b, expect', get_datas()['mul']['fint'])
    def test_mul_fint(self, calculatemul, a, b, expect):
        assert expect == calculatemul.mul(a, b)

    # 负负相乘
    @allure.title("负负相乘")
    @pytest.mark.parametrize('a, b, expect', get_datas()['mul']['ff'])
    def test_mul_ff(self, calculatemul, a, b, expect):
        assert expect == calculatemul.mul(a, b)


# 定义一个相除类
@allure.feature("相除运算")
class TestCaldiv:
    # 整数相除
    @allure.title("整数相除")
    @pytest.mark.parametrize('a, b, expect', get_datas()['div']['int'])
    def test_div_int(self, calculatediv, a, b, expect):
        assert expect == calculatediv.div(a, b)
    # 小数相除
    @allure.title("小数相除")
    @pytest.mark.parametrize('a, b, expect', get_datas()['div']['float'])
    def test_div_float(self, calculatediv, a, b, expect):
        assert expect == round(calculatediv.div(a, b), 2)
    # 负数相除
    @allure.title("负数相除")
    @pytest.mark.parametrize('a, b, expect', get_datas()['div']['ff'])
    def test_div_ff(self, calculatediv, a, b, expect):
        assert expect == calculatediv.div(a, b)
    # 被除数为0
    @allure.title("被除数为0")
    @pytest.mark.parametrize('a, b, expect', get_datas()['div']['zero'])
    def test_div_zero(self, calculatediv, a, b, expect):
        assert expect == calculatediv.div(a, b)
    # 除数为0
    @allure.title("除数为0")
    @pytest.mark.parametrize('a, b, expect', get_datas()['div']['zero1'])
    def test_div_zero1(self, calculatediv, a, b, expect):
        with pytest.raises(ZeroDivisionError):
            calculatediv.div(a, b)