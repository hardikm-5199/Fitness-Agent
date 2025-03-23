from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import agentstack
from FitnessAgents import Fitness_expert, Nutrition_expert, Motivational_Trainer
from FitnessTasks import fitness_task, nutrition_task, motivation_task

@CrewBase
class FitnessagentCrew():
    """fitness_agent crew"""

    def __init__(self, user_data=None):
        self.user_data = user_data or {}
    
    @crew
    def crew(self) -> Crew:
        """Creates the Fitness crew with tasks based on user data"""
        tasks = []
        
        if self.user_data:
            tasks = [
                fitness_task(
                    Fitness_expert,
                    self.user_data.get('user_goal'),
                    self.user_data.get('activity_level'),
                    self.user_data.get('concerns'),
                    self.user_data.get('gender'),
                    self.user_data.get('age'),
                    self.user_data.get('weight'),
                    self.user_data.get('height'),
                    self.user_data.get('name')
                ),
                nutrition_task(
                    Nutrition_expert,
                    self.user_data.get('user_goal'),
                    self.user_data.get('dietary_preferences'),
                    self.user_data.get('allergies')
                ),
                motivation_task(
                    Motivational_Trainer,
                    self.user_data.get('user_goal'),
                    self.user_data.get('challenges'),
                    self.user_data.get('motivation_level')
                )
            ]
        
        return Crew(
            agents=[Fitness_expert, Nutrition_expert, Motivational_Trainer],
            tasks=tasks,
            process=Process.sequential,
            verbose=True,
            output_file='fitness_plan.txt'
        )