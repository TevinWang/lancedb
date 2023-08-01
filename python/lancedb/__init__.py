
#  Copyright 2023 LanceDB Developers
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import logging

from .db import URI, LanceDBConnection


def connect(uri: URI) -> LanceDBConnection:
    """Connect to a LanceDB instance at the given URI

    Parameters
    ----------
    uri: str or Path
      http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    # Add logging to help with debugging
    logger = logging.getLogger(__name__)
    logger.info("Connecting to LanceDB at %s", uri)

    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    >>> db = lancedb.connect("~/.lancedb")

    For object storage, use a URI prefix:

    >>> db = lancedb.connect("s3://my-bucket/lancedb")

    Returns
    -------
    conn : LanceDBConnection
        A connection to a LanceDB database.
    """
    return LanceDBConnection(uri)

