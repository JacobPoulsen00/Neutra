require('dotenv').config({ path: __dirname + '/../.env' });
const pythonPath = process.env.PYTHON_PATH;

const express = require('express');
const { exec } = require('child_process');

const app = express();
const PORT = 5000; // Changed port to avoid conflict with React's dev server

const cors = require('cors');
app.use(cors({
    origin: 'http://localhost:3000', 
    methods: ['GET', 'POST'],
    allowedHeaders: ['Content-Type', 'Authorization']
  }));

app.use(express.json());

app.post('/analyze', (req, res) => {
    const newsURL = req.body.url;
    
    // Check if url exists in request body
    if (!newsURL) {
        return res.status(400).send({ error: 'URL is required' });
    }
    
    // Debug
    console.log("Running script");
    
    // Run your Python script
     const pythonScriptPath = __dirname + '/../utils/analyze_news.py';
     const cmd = `"${pythonPath}" ${pythonScriptPath} "${newsURL}"`;
     exec(cmd, (error, stdout, stderr) => {
         if (error) {
             console.error(`exec error: ${error}`);
             return res.status(500).send({ error: 'Failed to analyze news' });
         }
 
         const result = stdout;  
 
         return res.send({ data: result });
     });
 });

 app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});