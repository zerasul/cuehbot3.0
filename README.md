# cuehbot3.0
Third Version of CuehBot for discord

This Discord bot allow to show Random Ducks images in your discord, using [Random Duck Api](https://random-d.uk/api).

This Bot is created using [Discord.py](https://discordpy.readthedocs.io/en/stable/) library.

Also you can use Docker to generate an image; with the next steps:

1. Create a new Discord Application Token in the [Discord Developer Portal](https://discord.com/developers/docs/intro).
2. Build a new image using Docker

```bash
docker build -t cuehbot.3.0 .
```

3. Run a new Container
```bash
docker run --env DISCORD_TOKEN=<discordtoken> cuehbot:3.0
```

**NOTE:** Also, you can add an .env file and add the DISCORD_TOKEN environment Variable.
