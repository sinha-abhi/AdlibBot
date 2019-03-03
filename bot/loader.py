#!/usr/bin/python3
from datetime import datetime
import logging
import os
import praw
import prawcore
import yaml


_CFG_FILE = "bot.yaml"

class ConfigLoader(object):

    def __init__(self, loc="res/"):
        """
        Initializes ConfigLoader through configuration files provided.

        The ConfigLoader expects a file given by the name above.
        For more information on these files, see the res/examples/ directory.
        
        Parameters
        ----------
        loc : string
              Directory location of configuration files.
              Default location is res/.
        """
        self.ex_pth = os.path.dirname(os.path.realpath(__file__))
        cfg_pth = os.path.join(os.path.split(self.ex_pth)[0], loc)
        
        self.config = self._read_yaml(cfg_pth)
        self.__has_logger = False

    def _read_yaml(self, path):
        with open(os.path.join(path, _CFG_FILE), "r") as __cfg:
            return yaml.load(__cfg)

    def _verify_login(self):
        try:
            self.reddit.user.me()
            return True
        except prawcore.exceptions.OAuthException:
            return False 

    def get_subreddit_list(self):
        return self.config["subreddits"] 

    def init_logger(self):
        # build dict for logger levels
        _levels = {"DEBUG": logging.DEBUG,
                   "INFO": logging.INFO,
                   "WARNING": logging.WARNING,
                   "ERROR": logging.ERROR,
                   "CRITICAL": logging.CRITICAL}

        log_cfg = self.config["logging"]

        log_pth = os.path.join(self.ex_pth, log_cfg["location"])
        if not os.path.exists(log_pth):
            os.makedirs(log_pth)

        log_file = (log_cfg["location"]
                    + log_cfg["filename"] 
                    + datetime.now().strftime("%m-%d-%Y")
                    + "." + log_cfg["fileformat"])

        logging.basicConfig(filename = log_file,
                            filemode = "w",
                            format = log_cfg["format"],
                            level = _levels[log_cfg["level"]])

        logging.info("Initialized logger!")
        self.__has_logger = True;

        return logging.getLogger(__name__)

    def spawn_reddit_inst(self):
        if not self.__has_logger:
            print("[ERROR] Logger not initialized, but is required. " 
                  + "Initialize logger by calling init_logger().")
            exit(1)

        reddit_cfg = self.config["login"]
        logging.info("Logging into Reddit...")
        self.reddit = praw.Reddit(client_id = reddit_cfg["client_id"],
                                  client_secret = reddit_cfg["client_secret"],
                                  user_agent = reddit_cfg["user_agent"],
                                  username = reddit_cfg["username"],
                                  password = reddit_cfg["password"])

        if self._verify_login():
            logging.info("Login successful.")
            return self.reddit
        else:
            logging.critical("Login failed.")
            return None

