from openai import OpenAI
import os

client = OpenAI()

def chatCompletionQuery(options):
        """
        This method calls the openAI ChatCompletionCreate method. Use this if you want to send priming sequences.
        Options should be:
            messages=messages,
            temperature=1,
            max_tokens=1024,
            n=1,
            stop=None,
        The messages is an array of objects, system, user and assisant, eg:
        priming_sequence = [
            {"role": "system", "content": "You are an AI writer. You write compelling and informative content designed to help people understand complex topics."},
            {"role": "user", "content": "Mike: Hi, I'm a programmer setting up your environment."},
            {"role": "assistant", "content": "It's nice to meet you."},
        ]
        """
        options["model"] = "gpt-3.5-turbo"
        try:
            return client.chat.completions.create(
                **options
            )
        except Exception as e:
            print(f"Problem with: {e}.")

def audioGenerationQuery(options):
        """
        This method calls the openAI audioGenerationQuery method. Use this if you want to generate audio from text.
        Options should be:
            input=input,
            voice=voice
        The input is the text to transform into speech
        The voice is the voice type to use for the speech, e.g fable for story telling sounding (ideal for poems)
        """
        options["model"] = "tts-1"
        try:
            return client.audio.speech.create(
                **options
            )
        except Exception as e:
            print(f"Problem with: {e}.")