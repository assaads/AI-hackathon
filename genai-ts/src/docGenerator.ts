import { promises as fs } from 'fs';
import path from 'path';
import { Documentation } from './types';

export class DocGenerator {
  async generateDocs(documentation: Documentation, outputPath: string): Promise<void> {
    await fs.mkdir(outputPath, { recursive: true });

    // Generate README.md
    await fs.writeFile(path.join(outputPath, 'README.md'), documentation.readme);

    // Generate API documentation
    for (const doc of documentation.apiDocumentation) {
      await fs.writeFile(path.join(outputPath, `API_${Date.now()}.md`), doc);
    }
  }
}