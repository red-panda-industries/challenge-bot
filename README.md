# Red Panda Challenge Discord Bot

The **Red Panda Challenge Discord Bot**, or **`rpc-bot`** for short, is the robotic minister of the **Red Panda Challenge** (**RPC**). The good robot communicates with our plane of existence via the portal known as [Discord](https://discord.com/). The `rpc-bot` is the first robot to be minted by the emerging and powerful [Red Panda Industries](https://github.com/red-panda-industries).

The RPC is a daily exercise challenge with multiple activities and levels.

Currently, the `rpc-bot` has limited functionality. This project is in early stages of development.

## Setting up the bot configuration

After obtaining a copy of this repository, you must create a working configuration file.

If you are an editor of this repository, unlock the existing encrypted configuration file with [git-crypt](https://www.agwa.name/projects/git-crypt/), using the command `git-crypt unlock config.json`.

If you are creating your own bot instance, you must delete the encrypted `config.json` file in this repository and create your own. It should look like this:

`config.json`
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

To obtain values for `application_id` and `token`, you must create an **application** and a corresponding **bot** on the [Discord Developer Portal](https://discord.com/developers/applications).

To obtain your user ID, see &ldquo;[How to find your unique Discord ID](http://web.archive.org/web/20230313045358/https://www.businessinsider.com/guides/tech/discord-id).&rdquo;

<table>
  <caption>Required entries in <code>config.json</code></caption>
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

Finally, invite your bot onto your server by following this invite link in your browser (replacing `YOUR_APPLICATION_ID_HERE` with the application ID):

```
https://discord.com/oauth2/authorize?scope=bot+applications.commands&permissions=36574522433&client_id=YOUR_APPLICATION_ID_HERE
```

## Installation

To run the bot, you need the **Python** programming language (**version&nbsp;3.9 or later**) and a few packages.

### Using Conda environment manager

This is the recommended method for running this project.

If the `conda` command is not available on your machine, install the **[miniconda](https://docs.conda.io/en/latest/miniconda.html)** distribution.

Install packages and create the `challenge-bot` environment:

```bash
conda env create -f environment.yml
```

Then activate the environment:

```bash
conda activate challenge-bot
```

### Using Pip package installer

Install packages:

```bash
python -m pip install -r requirements.txt
```

## Starting the server

```bash
python bot.py
```

## License

This project is licensed under the Apache License, version&nbsp;2.0. See the [LICENSE.md](LICENSE.md) file for details.

&copy; 2021 Krypton <br>
&copy; 2023 Jackson Willis <br>
&copy; 2023 multiusersystem