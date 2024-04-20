#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7012342197:AAFTFGxXV7vN0oVdopz3s9xM_GluDWltKEo")
    API_ID = int(os.environ.get("API_ID", "27803618"))
    API_HASH = os.environ.get("API_HASH", "2cdaef9643189f6bd9c7b31a70257356")
    AUTH_USERS = os.environ.get("AUTH_USERS", "745084259")
