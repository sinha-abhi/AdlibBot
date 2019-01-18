#!/usr/bin/python3
import praw, prawcore
import configparser


# Load information from config files
class ConfigLoader(object):

    def __init__(self):
        self.__cfg = configparser.ConfigParser()
        
        BOT_CFG = "../res/bot.ini"
        if not self.__cfg.read(BOT_CFG):
            print("Configuration file", BOT_CFG, "not found.")
            raise FileNotFoundError(BOT_CFG)

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
                
    def __verify_login(self):
        try:
            self.reddit.user.me()
            return True
        except prawcore.exceptions.OAuthException:
            return False 

    def __read_cfg_opt(self, cfg_parser, sect, opt):
        try:
            return cfg_parser.get(sect, opt)
        except:
            print("Unable to find option", opt, "in section", sect)


if __name__ == "__main__":
    e = ConfigLoader()
    e.load_config()
    print(e.spawn_reddit_inst(True))
