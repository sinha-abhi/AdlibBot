#!/usr/bin/python3
import praw, json, os

# load config.json

if __name__ == '__main__':
        
    with open("config.json", 'r') as config_file:
        config = json.loads(config_file.read())

    reddit = praw.Reddit(client_id = config["client_id"],
                        client_secret = config["client_secret"],
                        user_agent = config["user_agent"],
                        username = config["username"],
                        password = config["password"])


    if reddit.user.me() != config["username"]:
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

    #
    jar = reddit.redditor("BadCondition")
    print(jar.name, "\'s karma: %d" % jar.comment_karma)
    jar.message("hello", "test", from_subreddit=None)
