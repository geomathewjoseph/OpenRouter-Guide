#!/usr/bin/env python3
"""
OpenRouter Basic Python Example
A simple script demonstrating how to use OpenRouter API with Python
"""

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def chat_with_openrouter(message, model="openai/gpt-3.5-turbo"):
    """
    Send a message to OpenRouter and get a response
    
    Args:
        message (str): The message to send to the AI
        model (str): The model to use (default: gpt-3.5-turbo)
    
    Returns:
        dict: The response from OpenRouter API
    """
    api_key = os.getenv('OPENROUTER_API_KEY')
    
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")
    
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": message}
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

def main():
    """Main function to demonstrate OpenRouter usage"""
    print("🤖 OpenRouter Python Example")
    print("=" * 40)
    
    # Example 1: Simple chat
    print("\n📝 Example 1: Simple Chat")
    message = "Hello! Can you tell me a fun fact about space?"
    result = chat_with_openrouter(message)
    
    if result:
        response_text = result['choices'][0]['message']['content']
        print(f"User: {message}")
        print(f"AI: {response_text}")
    else:
        print("Failed to get response")
    
    # Example 2: Different model
    print("\n🔄 Example 2: Using Different Model")
    message = "Write a short poem about coding"
    result = chat_with_openrouter(message, model="anthropic/claude-3-haiku")
    
    if result:
        response_text = result['choices'][0]['message']['content']
        print(f"User: {message}")
        print(f"AI (Claude): {response_text}")
    else:
        print("Failed to get response")
    
    # Example 3: Conversation
    print("\n💬 Example 3: Multi-turn Conversation")
    conversation = [
        {"role": "user", "content": "What's the capital of France?"},
        {"role": "assistant", "content": "The capital of France is Paris."},
        {"role": "user", "content": "What's the population of that city?"}
    ]
    
    api_key = os.getenv('OPENROUTER_API_KEY')
    if api_key:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": conversation
        }
        
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            response_text = result['choices'][0]['message']['content']
            print(f"User: What's the population of that city?")
            print(f"AI: {response_text}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
