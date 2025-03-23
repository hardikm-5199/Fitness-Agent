#!/usr/bin/env python
import sys
import streamlit as st
from crew import FitnessagentCrew
import agentstack
import agentops
from FitnessApp import *

def run():
    """
    Run the Streamlit application with AgentStack integration.
    """
    agentops.init(default_tags=agentstack.get_tags())
    

    if st.button("🚀 Generate The Plan"):
        with st.spinner("⏳ AI is preparing your personalized fitness & nutrition plan..."):
            # Prepare user data for the crew
            user_data = {
                'name': name,
                'age': age,
                'gender': gender,
                'weight': weight,
                'height': height,
                'activity_level': activity_level,
                'user_goal': user_goal,
                'concerns': concerns,
                'dietary_preferences': dietary_preferences,
                'allergies': allergies,
                'challenges': challenges,
                'motivation_level': motivation_level
            }
            
            # Initialize crew with user data
            fitness_crew = FitnessagentCrew(user_data=user_data)
            
            # Execute the crew tasks
            result = fitness_crew.crew().kickoff()
            

if __name__ == '__main__':
    run()