from schemas import FoodItem, MenuRequest

def menu_prompt(prompt_input: MenuRequest):
    elements_detailed = [
        f"Item: {item.name}, Macros (P:{item.proteins_g}, C:{item.carbohydrates_g}, F:{item.fats_g}), Quantity: {item.number}"
        for item in prompt_input.elements
    ]
    prompt_template = f"""Based on the following ingredients and their nutritional profile (P=Proteins, C=Carbohydrates, F=Fats), generate seven-day weekly menu using this language code {prompt_input.language}.
    The available ingredients are: {', '.join(elements_detailed)}.
    The returned JSON object must contain an array named 'menu' where each element is an object with the keys: 'day', 'breakfast', 'lunch', and 'dinner'.
    Translate all keys (day, breakfast, lunch, dinner) and all dish names into the requested language {prompt_input.language}.
    Fill breakfast, lunch and dinner for all days. Example structure: 
    {{ 
        "menu": [
            {{ 
                "day": "Lunes",
                "breakfast": "Omelet con espinacas (25gr)",
                "lunch": "Ensalada de pollo (20gr)",
                "dinner": "Pechuga a la parrilla (20gr)"
            }} 
        ]
    }}
    """
    return prompt_template