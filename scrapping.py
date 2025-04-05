from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, WebsiteSearchTool
import os

# === API Keys ===
os.environ['SERPER_API_KEY'] = '4fa67bcb0515b8e5d69bfc5748a875b6b735ee95'
os.environ['OPENAI_API_KEY'] = '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'

# === Tools ===
search_tool = SerperDevTool()
web_reader = WebsiteSearchTool()

# === Agent ===
researcher = Agent(
    role='AI Researcher',
    goal='Search the web and summarize key insights from top sources.',
    backstory='An AI with strong reading and summarizing capabilities.',
    tools=[search_tool, web_reader],
    verbose=True
)

# === Task ===
user_topic = input("Enter a topic to research: ")
search_task = Task(
    description=f"Search for information about '{user_topic}' and return a clear, structured summary of what is found.",
    expected_output="A summary of 2-3 main insights pulled from top search results.",
    agent=researcher
)

# === Crew ===
crew = Crew(
    agents=[researcher],
    tasks=[search_task],
    verbose=True,
    planning=True
)

# === Run ===
print("\n--- Starting Web Research Crew ---\n")
crew.kickoff()
print("\n--- Done ---")
