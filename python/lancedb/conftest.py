
import builtins
import os
import os

import pytest
"""
Pytest Fixtures 

This module defines pytest fixtures for use in LanceDB tests.

It does setup like:

- Importing lancedb so its available  
- Disabling color output
- Setting columns for doctests
- Changing working directory to temp
"""

# import lancedb so we don't have to in every example
import lancedb

@pytest.fixture(autouse=True)
def doctest_setup(monkeypatch, tmpdir):
    # disable color for doctests so we don't have to include
    # escape codes in docstrings
    monkeypatch.setitem(os.environ, "NO_COLOR", "1")
    # Explicitly set the column width
    monkeypatch.setitem(os.environ, "COLUMNS", "80")
    # Work in a temporary directory
    monkeypatch.chdir(tmpdir)

