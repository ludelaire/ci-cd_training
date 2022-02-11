from cicd.main import suma


def test_positive_negative_result_zero():
    a = 9
    b = -9
    c = suma(a, b)

    assert c == 0
