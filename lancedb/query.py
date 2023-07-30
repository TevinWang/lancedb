
# Minor style improvements

from __future__ import annotations
from typing import Literal

import numpy as np
import pandas as pd
import pyarrow as pa

from .common import VECTOR_COLUMN_NAME


class LanceQueryBuilder:

    # Use underscore for private attributes
    def __init__(self, table: "lancedb.table.LanceTable", query: np.ndarray):
        self._metric = "L2"
        ...

    # Rest of class
    
class LanceFtsQueryBuilder(LanceQueryBuilder):
  
  # Rest of class
  
