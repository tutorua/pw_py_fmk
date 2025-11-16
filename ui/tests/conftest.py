import pytest

@pytest.fixture(scope='session')
def loadPreconditions():
    print("Setup session preconditions")