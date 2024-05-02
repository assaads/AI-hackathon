import axios from 'axios';
import { OpenAIResponse } from './types';

const OPENAI_URL = 'https://api.openai.com/v1/engines/davinci-codex/completions';

export class OpenAIService {
  apiKey: string;

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }

  async generateDocumentation(prompt: string): Promise<OpenAIResponse> {
    try {
      const response = await axios.post(
        OPENAI_URL,
        {
          prompt,
          temperature: 0.5,
          max_tokens: 2048,
          top_p: 1.0,
          frequency_penalty: 0.0,
          presence_penalty: 0.0,
        },
        {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${this.apiKey}`
          }
        }
      );
      return response.data;
    } catch (error) {
      console.error('Error calling OpenAI API:', error);
      throw error;
    }
  }
}