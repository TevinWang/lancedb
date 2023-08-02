
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
Common Types and Constants

This internal module defines common types and constants used across 
LanceDB. Key contents:

- URI - The uri type
- DATA - Supported data types 
- VEC - Vector types
- VECTOR_COLUMN_NAME - Name of vector column

Keeping these in a shared location avoids duplication and ensures
consistency across components. The types also help annotate
method signatures.
"""

from pathlib import Path
from typing import List, Union


import numpy as np
import pandas as pd
import pyarrow as pa

VEC = Union[list, np.ndarray, pa.Array, pa.ChunkedArray]
URI = Union[str, Path]

# TODO support generator
DATA = Union[List[dict], dict, pd.DataFrame]
VECTOR_COLUMN_NAME = "vector"

