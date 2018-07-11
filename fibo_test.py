import fibo


def test_fibo_10():
    result_10 = fibo.fib2(10)
    expected_result = [0, 1, 1, 2, 3, 5, 8]
    assert result_10 == expected_result

def test_fibo_0():
    result_0 = fibo.fib2(0)
    expected_result = []
    assert result_0 == expected_result
    
def test_fibo_minus():
    result = fibo.fib2(-1)
    expected_result = []
    assert result == expected_result
