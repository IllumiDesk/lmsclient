import pytest

@pytest.fixture(scope='function')
def setup_image_environ(monkeypatch):
    """
    Set the enviroment variables used to identify the end user image.
    """
    monkeypatch.setenv('API_URL', 'http://my.lms.com')
    monkeypatch.setenv('API_KEY', 'abc123')
    monkeypatch.setenv('COURSE_ID', '123')
