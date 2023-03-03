import express from "express";
import { PythonShell } from 'python-shell'
import cors from 'cors'

const app = express()
let option = {
    mode: 'text',
    pythonOptions: ['-u'],
    scriptPath: './ImageGenerator',
};
let defaultImage = "https://firebasestorage.googleapis.com/v0/b/greenieverse.appspot.com/o/%2F%2F_test.png?alt=media&token=e7c691e6-f1be-4a95-bc97-3bae7195ef57";


app.use(cors())

// Home directory 
app.get('/', (req, res) => {
    res.send("Hello world again");
    return;
})

app.get('/image', async (req, res) => {
    console.log(req.query.prompt);
    if (!req.query.prompt) {
        res.send(defaultImage)
        return;
    }
    let prompt = req.query.prompt;
    option.args = [prompt];

    try {
        await PythonShell.run("text2image.py", option).then((message) => {
            res.send(message[0])
            return;
        })
    
    }
    catch (err) {
        console.log(err);
        res.send(defaultImage);
        return;
    }
})

let port = 5000;
app.listen(port, () => {
    console.log("Server is listening");
})