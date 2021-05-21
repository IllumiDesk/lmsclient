from itertools import chain
from itertools import starmap
from typing import Any
from typing import Dict


def flatten_dict(dictionary: Dict[str, Any]) -> dict:
    """Flatten a nested dictionary structure. All keys are assumed to be strings and values
    are of any type.

    Ref: https://stackoverflow.com/questions/56843948/how-to-flatten-deep-dictionary-surrounding-any-child-dictionary-keys-with-squar
    """

    def unpack(parent_key: str, parent_value: Any) -> dict:
        """Unpack one level of nesting in a dictionary

        Args:
            parent_key (str): the dictionary's parent key
            parent_value (Any): the dictionary's parent value

        Returns:
            dict: the dictionary

        Yields:
            Iterator[dict]: an iterable dictionary
        """
        try:
            items = parent_value.items()
        except AttributeError:
            # parent_value was not a dict, no need to flatten
            yield (parent_key, parent_value)
        else:
            for key, value in items:
                if type(value) == list:
                    for k, v in enumerate(value):
                        yield (parent_key + "[" + key + "]" + "[" + str(k) + "]", v)
                else:
                    yield (parent_key + "[" + key + "]", value)

    while True:
        # Keep unpacking the dictionary until all value's are not dictionary's
        dictionary = dict(chain.from_iterable(starmap(unpack, dictionary.items())))
        if not any(isinstance(value, dict) for value in dictionary.values()):
            break
    return dictionary
