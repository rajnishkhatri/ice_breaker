"""
Example of using Mistral with LangChain

This script shows how to use the Mistral model through Ollama with LangChain.
Mistral is a powerful open-source language model with excellent reasoning capabilities.

To use this script:
1. Make sure Ollama is installed and running locally
2. Run 'ollama pull mistral' in the terminal
3. Run this script to see the Mistral model in action
"""

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM, ChatOllama

load_dotenv()

def main():
    print("Mistral with LangChain Example")
    print("-----------------------------")
    
    # Example 1: Using OllamaLLM (better for completions)
    print("Example 1: Using OllamaLLM with Mistral")
    llm = OllamaLLM(model="mistral")
    
    prompt_template = """
    You are an expert data scientist. Please explain the following concept in simple terms:
    
    Concept: {concept}
    
    Explanation:
    """
    
    prompt = PromptTemplate.from_template(prompt_template)
    chain = prompt | llm
    
    concept = "Random Forest algorithm"
    print(f"Asking about: {concept}")
    print("\nGenerating response...")
    
    response = chain.invoke({"concept": concept})
    print("\nResponse from Mistral:")
    print(response)
    
    # Example 2: Using ChatOllama (better for chat-like interactions)
    print("\n\nExample 2: Using ChatOllama with Mistral")
    chat_model = ChatOllama(model="mistral", temperature=0.7)
    
    chat_template = """
    You are a helpful career advisor. The user is asking for advice about their career path.
    
    User's question: {question}
    
    Your advice:
    """
    
    chat_prompt = PromptTemplate.from_template(chat_template)
    chat_chain = chat_prompt | chat_model
    
    career_question = "I'm considering a career switch from marketing to data science. What steps should I take?"
    print(f"Career question: {career_question}")
    print("\nGenerating advice...")
    
    chat_response = chat_chain.invoke({"question": career_question})
    print("\nCareer advice from Mistral:")
    print(chat_response.content)

if __name__ == "__main__":
    main() 