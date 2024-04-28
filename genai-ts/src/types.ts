export interface OpenAIResponse {
  choices: Array<{
    text: string;
  }>;
}

export interface Documentation {
  readme: string;
  apiDocumentation: string[];
}