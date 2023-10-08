"""
The purpose of this class is to test the fucntionality of the doc creation.
"""


class MyRandomClass:
    """
    This is a random class to test the doc.
    """

    def __init__(self, value: int) -> None:
        self.value = value

    def test_function(self) -> int:
        """
        A test function that returns the value of the example class.

        :returns value: the initial value the instance got from beginning.
        """
        return self.value
