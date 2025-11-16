# These tests are suppoed to check the components of the Home page: header, footer, etc.
import pytest

@pytest.fixture(scope='module')
def loadPreconditions():
    print("Setup module preconditions")


def test_topBar(loadPreconditions):
    print("This is the first tet")


def test_footer(loadPreconditions):
    print('This is the second test')
