import axios from 'axios';

// Mock function to simulate sending requests to OpenAI API
export async function sendOpenAIRequest(prompt: string): Promise<string> {
  // In a real application, replace this with actual API request logic.
  console.log(`Sending request to OpenAI with prompt: ${prompt}`);
  return Promise.resolve(`This is a mocked response for the prompt: ${prompt}`);
}