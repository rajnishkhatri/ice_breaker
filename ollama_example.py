"""
Example of using Ollama with LangChain

This script shows how to use Ollama as an LLM provider in LangChain.
Ollama allows you to run open-source large language models locally.

To use this script:
1. Make sure Ollama is installed and running locally
2. Run this script to see an example of using an Ollama model with LangChain
"""

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

load_dotenv()

def main():
    print("Ollama with LangChain Example")
    print("-----------------------------")
    
    # Initialize Ollama LLM with the updated class
    # Note: You need to have the model pulled in Ollama first
    # For example: `ollama pull llama2` in the terminal
    llm = OllamaLLM(model="llama2")  # You can change this to any model you've pulled
    
    # Define a prompt template
    prompt_template = """
    You are a helpful assistant. Please respond to the following question:
    
    Question: {question}
    
    Answer:
    """
    
    prompt = PromptTemplate.from_template(prompt_template)
    
    # Create a chain
    chain = prompt | llm
    
    # Example question
    question = "What are some benefits of using open-source LLMs like Llama?"
    
    print(f"Asking: {question}")
    print("\nGenerating response...")
    
    # Invoke the chain
    response = chain.invoke({"question": question})
    
    print("\nResponse:")
    print(response)

if __name__ == "__main__":
    main() 