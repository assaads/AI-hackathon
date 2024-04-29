import express from 'express';
import bodyParser from 'body-parser';
import { processSourceCode } from './sourceCodeProcessor';

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/process', (req, res) => {
  const { sourceCode } = req.body;
  const result = processSourceCode(sourceCode);
  res.json(result);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});