from FitnessAgents import Fitness_expert, Nutrition_expert, Motivational_Trainer,Plan_Editor
from FitnessTasks import fitness_task, nutrition_task, motivation_task, editor_task
from crewai import Crew, Process
import streamlit as st

# Streamlit App Title
st.title("💪 AI-Powered Fitness & Nutrition Assistant")

st.markdown("""
🏋️ **Achieve Your Fitness Goals with AI!**  
Get personalized workout plans, tailored nutrition advice, and expert motivation—all in one place.  

### 🔥 What You Can Do:  
✅ **Custom Workouts** – Get exercise plans based on your fitness goal & activity level.  
🥗 **Smart Nutrition** – Receive diet recommendations tailored to your preferences.  
🎯 **Stay Motivated** – Get tips & encouragement to stay consistent.  

Just enter your details below and let AI guide you on your fitness journey! 🚀🏆  
""")

# Personal Information
name = st.text_input("👤 Name", placeholder="Enter your name")
age = st.number_input("🎂 Age", min_value=10, max_value=100, step=1, placeholder="Enter your age")
gender = st.selectbox("⚧ Gender", ["Male", "Female", "Other"], index=0)
weight = st.number_input("⚖️ Weight (kg)", min_value=20.0, max_value=300.0, step=0.5, placeholder="Enter your weight in kg")
height = st.number_input("📏 Height (cm)", min_value=50, max_value=250, step=1, placeholder="Enter your height in cm")

# Activity & Fitness Goal
activity_level = st.selectbox(
    "🏃 Activity Level", 
    ["Sedentary (little or no exercise)", "Lightly active (1-3 days/week)", "Moderately active (3-5 days/week)", 
     "Very active (6-7 days/week)", "Super active (athlete, intense exercise)"],
    index=1
)
user_goal = st.selectbox("🎯 Fitness Goal", ["Muscle Gain", "Fat Loss", "Stay Active"], index=0)

# Health Concerns
concerns = st.text_area("⚠️ Any Health Concerns?", placeholder="E.g., knee pain, back issues, or specific injuries")

# Nutrition Preferences
dietary_preferences = st.selectbox(
    "🥗 Dietary Preference", 
    ["Balanced Diet", "Vegetarian", "Vegan", "Pescatarian", "Keto", "Low-Carb", "Mediterranean", "Other"], 
    index=0
)
allergies = st.text_input("🚫 Allergies/Restrictions", placeholder="E.g., gluten-free, nut allergy, lactose intolerance")

# Motivation & Challenges
challenges = st.text_area("💭 Challenges Faced", placeholder="E.g., lack of motivation, consistency, time constraints")
motivation_level = st.selectbox("🔥 Motivation Level", ["Low", "Medium", "High"], index=1)

st.markdown("---")
st.markdown("Click the button below to generate your **personalized fitness & nutrition plan**! 🚀")


# Button to run CrewAI
if st.button("🚀 Generate The Plan"):
    with st.spinner("⏳ AI is preparing your personalized fitness & nutrition plan... Please wait."):
        # Initialize Tasks
        fit_task = fitness_task(Fitness_expert, user_goal, activity_level, concerns, gender, age, weight, height, name)
        nutr_task = nutrition_task(Nutrition_expert, user_goal, dietary_preferences, allergies)
        mot_task = motivation_task(Motivational_Trainer, user_goal, challenges, motivation_level)
        edit_task= editor_task(Plan_Editor)

        # Define Crew
        crew = Crew(
            agents=[Fitness_expert, Nutrition_expert, Motivational_Trainer,Plan_Editor],
            tasks=[fit_task, nutr_task, mot_task,edit_task],
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )
        # Run Crew AI
        result = crew.kickoff()

        # Display Results
        st.subheader("📋 Your Personalized Fitness & Nutrition Plan:")
        st.markdown(result)

        # Ensure result is a string
        fitness_plan_text = str(result)  # ✅ Convert CrewOutput to string

        st.download_button(
            label="📥 Download Fitness Plan",
            data=fitness_plan_text,  # ✅ Now passing a valid string
            file_name=f"fitness_plan_for_{name}.txt",
            mime="text/plain"
        )