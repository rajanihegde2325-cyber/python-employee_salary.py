import pytest
from salary import calculate_gross_salary


def test_gross_salary():
    assert calculate_gross_salary(50000) == 65000


def test_hra_and_da():
    basic_salary = 50000
    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    assert hra == 10000
    assert da == 5000


def test_zero_salary():
    assert calculate_gross_salary(0) == 0


def test_different_salary():
    assert calculate_gross_salary(30000) == 39000