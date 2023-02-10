#!/usr/bin/python3
"""
    init file for models module
"""

import models.base_model
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()