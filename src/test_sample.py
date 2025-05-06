# This is a sample test file
# this code base mostly stitch API calls together
# and does not have much logic
# so we don't have much to test
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
