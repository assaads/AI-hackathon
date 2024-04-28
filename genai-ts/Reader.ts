import { promisify } from "util";
import glob from "glob";
import { readFile } from "fs";

const globPromise = promisify(glob);
const readFilePromise = promisify(readFile);

export class FileReader {
  async readFiles(directoryPath: string): Promise<{ path: string; content: string; extension: string }[]> {
    const files = await globPromise(`${directoryPath}/**/*.*`, { nodir: true });
    return Promise.all(
      files.map(async (filePath) => {
        const content = await readFilePromise(filePath, { encoding: "utf8" });
        return {
          path: filePath,
          content,
          extension: filePath.split('.').pop() || ''
        };
      })
    );
  }
}