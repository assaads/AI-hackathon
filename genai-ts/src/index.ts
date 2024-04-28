import { generateDocumentation } from './documentationGenerator';
import { sendOpenAIRequest } from './openAIAdapter';

async function main() {
  const documentationStructure = generateDocumentation();
  console.log('Generated Documentation Structure:', documentationStructure);

  // Mock sending a request to OpenAI for documentation content
  const exampleFunctionDescription = await sendOpenAIRequest('Describe a function that adds two numbers.');
  console.log('OpenAI API Response:', exampleFunctionDescription);
}

main().catch(console.error);