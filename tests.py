# necessary imports
import finder

# define base cases
# 'mouse' is a proper substring, mice is a constituent substring
to_find = ['mouse', 'mice']
to_verify = [True, False]


# this test is for appearances of the found word as a proper substring, rather than a constituent substring
# (PASS)
def test_finder_1() -> None:
    # we expect to find 'mouse' as a proper substring that starts at index 22
    output = finder.finder('mousecat mice catmice mouse mousemouse', to_find[0], to_find[1])
    assert output == [[22]]


# this test is for appearances of the found word as a substring in any form
# (FAIL)
def test_finder_2() -> None:
    # we expect to find 'mice' as a constituent substring, two of which start at indices 9 and 17
    output = finder.finder('mousecat mice catmice mouse mousemouse', to_find[1], to_verify[1])
    assert output == [[9, 17]]
