# Ice Breaker

An AI-powered tool that generates personalized ice breakers and conversation starters by analyzing a person's LinkedIn and Twitter profiles.

![Project Logo](https://github.com/emarco177/ice_breaker/blob/main/static/demo.gif)

## 📋 Overview

Ice Breaker uses LangChain and large language models to:
1. Scrape a person's LinkedIn and Twitter data
2. Analyze their professional background and interests
3. Generate personalized summaries, topics of interest, and ice breakers
4. Provide conversation starters that help you connect with them

Perfect for networking events, job interviews, or anytime you need to make a meaningful connection with someone new.

## ✨ Features

- **LinkedIn Profile Analysis**: Scrapes and analyzes professional background
- **Twitter Analysis**: Examines tweets to identify interests and topics
- **AI-Powered Summaries**: Creates concise professional summaries
- **Personalized Ice Breakers**: Generates custom conversation starters
- **Web Interface**: Easy-to-use UI for entering names and viewing results
- **Multiple LLM Support**: Works with OpenAI models or local Ollama models

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- API keys for OpenAI, LinkedIn scraping service, and Twitter (optional)
- Ollama (optional, for local models)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ice_breaker.git
cd ice_breaker
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your API keys (see Environment Variables section)

## 🔑 Environment Variables

Create a `.env` file in the project root with the following variables:

```
OPENAI_API_KEY="your-openai-api-key"
SCRAPIN_API_KEY="your-scrapin-api-key"
TAVILY_API_KEY="your-tavily-api-key"
TWITTER_API_KEY="your-twitter-api-key"
TWITTER_API_KEY_SECRET="your-twitter-api-secret"
TWITTER_BEARER_TOKEN="your-twitter-bearer-token"
TWITTER_ACCESS_TOKEN="your-twitter-access-token"
TWITTER_ACCESS_TOKEN_SECRET="your-twitter-access-token-secret"
LANGCHAIN_API_KEY="your-langchain-api-key"  # Optional, for tracing
LANGCHAIN_TRACING_V2="true"  # Optional
LANGCHAIN_PROJECT="Ice Breaker"  # Optional
```

> **Note**: For LinkedIn scraping, you can get API keys from [Scrapin.io](https://www.scrapin.io/).
> 
> **Important**: If you enable LangChain tracing, you must provide a valid LangSmith API key.

## 🚀 Usage

### Web Interface

1. Start the web server:
```bash
python app.py
```

2. Open your browser to `http://localhost:5001`

3. Enter the name of the person you want to generate ice breakers for and submit

### Command Line

Run the ice breaker script directly:
```bash
python ice_breaker.py
```

## 🧠 Using Different Language Models

### OpenAI (Default)

The project uses OpenAI's models by default. Make sure your `OPENAI_API_KEY` is in the `.env` file.

### Local Models with Ollama

You can use local models through Ollama:

1. Install Ollama from [ollama.ai](https://ollama.ai)
2. Pull the models you want to use:
```bash
ollama pull mistral
ollama pull llama2
```

3. Edit third_parties/prompt.py to use Ollama:
```python
# Comment out the OpenAI option
# llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# Uncomment the Ollama option
llm = ChatOllama(model="mistral")  # or "llama2"
```

## 📁 Project Structure

- **agents/**: Contains LangChain agents for LinkedIn and Twitter lookup
- **chains/**: Custom LangChain processing chains
- **output_parsers/**: Parsers for structured outputs from LLMs
- **third_parties/**: Integration with external services (LinkedIn, Twitter)
- **templates/**: HTML templates for the web interface
- **static/**: Static assets for the web interface
- **app.py**: Web application using Flask
- **ice_breaker.py**: Main library for generating ice breakers

## ⚙️ Testing

Run the tests with:
```bash
pytest .
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

