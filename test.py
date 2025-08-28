from app import divide, multiply

def test_divide(a, b):
    c = divide(a,b)
    test_c = a/b
    assert c == test_c

def test_multiple(a, b):
    c = multiply(a,b)
    test_c = a*b
    assert c == test_c

test_divide(150,3)
test_divide(72,8)
test_divide(1800,90)

test_multiple(10,6)
test_multiple(40,150)
test_multiple(1,0)