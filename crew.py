from crewai import Crew
from agent import venue_coordinator, logistics_manager, marketing_communications_agent
from task import venue_task, logistics_task, marketing_task


# Define the crew with agents and tasks
event_management_crew = Crew(
    agents=[venue_coordinator, 
            logistics_manager, 
            marketing_communications_agent],
    
    tasks=[venue_task, 
           logistics_task, 
           marketing_task],
    
    verbose=True
)