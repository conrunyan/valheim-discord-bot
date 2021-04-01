# Valheim Discord Bot

This discord bot is intended to provide quick tools to quickly retrieve information about your dedicated Valheim server. It currently only supports the Linux version, as that's the only dedicated server I've used up to this point. 

IMPORTANT NOTE: This bot needs to be running on the same server/container/etc. as your Valheim server.

## Getting Started

Setting up the discord bot involves a few steps, including creating a new application and bot on the Discord developer platform.

If you are new to creating a Discord Bot, the "discord.py" docs are very helpful.
* [Introduction to discord.py](https://discordpy.readthedocs.io/en/latest/intro.html)
* [Creating a Bot Account on Discord's Developer Platform](https://discordpy.readthedocs.io/en/latest/discord.html)



### Prerequisites

* Python 3.6+ (Uses Python's formatted strings)
* Valheim dedicated server running on a Linux machine
* A new discord Application and associated Bot (see Creating a Bot Account above)

### Installing

First, you need to set up the Python environment. To do this, execute the following from the project directory:
```
bash install_heimdall.sh
```
Heimdall.py uses the dotenv library, and looks for a .env file in the same directory. 
Make a copy of the .env_template file.
```
cp .env_template .env
```
Using your favorite editor, replace the "<YOUR_TOKEN_HERE>" snippet in the new .env file with your bot's token.

By default, the bot assumes your server is logging to "/var/log/syslog". If it is not, you wil need to edit the "SYS_LOG" variable in heimdall.py (line 40).
Be sure this points to whatever file contains the server logs. 

Now you're all set! Run the below command to start up Heimdall!
```
bash start_heimdall.sh
```
OPTIONAL
The discord bot will not run in the background by default. If you want it to run in the background, there are a few options:

1 - Run the bot as a process, sending it to the background with "&"
```
bash start_heimdall.sh &
```
2 - Setting the bot as a system service using systemd
```
#TODO: Add steps on how to make it a service
```

## Running the tests

```
pytest test_valheim_server_tools.py
```

## Built With

* [Discord.py](https://discordpy.readthedocs.io/en/latest/)

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/conrunyan/valheim-discord-bot/tags). 

## Authors

* **Connor Runyan** - *Initial work* - [https://github.com/conrunyan](https://github.com/conrunyan)

See also the list of [contributors](https://github.com/conrunyan/valheim-discord-bot/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* PurpleBooth for the [README tempalte](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* Nimdy and the folks working on the [Dedicated Valheim Server Script](https://github.com/Nimdy/Dedicated_Valheim_Server_Script)
