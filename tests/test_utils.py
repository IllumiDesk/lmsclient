from lmsclient.utils import flatten_dict


def test_flatten_dict(unflattened_dict, flattened_dict):
    """Ensure that an unflattened dictionary is correctly flattened."""
    local_flattened = flatten_dict(unflattened_dict)
    assert local_flattened == flattened_dict
