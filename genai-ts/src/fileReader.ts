import { promises as fs } from 'fs';
import path from 'path';

export class FileReader {
  async readSourceFiles(directory: string): Promise<string[]> {
    let filesContent: string[] = [];
    const files = await fs.readdir(directory);

    for (const file of files) {
      const filePath = path.join(directory, file);
      const stat = await fs.stat(filePath);

      if (stat.isDirectory()) {
        filesContent = filesContent.concat(await this.readSourceFiles(filePath));
      } else if (stat.isFile()) {
        const content = await fs.readFile(filePath, 'utf8');
        filesContent.push(content);
      }
    }

    return filesContent;
  }
}