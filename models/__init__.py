#!/usr/bin/python3
"""
This module initializes the storage engine based 
on the environment variable HBNB_TYPE_STORAGE.
"""

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Check the environment variable HBNB_TYPE_STORAGE
storage_type = os.getenv("HBNB_TYPE_STORAGE")

# Initialize storage based on the type
if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage
storage.reload()
