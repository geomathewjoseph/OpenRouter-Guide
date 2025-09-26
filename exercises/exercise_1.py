#!/usr/bin/env python3
"""
Exercise 1: Your First API Call
Goal: Make your first successful API call to OpenRouter

Instructions:
1. Make sure you have your API key in the .env file
2. Run this script: python exercise_1.py
3. Modify the message and run again
4. Try different models by changing the model parameter
"""

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    print("🎯 Exercise 1: Your First API Call")
    print("=" * 50)
    
    # Get API key from environment
    api_key = os.getenv('OPENROUTER_API_KEY')
    
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found!")
        print("Please add your API key to the .env file:")
        print("OPENROUTER_API_KEY=your_api_key_here")
        return
    
    print("✅ API key found!")
    
    # Your first message to OpenRouter
    message = "Hello! Can you introduce yourself and tell me what you can help with?"
    
    print(f"\n📤 Sending message: {message}")
    
    # Make the API call
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": message}]
            }
        )
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            ai_response = result['choices'][0]['message']['content']
            
            print("✅ Success! Here's the response:")
            print(f"🤖 AI: {ai_response}")
            
            # Show some useful information
            print(f"\n📊 Response Info:")
            print(f"   Model used: {result['model']}")
            print(f"   Tokens used: {result['usage']['total_tokens']}")
            print(f"   Response time: {response.elapsed.total_seconds():.2f} seconds")
            
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    
    print("\n🎉 Exercise 1 Complete!")
    print("\n💡 Try these modifications:")
    print("   1. Change the message to ask something else")
    print("   2. Try a different model like 'anthropic/claude-3-haiku'")
    print("   3. Add more context to your message")

if __name__ == "__main__":
    main()
