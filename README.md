# Red Panda Challenge Discord Bot

The **Red Panda Challenge Discord Bot**, or **`rpc-bot`** for short, is the robotic minister of the **Red Panda Challenge**. The good robot communicates with our plane of existence via the portal known as **[Discord](https://discord.com/)**. The `rpc-bot` is the first robot to be minted by the emerging and powerful **[Red Panda Industries](https://github.com/red-panda-industries)**.

<figure>
  <img alt="Preacherbot from Futurama" src="images/preacherbot.png" height=200 width=200>
  <figcaption>

  Figure&nbsp;1: A robotic minister

  </figcaption>
</figure>

## The Red Panda Challenge

The **Red Panda Challenge** (**RPC**) is a daily exercise challenge with multiple activities and levels.

Currently, the `rpc-bot` has limited functionality. This project is in early stages of development.

## Available commands

| Command | Description |
| --- | --- |
| `/help` | List available commands. |
| `/randomfact` | Get a random fact. |
| `/coinflip` | Make a coin flip, but give your bet before. |
| `/rps` | Play the rock paper scissors game against the bot. |
| `/ping` | Check if the bot is alive. |
| `/botinfo` | Get some information about the bot. |

## Setting up the bot

To run the bot yourself, first download or clone this repository.

```bash
git clone git@github.com:red-panda-industries/challenge-bot.git
cd challenge-bot
```

After obtaining a copy of this repository, you must set up the configuration file.

If you are a member of Red Panda Industries, unlock the encrypted configuration file with **[git-crypt](https://www.agwa.name/projects/git-crypt/)**, using this command:

```bash
git-crypt unlock config.json
```

If you are creating your own bot instance, you must delete the encrypted `config.json` and create your own. It should look like this:

<figure>
<figcaption>

Figure&nbsp;2: `config.json` example

</figcaption>

```json
{
  "application_id": "YOUR_APPLICATION_ID_HERE",
  "token": "YOUR_BOT_TOKEN_HERE",
  "owners": [
    111111,
    2222222333445
  ],
  "prefix": "!rpc ",
  "permissions": "36574522433",
  "sync_commands_globally": true,
}
```

</figure>

**Note: Never publish your unencrypted `config.json` file or any secrets anywhere public.**

To obtain values for `application_id` and `token`, you must create an **application** and a corresponding **bot** on the [Discord Developer Portal](https://discord.com/developers/applications).

To obtain your user ID, see &ldquo;[How to find your unique Discord ID](http://web.archive.org/web/20230313045358/https://www.businessinsider.com/guides/tech/discord-id).&rdquo;

<figure>
<figcaption>

Figure&nbsp;3: Required entries in `config.json`

</figcaption>
<table>
  <thead>
    <tr>
      <th>Key name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>application_id</code></td>
      <td>The application ID of your bot.</td>
    </tr>
    <tr>
      <td><code>token</code></td>
      <td>The token of your bot.</td>
    </tr>
    <tr>
      <td><code>owners</code></td>
      <td>The Discord user IDs of all the bot owners.</td>
    </tr>
    <tr>
      <td><code>prefix</code></td>
      <td>The prefix you want to use for normal commands (including an optional trailing space).</td>
    </tr>
    <tr>
      <td><code>permissions</code></td>
      <td>Represents the permissions needed by the bot, which in this case, is <code>"36574522433"</code>. See <a href="https://discordapi.com/permissions.html">Discord Permissions Calculator</a>.</td>
    </tr>
    <tr>
      <td><code>sync_commands_globally</code></td>
      <td>Whether to offer slash commands globally within the server, as opposed to only for users in the same guild.</td>
  </tbody>
</table>
</figure>

Finally, invite your bot onto your server by following this invite link in your browser (replacing `YOUR_APPLICATION_ID_HERE` with the application ID):

<!-- https://discord.com/oauth2/authorize?scope=bot+applications.commands&permissions=36574522433&client_id=YOUR_APPLICATION_ID_HERE -->

<figure>
<code>https:<span>//</span>discord.com/oauth2/authorize<wbr>?scope=bot+applications.commands<wbr>&permissions=36574522433<wbr>&client_id=YOUR_APPLICATION_ID_HERE</strong></code>
</figure>

## Installation

To run the bot, you need **[Python](https://www.python.org/)** and a few packages.

Python versions **3.10 and&nbsp;greater** are supported.

The packages can be installed through the **[conda](https://docs.conda.io/en/latest/)** environment manager or the **[pip](https://pypi.org/project/pip/)** package manager that comes pre-installed with Python.

### Using Conda

We recommend using Conda to run this bot, as it allows for better control over the Python environment.

If you don't already have the `conda` command on your machine, install it using **[Miniconda](https://docs.conda.io/en/latest/miniconda.html)**.

The Miniconda installer includes its own copy of Python, and Conda may download additional versions of Python. This is intentional, as it allows us to create clean Python environments.

To install the packages and create the `challenge-bot` environment, run:

```bash
conda env create -f environment.yml
```

You must activate the environment before starting the bot, like:

```bash
conda activate challenge-bot
```

Activating the environment ensures that the correct versions of Python and other packages are installed and selected for use.

### Using Pip

Install the packages:

```bash
python -m pip install -r requirements.txt
```

## Starting the bot

```bash
python bot.py
```

## Open source

The Red Panda Challenge Discord Bot is distributed under the terms of the **[Apache License, Version&nbsp;2.0](https://en.wikipedia.org/wiki/Apache_License)**.

In practice, this means that you are **free to use, modify and distribute the bot**, as long as any redistribution of the software includes the **original copyright notice** and a **copy of the license**.

See [LICENSE.md](LICENSE.md) for details.

&copy; 2021 Krypton <br>
&copy; 2023 Jackson Willis <br>
&copy; 2023 multiusersystem