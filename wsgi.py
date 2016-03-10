#!/usr/bin/env python
import os
import sys
from app import create_app 

app = create_app(os.getenv('PUSH7_API_CONFIG') or 'default')

