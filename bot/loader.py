#!/usr/bin/python3
import praw, prawcore
import configparser
import os

# Load information from config files
class ConfigLoader(object):

    def __init__(self, loc=None):
        self.__cfg = configparser.ConfigParser()
        
        CFG_PATH = self.__get_cfg_path(loc)
        if not self.__cfg.read(CFG_PATH):
            print("Configuration file", CFG_PATH, "not found.")
            raise FileNotFoundError(CFG_PATH)

        self.__keys = ["subfile", "logfile", "client_id", "client_secret",
                 "user_agent", "username", "password"]

    def load_config(self):
        self.config = {}
        for key in self.__keys:
            self.config[key] = self.__read_cfg_opt(self.__cfg, "login_cfg", key)    
     
    def spawn_reddit_inst(self, verify=None):
        self.reddit = praw.Reddit(client_id = self.config["client_id"],
                              client_secret = self.config["client_secret"],
                              user_agent = self.config["user_agent"],
                              username = self.config["username"],
                              password = self.config["password"])
        if verify is not None:
            return self.__verify_login()

    def __get_cfg_path(self, loc=None):
        if loc is None:
            loc = "res/bot.ini"
        exec_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(os.path.split(exec_path)[0], loc)

    def __read_cfg_opt(self, cfg_parser, sect, opt):
        try:
            return cfg_parser.get(sect, opt)
        except:
            print("Unable to find option", opt, "in section", sect)
            
    def __verify_login(self):
        try:
            self.reddit.user.me()
            return True
        except prawcore.exceptions.OAuthException:
            return False 

    

if __name__ == "__main__":
    e = ConfigLoader()
    e.load_config()
    print(e.spawn_reddit_inst(True))
