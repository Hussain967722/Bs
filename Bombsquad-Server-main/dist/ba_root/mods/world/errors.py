"""MIT License

Copyright (c) 2021 LIRIK SPENCER

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

"""EXCEPTION CLASSES FOR OVERALL MODS"""


class FewArgumentsError(Exception):
    """Raised when we don't meet the minimum arguments required"""


class DataTypeError(RuntimeError):
    """Raised when we don't provide the required data type"""


class ManyArgumentsError(Exception):
    """Raised when we provide more arguments then required"""


class NonImplementedError(Exception):
    """Raises when we perform some non implemented methods"""


class MustBeIntegerError(ValueError):
    """Raised when the argument provided is a letter rather than integer"""

    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

    def __str__(self):
        return f"`{self.arg}` must be an integer"


class RoleNameError(KeyError):
    """Raised when the provided is not found in roles json file"""


class ConfigClassError(RuntimeError):
    """Base Exception for Config"""


class ArgumentDoesntMatchError(AttributeError):
    """
    ```Raised when the argument provided doesn't match with the required one```
    For an example we have a shop command where we use /shop (effects/items) and
    if we provide anything else rather than (effects/items), this will be raised.
    """

    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

    def __str__(self):
        return f"`{self.arg}` doesn't match to any argument"
