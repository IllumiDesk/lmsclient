import pytest


@pytest.fixture(scope="function")
def setup_image_environ(monkeypatch):
    """
    Set the enviroment variables used to identify the end user image.
    """
    monkeypatch.setenv("API_URL", "http://my.lms.com")
    monkeypatch.setenv("API_KEY", "abc123")
    monkeypatch.setenv("COURSE_ID", "123")


@pytest.fixture(scope="function")
def unflattened_dict() -> dict:
    """
    An example unflattened dictionary.
    """
    input_dict = {
        "first": {"a": 24, "b": {"green": {"look": 3, "out": "Nope"}, "apple": True}},
        "third": {"x": {"word": 8}, "y": -1, "z": 26},
        "fifth": {"ae": [0, None, 2.0, 3.0], "e": None},
    }
    return input_dict


@pytest.fixture(scope="function")
def flattened_dict() -> dict:
    """
    An example flattened dictionary.
    """
    local_flattened = {
        "first[a]": 24,
        "first[b][green][look]": 3,
        "first[b][green][out]": "Nope",
        "first[b][apple]": True,
        "third[x][word]": 8,
        "third[y]": -1,
        "third[z]": 26,
        "fifth[ae][0]": 0,
        "fifth[ae][1]": None,
        "fifth[ae][2]": 2.0,
        "fifth[ae][3]": 3.0,
        "fifth[e]": None,
    }
    return local_flattened


@pytest.fixture(scope="function")
def make_course_api_response():
    """Returns a course as json to mimic the API's response."""

    def _make_course():
        local_course = {}
        return local_course

    return _make_course
