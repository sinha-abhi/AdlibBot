#!/usr/bin/python3
import praw
import configparser

# Extracts information from Reddit
class Extractor(object):

    def __init__(self, **config):
        cfg = configparser.ConfigParser()
        
        BOT_CFG = "../res/bot.ini"
        # require config file
        if not cfg.read(BOT_CFG):
            print("Configuration file for bot not found.")
            raise FileNotFoundError(BOT_CFG)




        self.reddit = praw.Reddit(client_id = "jlxtwwfRpUiYmw",
                client_secret = "wwmXY-wJntO6VfpNzVVXQTKv2nw",
                user_agent = "test connection of bot",
                username = USERNAME,
                password = "Preparation123")


