# necessary imports
import finder

# define base cases
to_find = ['mouse', 'mice']
to_verify = [True, False]


# this test is for appearances of the found word as a proper substring, rather than a constituent substring
# (PASS)
def test_finder_1() -> None:
    output = finder.finder('mousecat mice catmice mouse mousemouse', to_find[0], to_find[1])
    assert output == [[22]]


# this test is for appearances of the found word as a substring in any form
# (FAIL)
def test_finder_2() -> None:
    output = finder.finder('mousecat mice catmice mouse mousemouse', to_find[1], to_verify[1])
    assert output == [[9, 17]]
