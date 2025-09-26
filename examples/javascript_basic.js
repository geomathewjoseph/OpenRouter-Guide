#!/usr/bin/env node
/**
 * OpenRouter Basic JavaScript Example
 * A simple script demonstrating how to use OpenRouter API with Node.js
 */

const axios = require('axios');
require('dotenv').config();

/**
 * Send a message to OpenRouter and get a response
 * @param {string} message - The message to send to the AI
 * @param {string} model - The model to use (default: gpt-3.5-turbo)
 * @returns {Promise<Object>} The response from OpenRouter API
 */
async function chatWithOpenRouter(message, model = 'openai/gpt-3.5-turbo') {
    const apiKey = process.env.OPENROUTER_API_KEY;
    
    if (!apiKey) {
        throw new Error('OPENROUTER_API_KEY not found in environment variables');
    }
    
    const url = 'https://openrouter.ai/api/v1/chat/completions';
    
    const headers = {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
    };
    
    const data = {
        model: model,
        messages: [
            { role: 'user', content: message }
        ]
    };
    
    try {
        const response = await axios.post(url, data, { headers });
        return response.data;
    } catch (error) {
        console.error('Error making request:', error.response?.data || error.message);
        return null;
    }
}

/**
 * Main function to demonstrate OpenRouter usage
 */
async function main() {
    console.log('🤖 OpenRouter JavaScript Example');
    console.log('='.repeat(40));
    
    // Example 1: Simple chat
    console.log('\n📝 Example 1: Simple Chat');
    const message1 = 'Hello! Can you tell me a fun fact about space?';
    const result1 = await chatWithOpenRouter(message1);
    
    if (result1) {
        const responseText = result1.choices[0].message.content;
        console.log(`User: ${message1}`);
        console.log(`AI: ${responseText}`);
    } else {
        console.log('Failed to get response');
    }
    
    // Example 2: Different model
    console.log('\n🔄 Example 2: Using Different Model');
    const message2 = 'Write a short poem about coding';
    const result2 = await chatWithOpenRouter(message2, 'anthropic/claude-3-haiku');
    
    if (result2) {
        const responseText = result2.choices[0].message.content;
        console.log(`User: ${message2}`);
        console.log(`AI (Claude): ${responseText}`);
    } else {
        console.log('Failed to get response');
    }
    
    // Example 3: Conversation
    console.log('\n💬 Example 3: Multi-turn Conversation');
    const conversation = [
        { role: 'user', content: 'What\'s the capital of France?' },
        { role: 'assistant', content: 'The capital of France is Paris.' },
        { role: 'user', content: 'What\'s the population of that city?' }
    ];
    
    const apiKey = process.env.OPENROUTER_API_KEY;
    if (apiKey) {
        const url = 'https://openrouter.ai/api/v1/chat/completions';
        const headers = {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json'
        };
        const data = {
            model: 'openai/gpt-3.5-turbo',
            messages: conversation
        };
        
        try {
            const response = await axios.post(url, data, { headers });
            const result = response.data;
            const responseText = result.choices[0].message.content;
            console.log('User: What\'s the population of that city?');
            console.log(`AI: ${responseText}`);
        } catch (error) {
            console.error('Error:', error.response?.data || error.message);
        }
    }
}

// Run the main function
if (require.main === module) {
    main().catch(console.error);
}

module.exports = { chatWithOpenRouter };
