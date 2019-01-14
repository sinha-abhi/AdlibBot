#!/usr/bin/python3
import praw

USERNAME = "Adlib_bot"

reddit = praw.Reddit(client_id = "jlxtwwfRpUiYmw",
                     client_secret = "wwmXY-wJntO6VfpNzVVXQTKv2nw",
                     user_agent = "test connection of bot",
                     username = USERNAME,
                     password = "Preparation123")

if reddit.user.me() != USERNAME:
    print("unsuccessful login")
    exit(1)
else:
    print("successful login")
    print(reddit.user.me())
