from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
import agentstack
import os

llm = LLM(
    model = "groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

#agents
Fitness_expert = Agent(
    role="Fitness Expert",
    goal="Creates personalized workout routines based on user goals, activity levels, and any physical limitations.",
    backstory="A certified personal trainer with years of experience in designing effective workout plans for different fitness levels.",
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

Nutrition_expert = Agent(
    role="Nutrition Expert",
    goal="Provides dietary recommendations and nutrition advice based on user fitness goals and dietary preferences.",
    backstory="A knowledgeable nutritionist who helps individuals optimize their diet for muscle gain, fat loss, and overall health.",
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

Motivational_Trainer = Agent(
    role="Motivational Trainer",
    goal="Offers motivation, guidance, and fitness tips to keep users engaged and committed to their fitness journey.",
    backstory="A passionate fitness coach who inspires individuals to stay consistent, overcome challenges, and achieve their fitness goals.",
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

Plan_Editor = Agent(
    role="Plan Editor",
    goal="Edits and refines the workout and nutrition plans and motivational plans to ensure they are accurate, engaging, and easy to follow.",
    backstory="An experienced editor who fine-tunes the fitness plans to make them more user-friendly and effective.",
    verbose=True,
    max_iter=5,   
    llm=llm,
    allow_delegation=False,
    output_file='final_plan.md',
)
