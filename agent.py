from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# print(GROQ_API_KEY)
# print(SERPAPI_KEY)

# print(type(GROQ_API_KEY))
# print(type(SERPAPI_KEY))

os.environ["GROQ_API_KEY"] = GROQ_API_KEY
os.environ["SERPAPI_KEY"] = SERPAPI_KEY

llm = ChatGroq(model_name="groq/Llama-3.3-70b-Versatile", api_key=GROQ_API_KEY) # model name should be in this format


# Initialize the tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


# Agent 1: Venue Coordinator
venue_coordinator = Agent(
    role="Venue Coordinator",
    goal="Identify and book an appropriate venue "
    "based on event requirements",
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "With a keen sense of space and "
        "understanding of event logistics, "
        "you excel at finding and securing "
        "the perfect venue that fits the event's theme, "
        "size, and budget constraints."
    ),
    llm=llm
)


 # Agent 2: Logistics Manager
logistics_manager = Agent(
    role='Logistics Manager',
    goal=(
        "Manage all logistics for the event "
        "including catering and equipmen"
    ),
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "Organized and detail-oriented, "
        "you ensure that every logistical aspect of the event "
        "from catering to equipment setup "
        "is flawlessly executed to create a seamless experience."
    ),
    llm=llm
)


# Agent 3: Marketing and Communications Agent
marketing_communications_agent = Agent(
    role="Marketing and Communications Agent",
    goal="Effectively market the event and "
         "communicate with participants",
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "Creative and communicative, "
        "you craft compelling messages and "
        "engage with potential attendees "
        "to maximize event exposure and participation."
    ),
    llm=llm
)