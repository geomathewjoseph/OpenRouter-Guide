#!/usr/bin/env python3
"""
Exercise 3: Custom Chat Application
Goal: Build a simple interactive chat application

Instructions:
1. Run this script: python exercise_3.py
2. Start chatting with the AI
3. Type 'quit' or 'exit' to end the conversation
4. Try different models by changing the model variable
5. Experiment with system prompts to change the AI's personality
"""

import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class OpenRouterChat:
    def __init__(self, model="openai/gpt-3.5-turbo", system_prompt=None):
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        self.model = model
        self.conversation_history = []
        
        # Add system prompt if provided
        if system_prompt:
            self.conversation_history.append({
                "role": "system",
                "content": system_prompt
            })
    
    def send_message(self, message):
        """Send a message and get a response"""
        # Add user message to conversation
        self.conversation_history.append({
            "role": "user",
            "content": message
        })
        
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": self.conversation_history
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result['choices'][0]['message']['content']
                
                # Add AI response to conversation
                self.conversation_history.append({
                    "role": "assistant",
                    "content": ai_response
                })
                
                return ai_response
            else:
                return f"Error: {response.status_code} - {response.text}"
                
        except requests.exceptions.RequestException as e:
            return f"Network error: {e}"
    
    def get_conversation_summary(self):
        """Get a summary of the conversation"""
        user_messages = [msg for msg in self.conversation_history if msg["role"] == "user"]
        ai_messages = [msg for msg in self.conversation_history if msg["role"] == "assistant"]
        
        return {
            "total_messages": len(self.conversation_history),
            "user_messages": len(user_messages),
            "ai_messages": len(ai_messages),
            "model": self.model
        }

def main():
    print("🎯 Exercise 3: Custom Chat Application")
    print("=" * 50)
    
    # Check for API key
    if not os.getenv('OPENROUTER_API_KEY'):
        print("❌ Error: OPENROUTER_API_KEY not found!")
        return
    
    # Choose your model and personality
    print("🤖 Available models:")
    print("   1. openai/gpt-3.5-turbo (default)")
    print("   2. anthropic/claude-3-haiku")
    print("   3. meta-llama/llama-3.1-8b-instruct")
    
    model_choice = input("\nChoose a model (1-3) or press Enter for default: ").strip()
    
    model_map = {
        "1": "openai/gpt-3.5-turbo",
        "2": "anthropic/claude-3-haiku",
        "3": "meta-llama/llama-3.1-8b-instruct"
    }
    
    selected_model = model_map.get(model_choice, "openai/gpt-3.5-turbo")
    
    # Choose personality
    print("\n🎭 Choose AI personality:")
    print("   1. Helpful Assistant (default)")
    print("   2. Creative Writer")
    print("   3. Technical Expert")
    print("   4. Friendly Chatbot")
    
    personality_choice = input("Choose personality (1-4) or press Enter for default: ").strip()
    
    personality_map = {
        "1": "You are a helpful, knowledgeable, and friendly AI assistant.",
        "2": "You are a creative and imaginative AI that loves to write stories, poems, and creative content.",
        "3": "You are a technical expert who provides detailed, accurate information about technology and programming.",
        "4": "You are a fun, casual, and entertaining AI chatbot that loves to chat and make people smile."
    }
    
    system_prompt = personality_map.get(personality_choice, personality_map["1"])
    
    # Initialize chat
    chat = OpenRouterChat(model=selected_model, system_prompt=system_prompt)
    
    print(f"\n✅ Chat initialized with {selected_model}")
    print(f"🎭 Personality: {system_prompt}")
    print("\n💬 Start chatting! (Type 'quit' or 'exit' to end)")
    print("=" * 50)
    
    # Chat loop
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                break
            
            # Skip empty messages
            if not user_input:
                continue
            
            # Get AI response
            print("🤖 AI: ", end="", flush=True)
            response = chat.send_message(user_input)
            print(response)
            
        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted by user")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
    
    # Show conversation summary
    summary = chat.get_conversation_summary()
    print("\n" + "=" * 50)
    print("📊 CONVERSATION SUMMARY")
    print("=" * 50)
    print(f"🤖 Model: {summary['model']}")
    print(f"💬 Total messages: {summary['total_messages']}")
    print(f"👤 Your messages: {summary['user_messages']}")
    print(f"🤖 AI responses: {summary['ai_messages']}")
    
    print("\n🎉 Exercise 3 Complete!")
    print("\n💡 What you learned:")
    print("   - How to maintain conversation history")
    print("   - How to add system prompts for personality")
    print("   - How to build an interactive chat interface")
    print("   - How to handle user input and errors")
    
    print("\n🔧 Try these modifications:")
    print("   1. Add conversation saving/loading")
    print("   2. Implement different chat modes")
    print("   3. Add message timestamps")
    print("   4. Create a web interface")
    print("   5. Add conversation export functionality")

if __name__ == "__main__":
    main()
