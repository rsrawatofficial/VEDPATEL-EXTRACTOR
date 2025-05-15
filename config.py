#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from pymongo import MongoClient

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7609528498:AAGqcl_h-Cygc4v_oiXqD4cbp-yGypVcakY")
    API_ID = int(os.environ["API_ID", "27900743"]
    API_HASH = os.environ["API_HASH", "ebb06ea8d41420e60b29140dcee902fc"]
    AUTH_USERS = "7804396225"
    MONGO_URI = os.environ.get("MONGO_DB_URI", "your_mongo_db_uri")
    
