# Red Panda Challenge Discord Bot

## Configuration

Uses `git-crypt`.

These configuration options in [config.json](config.json) are required:

| Name                      | Description                                                           |
| ------------------------- | ----------------------------------------------------------------------|
| YOUR_BOT_PREFIX_HERE      | The prefix you want to use for normal commands                        |
| YOUR_BOT_TOKEN_HERE       | The token of your bot                                                 |
| YOUR_BOT_PERMISSIONS_HERE | The permissions integer your bot needs when it gets invited           |
| YOUR_APPLICATION_ID_HERE  | The application ID of your bot                                        |
| OWNERS                    | The user ID of all the bot owners                                     |

## Installation

**Using Conda (recommended):**

Install dependencies and create the `challenge-bot` environment:

```
conda env create -f environment.yml
```

Then activate the environment:

```
conda activate challenge-bot
```

**Using Pip**

Install dependencies:

```
python -m pip install -r requirements.txt
```

## Starting the server

```
python bot.py
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
