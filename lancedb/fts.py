
# Add type annotations

from typing import List, Tuple  

import pyarrow as pa

try:
    import tantivy
except ImportError:
    raise ImportError(...)
    
from .table import LanceTable


def create_index(index_path: str, text_fields: List[str]) -> tantivy.Index:
   ...
   
def populate_index(index: tantivy.Index, table: LanceTable, fields: List[str]) -> int:
   ...
   
def search_index(
    index: tantivy.Index, query: str, limit: int = 10    
) -> Tuple[Tuple[int], Tuple[float]]:
   ...

