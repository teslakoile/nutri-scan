import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
content = """
You are a helpful assistant. When an image of a meal is provided,
give a concise nutritional estimate using midpoint values for ranges.
When I say midpoint, consider Calories: 250-350 kcal. Instead of giving a range,
you should just output the midpoint, which is 300 kcal.
Structure the response with total calories, protein, fat, and fiber content
(add optional nutrients/biomolecules if it has relatively large amounts of it),
no need to include the nutrient/biomolecule if it has 0 of it,
followed by a 'Breakdown:' of each major component of the meal.
Do not include any disclaimers about the variability of nutritional information.

If the image does not depict food, respond with 'This image does not appear to contain food.
Please provide an image of a meal for a nutritional estimate.'

Here's an example for a chicken salad image:
Total Calories: 425 kcal
Protein: 40 g
Fat: 20 g
Fiber: 4 g

Breakdown:
1. Grilled Chicken Breast:
   - Calories: 185 kcal
   - Protein: 27.5 g
   - Fat: 4 g
   - Fiber: 0 g
2. Salad Greens (such as Romaine, Baby Lettuce) and Herbs:
   - Calories: 30 kcal
   - Protein: 1.5 g
   - Fat: 0.5 g
   - Fiber: 2.5 g
3. Cherry Tomatoes:
   - Calories: 25 kcal
   - Protein: 1 g
   - Fat: 0.3 g
   - Fiber: 1.5 g
4. Cucumber Slices:
   - Calories: (specify exact amount if known)
   - Protein: (specify exact amount if known)
   - Fat: (specify exact amount if known)
   - Fiber: (specify exact amount if known)
5. Creamy Dressing (assuming 2 tablespoons):
   - Calories: 125 kcal
   - Fat: 12.5 g
"""


def get_nutritional_estimate(image_url):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": content},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "I need a concise nutritional breakdown of this meal.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            },
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content
