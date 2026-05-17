# The Watcher
A simple discord bot that notifies users when Lost Ark server maintenance has concluded.

## Prerequisites
[UV package manager](https://github.com/astral-sh/uv)

## Installation
1. Clone the repository

2. Sync the project
```bash
uv sync --locked
```

3. Setup Environment Variables
```bash
cp .env.example .env
```

| Variable     | Description                                           |
| :---:        | :---:                                                 |
| `BOT_TOKEN`  | Discord Bot API token from the Developer Portal       |
| `CHANNEL_ID` | The channel where maintenance messages will be posted |
| `GUILD_ID`   | The server ID                                         |
| `ROLE_ID`    | The role to be notified                               |

## Usage
```bash
uv run ./main.py
```

The bot will start monitoring only when maintenance is scheduled to start.

To manually start monitoring in case of emergency maintenance use the `/monitor` command

### Docker Compose
For a no-fuss docker daemon use the included compose file

```bash
docker compose up -d
```
