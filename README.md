# Chrotry

Search all history of Chrome in terminal.

## Usages

- Move the Chrome history file to current directory by running `move_history.sh`
- Rename `history_db_{timestamp}` file to the name `DB`
- [Optional] migration.py script is to merge the newest history file to `DB` file
  - `./migration.py history_db_1638637824`, it will merge `history_db_1638637824` to `DB` file
- chrotry to search title, url in terminal

### Shortcuts

- CTRL + n, move one line down
- CTRL + p, move one line up
- CTRL + e, quit
