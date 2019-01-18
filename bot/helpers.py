#!/usr/bin/python3
import configparser
import praw

class ExtractorHelper(object):
    def __init__(self):
        pass

    def read_cfg_opt(self, cfg_parser, sect, opt):
        try:
            return cfg_parser.get(sect, opt)
        except:
            print("Unable to find option", opt, "in section", sect)
            raise configparser.NoSectionError
