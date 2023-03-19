# Installing the Red Panda Challenge Bot

## Clone the repository


```bash
git clone git@github.com:red-panda-industries/challenge-bot.git
cd challenge-bot
```

## Set up the config file


The configuration file in this repository, `config.json`, is encrypted.

If you are a member of Red Panda Industries, unlock the file with **[git-crypt](https://www.agwa.name/projects/git-crypt/)**:

```bash
git-crypt unlock
```

If you are creating your own bot instance, you must delete the encrypted `config.json` (and `.git-crypt` directory) and create your own. It should look like this:

<figure>
<figcaption>

Figure: `config.json` example

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

**Note: Never publish your `config.json` file (unencrypted), or generally any secrets.**

To get your `application_id` and `token`, you must create an **application** and a corresponding **bot** on the **[Discord Developer Portal](https://discord.com/developers/applications)**.

To get your user ID, for the `owners` parameter, see &ldquo;[How to find your unique Discord ID](http://web.archive.org/web/20230313045358/https://www.businessinsider.com/guides/tech/discord-id).&rdquo;

<figure>
<figcaption>

Figure: Required entries in `config.json`

</figcaption>
<dl>
<dt><code>application_id</code></dt>
<dd>The application ID of your bot.</dd>
<dt><code>token</code></dt>
<dd>The token of your bot.</dd>
<dt><code>owners</code></dt>
<dd>The Discord user IDs of all the bot owners.</dd>
<dt><code>prefix</code></dt>
<dd>The prefix you want to use for normal commands (including an optional trailing space).</dd>
<dt><code>permissions</code></dt>
<dd>Represents the permissions needed by the bot, which in this case, is <code>"36574522433"</code>. See <a href="https://discordapi.com/permissions.html">Discord Permissions Calculator</a>.</dd>
<dt><code>sync_commands_globally</code></dt>
<dd>Whether to offer slash commands globally within the server, as opposed to only for users in the same guild.</dd>
</dl>
</figure>

Finally, invite your bot onto your server by following this invite link in your browser (replacing `YOUR_APPLICATION_ID_HERE` with the application ID):

<!-- https://discord.com/oauth2/authorize?scope=bot+applications.commands&permissions=36574522433&client_id=YOUR_APPLICATION_ID_HERE -->

<figure>
<code>https:<span>//</span>discord.com/oauth2/authorize<wbr>?scope=bot+applications.commands<wbr>&permissions=36574522433<wbr>&client_id=YOUR_APPLICATION_ID_HERE</strong></code>
</figure>

## Install dependencies

To run the bot, you need **[Python](https://www.python.org/)** and a few packages.

Python versions **3.10 and&nbsp;greater** are supported.

The packages can be installed through the **[conda](https://docs.conda.io/en/latest/)** environment manager or the **[pip](https://pypi.org/project/pip/)** package manager that comes pre-installed with Python.

### Using Conda

We recommend using Conda to run the bot, as it allows for better control over the Python environment.

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
