"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""

class Error(Exception):
    """Base validation exception."""

    ...

class SchemaError(Error):
    """An error was encountered in the schema."""

    ...

class Invalid(Error):
    """The data was invalid.

    :attr msg: The error message.
    :attr path: The path to the error, as a list of keys in the source data.
    :attr error_message: The actual error message that was raised, as a
        string.

    """

    def __init__(
        self, message, path=..., error_message=..., error_type=...
    ) -> None: ...
    @property
    def msg(self): ...
    def __str__(self) -> str: ...
    def prepend(self, path): ...

class MultipleInvalid(Invalid):
    def __init__(self, errors=...) -> None: ...
    def __repr__(self): ...
    @property
    def msg(self): ...
    @property
    def path(self): ...
    @property
    def error_message(self): ...
    def add(self, error): ...
    def __str__(self) -> str: ...
    def prepend(self, path): ...

class RequiredFieldInvalid(Invalid):
    """Required field was missing."""

    ...

class ObjectInvalid(Invalid):
    """The value we found was not an object."""

    ...

class DictInvalid(Invalid):
    """The value found was not a dict."""

    ...

class ExclusiveInvalid(Invalid):
    """More than one value found in exclusion group."""

    ...

class InclusiveInvalid(Invalid):
    """Not all values found in inclusion group."""

    ...

class SequenceTypeInvalid(Invalid):
    """The type found is not a sequence type."""

    ...

class TypeInvalid(Invalid):
    """The value was not of required type."""

    ...

class ValueInvalid(Invalid):
    """The value was found invalid by evaluation function."""

    ...

class ContainsInvalid(Invalid):
    """List does not contain item"""

    ...

class ScalarInvalid(Invalid):
    """Scalars did not match."""

    ...

class CoerceInvalid(Invalid):
    """Impossible to coerce value to type."""

    ...

class AnyInvalid(Invalid):
    """The value did not pass any validator."""

    ...

class AllInvalid(Invalid):
    """The value did not pass all validators."""

    ...

class MatchInvalid(Invalid):
    """The value does not match the given regular expression."""

    ...

class RangeInvalid(Invalid):
    """The value is not in given range."""

    ...

class TrueInvalid(Invalid):
    """The value is not True."""

    ...

class FalseInvalid(Invalid):
    """The value is not False."""

    ...

class BooleanInvalid(Invalid):
    """The value is not a boolean."""

    ...

class UrlInvalid(Invalid):
    """The value is not a URL."""

    ...

class EmailInvalid(Invalid):
    """The value is not an email address."""

    ...

class FileInvalid(Invalid):
    """The value is not a file."""

    ...

class DirInvalid(Invalid):
    """The value is not a directory."""

    ...

class PathInvalid(Invalid):
    """The value is not a path."""

    ...

class LiteralInvalid(Invalid):
    """The literal values do not match."""

    ...

class LengthInvalid(Invalid): ...

class DatetimeInvalid(Invalid):
    """The value is not a formatted datetime string."""

    ...

class DateInvalid(Invalid):
    """The value is not a formatted date string."""

    ...

class InInvalid(Invalid): ...
class NotInInvalid(Invalid): ...
class ExactSequenceInvalid(Invalid): ...

class NotEnoughValid(Invalid):
    """The value did not pass enough validations."""

    ...

class TooManyValid(Invalid):
    """The value passed more than expected validations."""

    ...
