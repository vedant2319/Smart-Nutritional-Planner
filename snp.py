# Smart Nutritional PLanner : Vedant Rajesh Naik (14 June 2024)
# Simple Python code with predefined data

import random

# Sample data for meals using dictionary
meals = {
    "breakfast": [
        {"name": "Oatmeal with Berries", "calories": 250, "protein": 10, "carbs": 45, "fat": 5},
        {"name": "Scrambled Eggs with pea", "calories": 300, "protein": 20, "carbs": 10, "fat": 20},
        {"name": "Oat Bowl with milk", "calories": 200, "protein": 5, "carbs": 35, "fat": 5}
    ],
    "lunch": [
        {"name": "Grilled Chicken Salad", "calories": 350, "protein": 30, "carbs": 20, "fat": 15},
        {"name": "Quinoa and Black Beans", "calories": 400, "protein": 15, "carbs": 60, "fat": 10},
        {"name": "Chicken Sandwich", "calories": 300, "protein": 25, "carbs": 40, "fat": 8}
    ],
    "dinner": [
        {"name": "Salmon with Veggies", "calories": 450, "protein": 35, "carbs": 20, "fat": 25},
        {"name": "Vegetable Stir Fry", "calories": 400, "protein": 10, "carbs": 70, "fat": 15},
        {"name": "Chicken Tacos", "calories": 500, "protein": 30, "carbs": 50, "fat": 20}
    ],
    "snack": [
        {"name": "Yogurt", "calories": 150, "protein": 15, "carbs": 10, "fat": 5},
        {"name": "Apple with Peanut Butter", "calories": 200, "protein": 5, "carbs": 30, "fat": 10},
        {"name": "Trail Mix", "calories": 250, "protein": 8, "carbs": 20, "fat": 15}
    ]
}

# Function to generate a meal plan
def generate_meal_plan(preferences):
    meal_plan = {}
    for meal_time, meal_options in meals.items():
        filtered_meals = [meal for meal in meal_options if all(pref in meal['name'].lower() for pref in preferences)]
        if filtered_meals:
            meal_plan[meal_time] = random.choice(filtered_meals)
        else:
            meal_plan[meal_time] = random.choice(meal_options)
    return meal_plan

# User-input
user_preferences = input("Enter your dietary preferences (e.g., 'balanced-diet', 'low-carb', 'high-protein'): ").lower().split()

# Display of meal plan
meal_plan = generate_meal_plan(user_preferences)
print("\nPersonalized Meal Plan:")
for meal_time, meal in meal_plan.items():
    print(f"{meal_time.capitalize()}: {meal['name']} - Calories: {meal['calories']}, Protein: {meal['protein']}g, Carbs: {meal['carbs']}g, Fat: {meal['fat']}g")
