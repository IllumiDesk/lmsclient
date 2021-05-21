import attr


class Base:
    """Base class that all classes should inherit from."""

    def jsonify(self) -> dict:
        """Represents the object's attributes as a dict.

        Returns:
            dict: a collection of k/v pairs
        """
        return attr.asdict(self)
