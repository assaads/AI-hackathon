import dotenv from 'dotenv';
import { OpenAIService } from './openaiService';
import { FileReader } from './fileReader';
import { DocGenerator } from './docGenerator';

dotenv.config();

const main = async () => {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) {
    console.error('OpenAI API key is not set.');
    process.exit(1);
  }

  const openAIService = new OpenAIService(apiKey);
  const fileReader = new FileReader();
  const docGenerator = new DocGenerator();

  const sourceFilesContent = await fileReader.readSourceFiles('./src');
  const prompt = sourceFilesContent.join('\n\n');

  const openAIResponse = await openAIService.generateDocumentation(prompt);
  const documentation = {
    readme: openAIResponse.choices[0].text,
    apiDocumentation: openAIResponse.choices.slice(1).map(choice => choice.text),
  };

  await docGenerator.generateDocs(documentation, './docs');
};

main().catch(console.error);