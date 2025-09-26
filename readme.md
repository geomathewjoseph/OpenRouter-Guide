# 🚀 OpenRouter Workshop Guide

> A beginner-friendly introduction to OpenRouter - your gateway to multiple AI models through one simple API

## 📖 What is OpenRouter?

OpenRouter is a unified API that gives you access to multiple AI models (GPT-4, Claude, Llama, and more) through a single endpoint. Think of it as a "router" that lets you easily switch between different AI providers without changing your code structure.

**Why use OpenRouter?**
- 🎯 One API for many models
- 💰 Transparent pricing
- 🔄 Easy model switching
- 📊 Built-in analytics

---

## 🛠️ Prerequisites

Before we start, make sure you have:

- [ ] **Node.js** (v14 or higher) installed
- [ ] **Text editor** (VS Code recommended)
- [ ] **OpenRouter account** - [Sign up here](https://openrouter.ai/)
- [ ] **Basic JavaScript knowledge** (variables, functions, async/await)
- [ ] **OpenRouter API Key** - Get it from your [dashboard](https://openrouter.ai/keys)

---

## 🏁 Quick Start

### 1. Installation

```bash
npm install openai  # OpenRouter uses OpenAI-compatible API
```

### 2. Basic Setup

```javascript
// basic-example.js
const OpenAI = require('openai');

const openai = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: process.env.OPENROUTER_API_KEY,
});

async function simpleChat() {
  const completion = await openai.chat.completions.create({
    model: "meta-llama/llama-3.1-8b-instruct:free",
    messages: [
      { role: "user", content: "Hello! What's the weather like on Mars?" }
    ],
  });

  console.log(completion.choices[0].message.content);
}

simpleChat();
```

### 3. Environment Setup

Create a `.env` file:
```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## 💻 Code Examples

### Example 1: Simple Chat
📁 **File**: [`examples/simple-chat.js`](./examples/simple-chat.js)

```javascript
// Simple question-answer example
const response = await openai.chat.completions.create({
  model: "meta-llama/llama-3.1-8b-instruct:free",
  messages: [{ role: "user", content: "Explain quantum computing in one sentence" }],
});
```

### Example 2: Model Comparison
📁 **File**: [`examples/model-comparison.js`](./examples/model-comparison.js)

```javascript
// Compare responses from different models
const models = [
  "meta-llama/llama-3.1-8b-instruct:free",
  "microsoft/phi-3-mini-128k-instruct:free"
];

for (const model of models) {
  const response = await openai.chat.completions.create({
    model: model,
    messages: [{ role: "user", content: "Write a haiku about coffee" }],
  });
  console.log(`${model}:`, response.choices[0].message.content);
}
```

### Example 3: Streaming Responses
📁 **File**: [`examples/streaming.js`](./examples/streaming.js)

```javascript
// Stream responses for real-time output
const stream = await openai.chat.completions.create({
  model: "meta-llama/llama-3.1-8b-instruct:free",
  messages: [{ role: "user", content: "Tell me a short story" }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || '');
}
```

---

## 🎯 Hands-on Exercises

### Exercise 1: Your First API Call (5 mins)
**Goal**: Make your first successful API call to OpenRouter

1. Copy the basic setup code above
2. Replace `your_api_key_here` with your actual API key
3. Run the script: `node basic-example.js`
4. ✅ Success: You should see a response about Mars weather!

**📁 Starter file**: [`exercises/exercise-1.js`](./exercises/exercise-1.js)

### Exercise 2: Model Explorer (10 mins)
**Goal**: Try 3 different free models and compare their responses

1. Use the model comparison example
2. Ask the same question to these models:
   - `meta-llama/llama-3.1-8b-instruct:free`
   - `microsoft/phi-3-mini-128k-instruct:free`
   - `google/gemma-2-9b-it:free`
3. Compare the different writing styles

**📁 Starter file**: [`exercises/exercise-2.js`](./exercises/exercise-2.js)

### Exercise 3: Build a Simple Chatbot (15 mins)
**Goal**: Create a basic command-line chatbot

1. Create a loop that accepts user input
2. Send input to OpenRouter
3. Display the AI response
4. Allow users to type 'exit' to quit

**📁 Starter file**: [`exercises/exercise-3.js`](./exercises/exercise-3.js)

---

## 💡 Tips & Tricks

### 🔥 Pro Tips
- **Start with free models** like `llama-3.1-8b-instruct:free` for testing
- **Use environment variables** for API keys (never commit them!)
- **Check token limits** - each model has different context windows
- **Monitor usage** in your OpenRouter dashboard

### 🚨 Common Gotchas
- Missing `await` keyword (async operations!)
- Wrong model names (check [models list](https://openrouter.ai/models))
- API key not loaded from environment
- Network timeouts for long responses

### 🎨 Best Practices
```javascript
// Good: Handle errors properly
try {
  const response = await openai.chat.completions.create({...});
} catch (error) {
  console.error('API Error:', error.message);
}

// Good: Set reasonable timeouts
const openai = new OpenAI({
  baseURL: "https://openrouter.ai/api/v1",
  apiKey: process.env.OPENROUTER_API_KEY,
  timeout: 30000, // 30 seconds
});
```

---

## 🎓 Next Steps

Ready to level up? Here's what to explore next:

- 🔍 **Explore more models**: Try GPT-4, Claude, or specialized models
- 🛠️ **Build a web app**: Integrate with React, Vue, or your favorite framework  
- 📊 **Add prompt engineering**: Learn to craft better prompts
- 🔗 **Function calling**: Make AI interact with external APIs
- 🎯 **Fine-tuning**: Train models on your specific data

**Recommended Next Projects:**
- Build a code review assistant
- Create a creative writing helper
- Make a technical documentation generator

---

## 📚 Resources

### Official Documentation
- 📖 [OpenRouter Docs](https://openrouter.ai/docs)
- 🔧 [API Reference](https://openrouter.ai/docs/api-reference)
- 🤖 [Available Models](https://openrouter.ai/models)
- 💰 [Pricing](https://openrouter.ai/models)

### Helpful Tutorials
- 🎥 [OpenRouter Getting Started Video](https://www.youtube.com/watch?v=example)
- 📝 [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- 🔧 [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)

### Community
- 💬 [OpenRouter Discord](https://discord.gg/openrouter)
- 🐦 [OpenRouter Twitter](https://twitter.com/OpenRouterAI)
- 📧 [Support](mailto:help@openrouter.ai)

---

## 🤝 Contributing

We love contributions! Here's how you can help improve this workshop:

### Ways to Contribute
- 🐛 **Report bugs** - Found something broken? [Open an issue](./issues)
- 💡 **Suggest improvements** - Have ideas? We'd love to hear them!
- 📝 **Add examples** - More code examples are always welcome
- 🎯 **Create exercises** - Help others learn with new hands-on tasks

### Getting Started
1. Fork this repository
2. Create a feature branch: `git checkout -b feature/amazing-example`
3. Make your changes and test them
4. Submit a pull request with a clear description

### Guidelines
- Keep examples simple and well-commented
- Test all code before submitting
- Follow existing naming conventions
- Update README if adding new sections

---

## 📄 License

This workshop guide is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 OpenRouter Workshop

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND...
```

**📁 Full license**: [`LICENSE`](./LICENSE)

---

## 🙋‍♂️ Need Help?

- 🔍 **Check the examples** in the `/examples` folder first
- 💬 **Ask questions** in our [Discussions](./discussions) 
- 🐛 **Report issues** using our [Issue Template](./issues/new)
- 📧 **Contact workshop organizers** at workshop@example.com

---

<div align="center">

**Happy coding! 🚀**

*Made with ❤️ for the AI developer community*

[![OpenRouter](https://img.shields.io/badge/OpenRouter-FF6B6B?style=flat&logo=router&logoColor=white)](https://openrouter.ai)
[![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)](https://nodejs.org)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

</div>