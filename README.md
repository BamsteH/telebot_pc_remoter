# telebot_pc_remoter

This is a Python script that uses the `telebot` library to create a Telegram bot that can perform certain actions on your computer remotely. The bot is capable of executing commands that are defined in a keyboard file.

## Features

- The bot can turn off your computer remotely.
- The bot can open a radio link in your web browser.

## Requirements

- Python 3.6 or higher
- `telebot` library

## Setup

1. Clone dist package from GitHub
2. Run main.exe file
3. Open Telegram and create a new bot using the BotFather or use an existing one
4. Copy the token and paste it in console
5. After that to prevent the bot from being used by unauthorized users, you need to write to your bot the command `/start` and then the bot will send you your user id in the console
6. Copy the user id and paste it in the console
7. Now you can use the bot

## Modifying

You can easily modify the bot to add more commands or change the existing ones. To do this, you need to modify 
the methods in the @bot.message_handler section of the code. You can also modify the keyboard file to add more commands.

After that you can build your own .exe file using pyinstaller or any other tool.
To run it, you need to install pip package PyInstaller and run the following command in the console:
```bash
pyinstaller --onefile main.py
```

## License

MIT License

Copyright (c) 2024 Shapovalenko A.R.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.