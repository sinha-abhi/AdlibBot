#!/usr/bin/python3
import praw, prawcore
import configparser
from helpers import ExtractorHelper

# Extracts information from Reddit
class Extractor(object):
    def __init__(self, **config):
        cfg = configparser.ConfigParser()
        helper = ExtractorHelper()
        
        BOT_CFG = "../res/bot.ini"
        if not cfg.read(BOT_CFG):
            print("Configuration file", BOT_CFG, "not found.")
            raise FileNotFoundError(BOT_CFG)

        self.config = {}
        _keys = ["subfile", "logfile", "client_id", "client_secret",
                 "user_agent", "username", "password"]
        for key in _keys:
            self.config[key] = helper.read_cfg_opt(cfg, "login_cfg", key)    
       
        #print(self.config)
        self.reddit = praw.Reddit(client_id = self.config["client_id"],
                          client_secret = self.config["client_secret"],
                          user_agent = self.config["user_agent"],
                          username = self.config["username"],
                          password = self.config["password"])
        try:
            self.reddit.user.me()
        except prawcore.exceptions.OAuthException:
            print("Unsuccessful login")
            exit()


if __name__ == "__main__":
    e = Extractor()
