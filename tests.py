# necessary imports
import finder

# define base cases
to_find = ['mouse', 'mice']
to_verify = [True, False]

# this test is for appearances of the found word as a proper substring, rather than a constituent substring
# (PASS)
def test_finder_1() -> None:
    output = finder.finder('mousecat mice catmice mouse mousemouse', ['mouse'], [True])
    assert output == [[22]]

# this test is for appearances of the found word as a substring in any form
# (FAIL)
def test_finder_2() -> None:
    output = finder.finder('mousecat mice catmice mouse mousemouse', ['mice'], [False])
    assert output == [[9, 17]]