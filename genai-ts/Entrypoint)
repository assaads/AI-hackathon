import { FileReader } from "./fileReader";
import { CodeParser } from "./codeParser";
import { APIClient } from "./apiClient";

const main = async () => {
  const fileReader = new FileReader();
  const codeParser = new CodeParser();
  const apiClient = new APIClient("http://api.endpoint.com/upload");

  const files = await fileReader.readFiles("./path/to/codebase");
  const parsedFiles = files.map(file => ({
    ...file,
    content: codeParser.parse(file.content, file.extension)
  }));

  await apiClient.sendCodebaseInfo(parsedFiles);
};

main().catch(console.error);