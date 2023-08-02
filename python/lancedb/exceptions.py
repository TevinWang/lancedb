"""Custom exception handling"""

"""
Custom Exceptions

Defines custom exceptions used in LanceDB:
  
- MissingValueError - Required value not provided 
- MissingColumnError - Column name not found

Using custom exception types makes it easier to handle errors 
from LanceDB separately from general ValueErrors and KeyErrors.

"""


class MissingValueError(ValueError):
    """Exception raised when a required value is missing."""
    """Exception raised when a required value is missing."""

    pass


class MissingColumnError(KeyError):
    """
    Exception raised when a column name specified is not in
    the  DataFrame object
    """

    def __init__(self, column_name):
        self.column_name = column_name

    def __str__(self):
        return (
            f"Error: Column '{self.column_name}' does not exist in the DataFrame object"
        )

