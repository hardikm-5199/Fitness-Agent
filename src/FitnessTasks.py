from crewai import Task

from crewai import Task

def fitness_task(agent, user_goal, activity_level, concerns, gender, age, weight, height, name):
    return Task(
        description=f"""
        Create a personalized workout plan based on the user's goal and fitness level, activity level, concerns, gender, age, height, and weight.

        User Goal: {user_goal}
        Activity Level: {activity_level}
        User Concerns: {concerns}
        Gender: {gender}
        Age: {age}
        Weight: {weight} kg
        Height: {height} cm
        name: {name}

        The plan should include:
        - Weekly workout schedule (split by muscle groups or full-body)
        - Exercise details (name of exercise, sets, reps, rest time)
        - Alternative exercises for any user limitations
        """,
        expected_output="A detailed markdown workout plan tailored to the user's needs.",
        agent=agent,
        output_file='workout_plan.md',
    )

def nutrition_task(agent, user_goal, dietary_preferences, allergies):
    return Task(
        description=f"""
        Provide a nutrition guide based on the user's fitness goal and dietary preferences.

        User Goal: {user_goal}
        Dietary Preferences: {dietary_preferences}
        Allergies/Restrictions: {allergies}

        The guide should include:
        - Suggested macronutrient breakdown (protein, carbs, fats)
        - Meal suggestions with portion sizes
        - Pre- and post-workout nutrition recommendations
        """,
        expected_output="A structured markdown nutrition guide.",
        agent=agent,
        output_file='nutrition_plan.md',
    )

def motivation_task(agent, user_goal, challenges, motivation_level):
    return Task(
        description=f"""
        Provide motivational guidance and fitness tips tailored to the user's journey.

        User Goal: {user_goal}
        Challenges Faced: {challenges}
        Motivation Level: {motivation_level}

        The response should include:
        - Motivational advice based on their goal
        - Strategies to stay consistent with workouts and diet
        - Encouraging mindset tips to overcome challenges
        """,
        expected_output="A markdown report with motivation tips and fitness guidance.",
        agent=agent,
        output_file='motivation_tips.md',
    )
    
def editor_task(agent):
    return Task(
        description=f"""
        Edit and refine the workout, nutrition, and motivational plans to ensure they are accurate, engaging, and easy to follow.
        
        The response should include:
        - A final fitness plan that combines the workout, nutrition, and motivational aspects
        - Clear instructions and guidelines for the user to follow
        - Engaging content to keep the user motivated and on track
        """,
        expected_output="A markdown report with the final fitness plan.",
        agent=agent,
        output_file='final_plan.md',
    )

