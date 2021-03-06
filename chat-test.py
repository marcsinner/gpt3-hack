import openai
import json


OPENAI_API_KEY="YOUR_OPEN_AI_KEY"
openai.api_key = OPENAI_API_KEY

def get_response(question):
	prompt = "Human: "+question+" \nAI:"
	api_response = openai.Completion.create(
	  engine="davinci",
	  prompt=prompt,
	  temperature=0.9,
	  max_tokens=150,
	  top_p=1,
	  frequency_penalty=0.0,
	  presence_penalty=0.6,
	  stop=["\n", " Human:", " AI:"]
	)
	reponse_dict = json.loads(str(api_response))
	response = reponse_dict.get("choices")[0].get("text")

	return response


running = True
while running: 
	print("Human: ")
	input1 = input() 
	if input1 == "exit":
		running = False
		break
	response= get_response(input1)
	print("AI:%s" %(response))