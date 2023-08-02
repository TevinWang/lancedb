
#  Copyright 2023 LanceDB Developers
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
    See the License for the specific language governing permissions and
    limitations under the License.

"""
LANCE Database Main Module

This module exports the main interface for connecting to a LanceDB and
interacting with tables.

The key functions are:

- connect() - Connect to a LanceDB at the given uri
- LanceDBConnection - Manages tables in the database  
- LanceTable - Represents a table in the database

The connect() function returns a LanceDBConnection which manages
access to the underlying database. This includes methods to list,
create, and delete tables.

LanceTable represents an individual table. This contains methods to 
query, modify, and retrieve the contents of the table. Methods allow
converting between Arrow, Pandas, and the native LanceDataset format.

See tutorials at https://lancedb.io for more usage details.
"""

from .db import URI, LanceDBConnection

def connect(uri: URI) -> LanceDBConnection:
    """Connect to a LanceDB instance at the given URI

    """Connect to a LanceDB instance at the given URI

    Parameters
    ----------
    uri: str or Path
        The uri of the database.

    Examples
    --------

    For a local directory, provide a path for the database:

    >>> import lancedb
    >>> db = lancedb.connect("~/.lancedb")

    For object storage, use a URI prefix:

    >>> db = lancedb.connect("s3://my-bucket/lancedb")

    Returns
    -------
    conn : LanceDBConnection
        A connection to a LanceDB database.
    """
    return LanceDBConnection(uri)

