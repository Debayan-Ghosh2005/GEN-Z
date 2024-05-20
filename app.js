import { GoogleGenerativeAI } from "@google/generative-ai";
import dotenv from 'dotenv';

// Load environment variables from .env file
dotenv.config();

// 1. Configuration
const apiKey = process.env.GOOGLE_API_KEY;  // Ensure your .env file has GOOGLE_API_KEY
const genAI = new GoogleGenerativeAI(apiKey);

// Define generation configuration
const generationConfig = {
    temperature: 0.9,
    top_p: 1,
    top_k: 1,
    max_output_tokens: 100 // Specify a reasonable number for tokens
};

// 2. Generate Content
async function generateContent() {
    try {
        const prompt = "create a Meal plan for today";
        const result = await genAI.generateText({
            model: "gemini-pro",
            prompt: prompt,
            ...generationConfig
        });
        const response = result.text;
        console.log(response);
    } catch (error) {
        console.error('Error generating content:', error);
    }
}

// Run the function
generateContent();
