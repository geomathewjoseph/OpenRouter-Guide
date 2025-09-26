#!/usr/bin/env python3
"""
Exercise 2: Model Comparison
Goal: Compare responses from different AI models

Instructions:
1. Run this script: python exercise_2.py
2. Observe the differences in response style and quality
3. Try adding your own prompt by modifying the test_prompt variable
4. Experiment with different models in the models list
"""

import requests
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_ai_response(message, model, api_key):
    """Get response from a specific model"""
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": message}]
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            return {
                "success": True,
                "content": result['choices'][0]['message']['content'],
                "tokens": result['usage']['total_tokens'],
                "model": result['model']
            }
        else:
            return {
                "success": False,
                "error": f"HTTP {response.status_code}: {response.text}"
            }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e)
        }

def main():
    print("🎯 Exercise 2: Model Comparison")
    print("=" * 50)
    
    # Get API key
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found!")
        return
    
    # Test prompt - feel free to modify this!
    test_prompt = "Explain quantum computing in simple terms that a 10-year-old could understand."
    
    # Models to compare - you can add or remove models here
    models = [
        "openai/gpt-3.5-turbo",
        "anthropic/claude-3-haiku",
        "meta-llama/llama-3.1-8b-instruct"
    ]
    
    print(f"📝 Test Prompt: {test_prompt}")
    print(f"🔍 Comparing {len(models)} models...")
    print("\n" + "=" * 80)
    
    results = []
    
    for i, model in enumerate(models, 1):
        print(f"\n🤖 Model {i}: {model}")
        print("-" * 60)
        
        start_time = time.time()
        result = get_ai_response(test_prompt, model, api_key)
        end_time = time.time()
        
        if result["success"]:
            print(f"✅ Response ({end_time - start_time:.2f}s, {result['tokens']} tokens):")
            print(f"   {result['content']}")
            results.append({
                "model": model,
                "response": result['content'],
                "tokens": result['tokens'],
                "time": end_time - start_time
            })
        else:
            print(f"❌ Error: {result['error']}")
    
    # Summary comparison
    if results:
        print("\n" + "=" * 80)
        print("📊 COMPARISON SUMMARY")
        print("=" * 80)
        
        for result in results:
            print(f"\n🤖 {result['model']}:")
            print(f"   ⏱️  Time: {result['time']:.2f}s")
            print(f"   🎯 Tokens: {result['tokens']}")
            print(f"   📝 Response length: {len(result['response'])} characters")
    
    print("\n🎉 Exercise 2 Complete!")
    print("\n💡 Observations:")
    print("   - Which model was fastest?")
    print("   - Which response was most detailed?")
    print("   - Which explanation was easiest to understand?")
    print("   - How do the token costs compare?")
    
    print("\n🔧 Try these modifications:")
    print("   1. Change the test_prompt to ask something else")
    print("   2. Add more models to the models list")
    print("   3. Try the same prompt with different models")
    print("   4. Compare creative vs factual responses")

if __name__ == "__main__":
    main()
