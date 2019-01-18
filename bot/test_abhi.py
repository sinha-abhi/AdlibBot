#!/usr/bin/python3
import praw
import configparser

USERNAME = "Adlib_bot"

def reddit_test():
    # instance of Reddit
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

    # subreddit info

    sb = reddit.subreddit("nintendoswitch")

    print("subreddit: ", sb.display_name)
    #print("description: ", sb.description)
    print("number of subs: %d" % sb.subscribers)

    # let's bother jarrett

    jar = reddit.redditor("doctorjohnny")
    print(jar.name, "\'s karma: %d" % jar.comment_karma)
    # jar.message("hello", "test", from_subreddit=None)


config = configparser.ConfigParser()

if not config.read('random.ini'):
    print("fail")
    raise FileNotFoundError("random.ini")
