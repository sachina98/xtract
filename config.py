#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7401337970:AAGpJD4CdY59wU-KWBgc6Ogp6hLjBueJxIU")
    API_ID = int(os.environ.get("API_ID", "29768900"))
    API_HASH = os.environ.get("API_HASH", "6a56e5c2383dc7b85210febe60b9f229")
    AUTH_USERS = "5986670447"

