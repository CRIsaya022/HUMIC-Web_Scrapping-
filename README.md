# Educational Resource Search Tool

A Python-based tool that helps find the best educational resources across various learning platforms. It uses Brave Search API and CrewAI to discover courses, tutorials, and learning materials tailored to your experience level.

## Features

- Experience level-based search (Beginner/Intermediate/Advanced)
- Learning goal customization (career, hobby, professional development, etc.)
- Focuses on educational content from reputable learning platforms
- Smart search prioritizing content aligned with your goals
- Returns top 15 most relevant educational resources
- Automatically saves results in JSON format with timestamps
- Clean and modular code structure

## Prerequisites

- Python 3.x
- Required API Keys:
  - OpenAI API Key
  - Brave Search API Key (Get it from [Brave Search API](https://api.search.brave.com/))

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Web\ Scrapping\ Demo
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install required packages:
```bash
pip install crewai crewai-tools
```

## Configuration

Before running the tool, you need to set up your API keys. Open `scrapping.py` and update the following environment variables:

```python
os.environ['OPENAI_API_KEY'] = "your-openai-api-key"
os.environ['BRAVE_API_KEY'] = 'your-brave-search-api-key'
```

## Usage

1. Run the script:
```bash
python scrapping.py
```

2. Follow the prompts:
```
Enter a topic to research: Python Programming

Select your experience level:
1. Beginner
2. Intermediate
3. Advanced
Enter number (1-3): 2

What's your learning goal? (e.g., 'start a career', 'hobby', 'professional development')
Enter your goal: professional development
```

3. The tool will:
   - Search for educational resources about your topic
   - Filter results based on your experience level
   - Customize content based on your learning goals
   - Focus on structured learning content (courses, tutorials, etc.)
   - Extract the top 15 most relevant resources
   - Save them in a JSON file in the `results` directory

## Output Format

Results are saved in JSON files with the following structure:
```json
{
  "topic": "Python Programming",
  "timestamp": "2025-04-19T11:45:37-04:00",
  "results": [
    {
      "title": "Intermediate Python Programming Course",
      "url": "https://example.com/course/python-intermediate",
      "description": "Comprehensive intermediate-level Python course covering advanced concepts, best practices, and real-world applications."
    },
    ...
  ]
}
```

Files are saved in the `results` directory with the naming format:
`YYYYMMDD_HHMMSS_Topic_Name.json`

Each result is carefully selected to match:
- Your specified experience level
- Educational content focus
- Structured learning material
- Reputable sources

## Code Structure

- `scrapping.py`: Main script containing all functionality
  - `setup_environment()`: Sets up API keys
  - `create_search_agent()`: Creates the search agent
  - `create_search_task()`: Creates a search task for a topic
  - `parse_results()`: Parses raw results into structured data
  - `save_results()`: Saves results to a JSON file
  - `main()`: Orchestrates the entire process

## Error Handling

The tool includes basic error handling for:
- Missing API keys
- Failed API requests
- Invalid search results format
- File system operations

## Limitations

- Maximum of 5 results per search
- Requires valid API keys for both OpenAI and Brave Search
- Results quality depends on Brave Search API and topic specificity

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
