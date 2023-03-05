<script>

import axios from 'axios';

let prompt;
let answer;

async function sendMessage(prompt) {
  const response = await axios.post('https://api.openai.com/v1/engines/text-davinci-003/completions', {
    prompt: prompt,
    max_tokens: 50,
    temperature: 0.5,
    n: 1,



  }, {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer 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'
    }
  });
  console.log(response.data.choices[0].text);
  answer = response.data.choices[0].text;
  return response.data.choices[0].text;
}

</script>

<input bind:value={prompt}>
<button type="button" name="button" on:click={() => sendMessage(prompt)}>click</button>
<p>{answer}</p>
