
# Use type annotations
from typing import Callable, Union  

import numpy as np
import pandas as pd
import pyarrow as pa
from lance.vector import vec_to_table
from retry import retry


def with_embeddings(
    func: Callable,  
    data: Union[pa.Table, pd.DataFrame],
    column: str = "text",
    wrap_api: bool = True,
    show_progress: bool = False,
    batch_size: int = 1000,
) -> pa.Table:
    
    # Rest of function
    
# Use context manager for EmbeddingFunction
class EmbeddingFunction:

    def __init__(self, func: Callable):
        self.func = func
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        ...  

# Rest of class
