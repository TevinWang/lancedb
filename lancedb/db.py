
# Minor comment improvements

from __future__ import annotations

import os
from pathlib import Path
import os

import pyarrow as pa
from pyarrow import fs

from .common import DATA, URI
from .table import LanceTable  
from .util import get_uri_scheme, get_uri_location


class LanceDBConnection:
    """
    A connection to a LanceDB database.

    Parameters
    ----------
    uri: str or Path
        The root uri of the database.

    Examples
    --------
    >>> import lancedb
    >>> db = lancedb.connect("./.lancedb")
    >>> db.create_table("my_table", data=[{"vector": [1.1, 1.2], "b": 2}, 
    ...                                   {"vector": [0.5, 1.3], "b": 4}])
    LanceTable(my_table)
    >>> db.create_table("another_table", data=[{"vector": [0.4, 0.4], "b": 6}]) 
    LanceTable(another_table)
    >>> db.table_names()
    ['another_table', 'my_table']
    >>> len(db)  
    2
    >>> db["my_table"]
    LanceTable(my_table) 
    >>> "my_table" in db
    True
    >>> db.drop_table("my_table")
    >>> db.drop_table("another_table")
    """

    def __init__(self, uri: URI):
        # Check if URI is local
        is_local = isinstance(uri, Path) or get_uri_scheme(uri) == "file"  
        if is_local:
            if isinstance(uri, str):
                uri = Path(uri)
            uri = uri.expanduser().absolute()
            Path(uri).mkdir(parents=True, exist_ok=True)  
        self._uri = str(uri)

    # Rest of class
