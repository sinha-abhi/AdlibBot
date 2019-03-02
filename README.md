Python 3.6.x

# Reddit Bot
A Reddit bot under construction...

## Getting started

### Classes for public use

#### ConfigLoader
`ConfigLoader` is in module `loader`.
Use this class to generate an instance of `praw.Reddit`. Files are loaded
from a config file (whose default location is `res/bot.ini`).

##### Examples
###### Spawning a Reddit instance with login verification 
```python
from loader import ConfigLoader

loader = ConfigLoader("res/bot.ini")

loader.load_config()

login_res = loader.spawn_reddit_inst(verify=True)
if not login_res[1]: 
    print("Unsuccessful login")
else:
    reddit = login_res[0]
    print("Successful login", reddit.user.me())
```
In the case of `verify=True`, `spawn_reddit_inst()` returns a tuple containing
a Reddit instance, and boolean indicating sucess.

###### Spawning a Reddit instance without login verification 
```python
from loader import ConfigLoader

loader = ConfigLoader("res/bot.ini")

loader.load_config()

reddit = loader.spawn_reddit_inst(verify=False)
```
In the case of `verify=False`, `spawn_reddit_inst()` returns a
Reddit instance.

*WARNING*: In this case, we have not verified whether PRAW was able to
establish a connection with Reddit or not. If the connection failed, 
then a prawcore.expceptions.OAuthException will be raised. The method
presented in the first example is recommended.
