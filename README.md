# OpenAI Flask Boilerplate instructions

1. Get an OpenAI API key and add it to the environment variable `OPENAI_KEY`
2. `pip install flask openai`
3. `python3 app.py`

## ChatGPT Tips and Tricks

Firstly, understand that GPT is conversational. That means even if you say `Please only respond with JSON`, it will probably still say something like:

```
OK! I understand, here's your JSON:
{
	"key": "Value"
}
```

Because while it's one of the world's most advanced AIs, it's still dumb as a brick. Here is a Python method that might help with extracting the JSON from a GPT response:

```python
def getJSONfromResponse(json_text):

    """
    Returns a JSON object from the openai api response. You'll need to get the openAIResponse['choices'][0]["message"]['content'] if you're using the ChatCompletion endpoint 
    or openAIResponse['choices'][0]["text"] if you're just using the Completion endpoint.
    """

    # Now try and load it as a JSON object
    try:

        # Remove or escape control characters
        json_bytes = json_text.encode('utf-8')
        json_text = json_bytes.decode('unicode_escape')

		# Remove trailing comma if it exists
        if json_text[-2] == ",":
            json_text = json_text[:-2] + "}"

        # If it's not just json, try and find the json in the string
        json_start = json_text.find("{")
        json_end = json_text.rfind("}") + 1
        json_str = json_text[json_start:json_end]

        # strict=false because we're not sure if it's valid json
        return json.loads(json_str, strict=False)

    except Exception as e:
        print(f"Unable to find any JSON: {e}.")
        return None
```

If you want to use priming, you have to send them to the ` openai.ChatCompletion.create`  endpoint (the `openai.Completion.create` doesn't support priming like the below, although you can prime with a standard prompt). Priming is an important part of working with LLMs and can save you a bunch of time writing prompts, here's an example:

```python
priming_sequence = [

        {"role": "system", "content": "You are an AI writer. You write business documents that are relevant to a certain standard I will provide later."},
        {"role": "user", "content": "Mike: Hi, I'm a programmer setting up your environment."},
        {"role": "assistant", "content": "It's nice to meet you."},
        {"role": "user", "content": f"Mike: I will provide you a [title] of a blogpost. I want you to provide at least 500 words of [content] for that blogpost. To help you, you will receive the title of the blog and the top of the blog"},
        {"role": "assistant", "content": "OK, I understand."},
        {"role": "user", "content": 'A computer will read your response, so I need you to respond to me with ONLY a JSON object and NOTHING ELSE. The next thing I send is an example of what I want you to return. '},
        {"role": "user", "content": '{"[title]": "[content]"}'},
        {"role": "assistant", "content": "OK, I understand."},
    ]

    priming_sequence.append(
        {"role": "user", "content": f"The [title] is 'How I like to clean my shoes'. The title of the blog is 'Mikes Housework Blog', the topic of the blog is 'Housework, Cleaning and Home Maintenance'"},
    )

     options = {
        "messages": priming_sequence,
        "temperature": 1,
        "max_tokens": 2048,
        "n": 1,
        "stop": None,
    }
```

Note the use of [title] and [content]. While I'm not sure if GPT treats these as variables, I've had more success with getting actually usable JSON by using these.