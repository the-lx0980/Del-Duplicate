
<h3 align="center">uniquify bot</h3>

  <p align="center">
    Uniquify bot is a Telegram bot that deletes duplicate files (Video, Audio, Photo, Voice, and Document) from target chat.
    <br />
    <a href="https://github.com/OxMohsen/uniquify-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/OxMohsen/uniquify-bot/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



## About The Project

uniquify bot will help you to find and delete duplicate files in your channel or group.
this bot uses `file_unique_id` to find duplicate files, so we can assure you that there is the same file as the deleted file in your group or channel.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [pyrogram](https://pyrogram.org/)

<p align="right">(<a href="#top">back to top</a>)</p>


## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Get your `api_id` and `api_hash` in [https://my.telegram.org](https://my.telegram.org)
2. Create a new bot in [https://t.me/botfather](https://t.me/botfather)
3. Clone the repo
   ```sh
   git clone https://github.com/OxMohsen/uniquify-bot.git
   ```
4. navigate into the new folder
   ```sh
   cd uniquify-bot
   ```
5. Install python packages
   ```sh
   pip3 install -r requirements.txt
   ```
5. rename the `sample-config.py` to `config.py`
6. fill the `config.py` with your data
7. run the bot
   ```sh
   python3 main.py
   ```

if you using heroku, you can run the bot with the following steps.
1. get your `api_id` and `api_hash` in [https://my.telegram.org](https://my.telegram.org)
2. create a new bot in [https://t.me/botfather](https://t.me/botfather)
3. press the following button:
    <br><a href="https://heroku.com/deploy?template=https://github.com/OxMohsen/uniquify-bot">
    <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
    </a>


<p align="right">(<a href="#top">back to top</a>)</p>
