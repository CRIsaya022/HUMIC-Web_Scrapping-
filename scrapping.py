from crewai import Agent, Task, Crew
from crewai_tools import BraveSearchTool
import os
import json
from datetime import datetime

def setup_environment():
    """Set up environment variables for API keys"""
    os.environ['OPENAI_API_KEY'] = "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"
    os.environ['BRAVE_API_KEY'] = 'BSAATTtj-6SVlEyF4VuRyhKQ7NjbMwI'

def create_search_agent():
    """Create and return a web search agent"""
    return Agent(
        role='Self Learning Assistant Web Scraper',
        goal='Search the web and extract detailed information from top online learning and educational sources e.g Coursera, edX, Udemy, etc.',
        backstory='An AI tool specialized in web search and data extraction.',
        tools=[BraveSearchTool()],
        verbose=True
    )

def get_user_input():
    """Get topic, experience level and learning goal from user"""
    topic = input("Enter a topic to research: ")
    
    print("\nSelect your experience level:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")
    while True:
        try:
            level = int(input("Enter number (1-3): "))
            if 1 <= level <= 3:
                experience_level = ['beginner', 'intermediate', 'advanced'][level-1]
                break
            print("Please enter a number between 1 and 3")
        except ValueError:
            print("Please enter a valid number")
    
    print("\nWhat's your learning goal? (e.g., 'start a career', 'hobby', 'professional development')")
    goal = input("Enter your goal: ")
    
    return topic, experience_level, goal

def create_search_task(agent, topic, experience_level, goal):
    """Create a search task for the given topic and experience level"""
    # Example educational platforms for reference
    example_platforms = [
        'coursera.org', 'edx.org', 'udemy.com', 'pluralsight.com',
        'linkedin.com/learning', 'codecademy.com', 'udacity.com',
        'skillshare.com', 'masterclass.com', 'brilliant.org',
        'khanacademy.org', 'freecodecamp.org', 'youtube.com'
    ]

    
    # Create a more general search query
    search_query = f"""
    Search for {experience_level} level educational content about '{topic}' that aligns with the goal of '{goal}'.
    Look for high-quality courses, tutorials, and learning resources.
    
    Some example educational platforms to consider (but don't limit to these):
    {', '.join(example_platforms)}
    
    Focus on finding the best educational resources regardless of platform.
    Prioritize content that:
    1. Matches the {experience_level} skill level
    2. Provides structured learning content
    3. Comes from reputable educational sources
    4. Is specifically designed for learning '{topic}' and achieving the goal of '{goal}'
    
    Return the top 15 most relevant educational resources.
    Format each result exactly as follows:
    
    Title: [title]
    URL: [url]
    Description: [description]
    
    Repeat this format for each result, separating them with a blank line.
    """
    
    return Task(
        description=search_query,
        expected_output="Fifteen educational resource results, each formatted with Title:, URL:, and Description: on separate lines, separated by blank lines.",
        agent=agent
    )

def parse_results(raw_results):
    """Parse the raw results into structured data"""
    results_list = []
    current_result = {}
    
    for line in raw_results.split('\n'):
        line = line.strip()
        if line.startswith('Title:'):
            if current_result and len(current_result) == 3:
                results_list.append(current_result)
                current_result = {}
            current_result['title'] = line.replace('Title:', '').strip()
        elif line.startswith('URL:'):
            current_result['url'] = line.replace('URL:', '').strip()
        elif line.startswith('Description:') or line.startswith('Content:'):
            current_result['description'] = line.replace('Description:', '').replace('Content:', '').strip()
    
    if current_result and len(current_result) == 3:
        results_list.append(current_result)
    
    return results_list[:15]  # Return top 15 results for better resource selection

def save_results(topic, results):
    """Save results to a JSON file"""
    output = {
        "topic": topic,
        "timestamp": datetime.now().isoformat(),
        "results": results
    }
    
    os.makedirs('results', exist_ok=True)
    filename = f'results/{datetime.now().strftime("%Y%m%d_%H%M%S")}_{topic.replace(" ", "_")}.json'
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    return filename

def main():
    """Main function to run the web research tool"""
    setup_environment()
    
    # Get user input
    topic, experience_level, goal = get_user_input()
    
    print("\n--- Starting Web Research Crew ---\n")
    
    # Create and run crew
    agent = create_search_agent()
    task = create_search_task(agent, topic, experience_level, goal)
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )
    result = crew.kickoff()
    
    # Process and save results
    results = parse_results(str(result))
    filename = save_results(topic, results)
    
    print(f"\nResults saved to: {filename}")
    print("\n--- Done ---")

if __name__ == "__main__":
    main()
