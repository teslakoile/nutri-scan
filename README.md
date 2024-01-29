# NutriScan
NutriScan is a Discord bot that provides nutritional estimates for meals based on images you provide. It utilizes OpenAI's GPT-4 Vision model to analyze images of food and return a concise breakdown of their nutritional content.

## Features
- Analyzes images of meals and provides a nutritional estimate.
- Supports various image formats (jpg, jpeg, png, gif, bmp).
- Provides a concise breakdown of total calories, protein, fat, and fiber content.
- Includes a 'Breakdown' of each major component of the meal.

## How it works
This project consists of two main Python scripts: `bot.py` and `vision_ai.py`

### `bot.py`
- This script is responsible for the main functionality of the bot. It handles user interactions, processes user inputs, and generates appropriate responses. The bot uses various AI and machine learning techniques to understand and respond to user queries.

### `vision_ai.py`
- This script is responsible for image analysis. When provided with an image of a meal, it gives a concise nutritional estimate using midpoint values for ranges. The response includes total calories, protein, fat, and fiber content. It also provides a breakdown of each major component of the meal. If the image does not depict food, it responds with a message asking for an image of a meal.

## Installation
### Clone this repository to your local machine:

`git clone https://github.com/yourusername/nutri-bot.git`

### Install the required Python packages:
`pip install -r requirements.txt`

### Create a .env file in the project directory and add your Discord bot token and OpenAI API key:

```
DISCORD_BOT_TOKEN=your_discord_bot_token
OPENAI_API_KEY=your_openai_api_key
```

### Run the bot:
`python bot.py`

## Usage
To use NutriScan, simply mention it in a Discord chat and attach an image of a meal. NutriScan will analyze the image and provide a nutritional estimate in response.

`@NutriScan`<br/><br/>
<img src="/assets/salad.png" alt="Salad" width="300">


## Credits
NutriScan uses OpenAI's GPT-4 Vision model for image analysis.
