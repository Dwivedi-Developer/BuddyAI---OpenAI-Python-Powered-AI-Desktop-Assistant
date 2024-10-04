import os
import openai
from config import apikey
openai.api_key = apikey
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my dean for holidays?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''{
  "id": "cmpl-7Rlug5j25TSgFNsbBDSyG83zDLUkp",
  "object": "text_completion",
  "created": 1686853390,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nSubject: Request for Holiday Leave\n\nDear Dean [Name],\n\nI am writing to make a formal request for holiday leave. This year has been especially challenging for both of us, especially due to the Covid-19 pandemic. Despite the challenges, I have managed to maintain a steady performance and have actively contributed to the activities of the college.\n\nI would like to take this opportunity to take a break from college duties and spend some time with my family. Given the current situation, I understand that this might be difficult to make happen and hence, I will take every possible responsibility for ensuring that the college is not adversely affected by my absence.\n\nI would also like to take this opportunity to thank you for your continued guidance and support this year. I look forward to your kind consideration of my request.\n\nSincerely,\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 178,
    "total_tokens": 187
  }
}'''