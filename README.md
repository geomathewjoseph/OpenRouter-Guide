
# 🤖 OpenRouter Workshop
*A 2-hour hands-on introduction to AI API integration*

> **⏱️ Perfect for beginners** | **✨ Easy-to-follow examples** | **🚀 Build in minutes**

---

## 🎯 What is OpenRouter?

OpenRouter is a unified API that lets you connect to multiple AI models (like GPT-4, Claude, Llama) through a single interface. Think of it as a "universal remote" for AI models! 

**Key benefits:**
- 🔌 **One API key** for 100+ models
- 💰 **Cost comparison** across different providers
- ⚡ **Automatic failover** if a model is busy
- 📊 **Usage analytics** and monitoring

---

## 🚀 Quick Start

### Prerequisites
- 📧 OpenRouter account ([sign up here](https://openrouter.com/))
- 🔑 API key from OpenRouter dashboard
- 💻 Basic Python knowledge
- 🐍 Python 3.7+ installed

### Installation
```bash
pip install requests
# or
pip install openrouter
```

---

## 💡 Sample Code Snippets

### 1. Basic Chat Completion
```python
import requests

API_KEY = "enter your api"
url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

messages = [{"role": "system", "content": "You are a helpful chatbot."}]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = requests.post(url, headers=headers, json={
        "model": "x-ai/grok-4-fast:free",  # can change model here
        "messages": messages
    })

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        print("Bot:", reply)
        messages.append({"role": "assistant", "content": reply})
    else:
        print("Error:", response.status_code, response.text)
```

### 2. Streaming Response
```python
# See full example in: examples/streaming_chat.py
```

### 3. Multiple Models Comparison
```python
# Check: examples/model_comparison.py
```

---

## 🛠️ Hands-On Exercises

### Exercise 1: Your First AI Call (5 minutes)
**Task**: Modify the basic chat example to ask about your favorite hobby.

**Goal**: Get comfortable with the API structure.

### Exercise 2: Model Explorer (10 minutes)
**Task**: Try the same prompt with 3 different models and compare responses.

**Goal**: Understand model differences.

### Exercise 3: Build a Simple Q&A Bot (15 minutes)
**Task**: Create a continuous conversation loop.

**Goal**: Practice handling conversation history.

---

## 📁 Project Structure
```
workshop/
├── examples/          # 📚 Complete code samples
│   ├── basic_chat.py
│   ├── streaming_chat.py
│   └── model_comparison.py
├── exercises/         # 🏋️ Starter files for exercises
│   ├── exercise1.py
│   ├── exercise2.py
│   └── exercise3.py
└── solutions/         # ✅ Exercise solutions
```

---

## 🔗 Resources & Links

### Official Documentation
- [OpenRouter Docs](https://openrouter.ai/docs) 📖
- [API Reference](https://openrouter.ai/docs/api-reference) 🔧
- [Model List](https://openrouter.ai/models) 🎯

### Helpful Tutorials
- [Quick Start Guide](https://openrouter.ai/docs/quick-start) 🚀
- [Authentication Guide](https://openrouter.ai/docs/auth) 🔐

### Community
- [OpenRouter Discord](https://discord.gg/openrouter) 💬
- [GitHub Issues](https://github.com/openrouter/api/issues) 🐛

---

## 💡 Tips & Tricks

### Cost Optimization
- 💰 Start with smaller models for testing
- 📊 Use `usage` field in responses to track costs
- 🔍 Compare prices per model in the dashboard

### Best Practices
- ⚡ Use streaming for better user experience
- 🔄 Implement retry logic for rate limits
- 📝 Always handle API errors gracefully

### Debugging
- 🐛 Check the `X-Request-ID` header for support
- 📋 Log full responses during development
- 🔍 Use the playground for quick tests

---

## 🎯 Next Steps After Workshop

### Project Ideas
- 🤖 Build a personal AI assistant
- 📧 Create an email responder
- 💬 Make a chatbot for your website
- 📊 Analyze documents or data

### Advanced Topics to Explore
- 🔌 Function calling
- 📝 Fine-tuning models
- 🎯 Custom model routing
- 📈 Performance optimization

---

## 🤝 How to Contribute

We welcome improvements! Here's how:

### 🐛 Report Issues
Found a bug or have a suggestion? [Create an issue](https://github.com/your-repo/issues).

### 💡 Add Content
1. Fork this repository
2. Create a branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a pull request

### 📚 Improve Documentation
- Fix typos or clarify instructions
- Add more examples or exercises
- Translate to other languages

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ❓ Getting Help

Stuck? Here's how to get assistance:
1. Check the [examples folder](/examples) 📁
2. Look at [exercise solutions](/solutions) ✅  
3. Ask in the [Discord community](https://discord.gg/openrouter) 💬
4. Create a [GitHub issue](https://github.com/your-repo/issues) 🐛

---

**Happy coding! 🎉 Build something amazing with OpenRouter!**

