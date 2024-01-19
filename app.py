import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_cors import CORS, cross_origin
import aifunctions, uberduckfunctions, requests
from pathlib import Path

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/mnemonic', methods=['POST'])
@cross_origin()
def get_mnemonic():
    user_input = request.get_json()

    type = user_input['type']
    genre = user_input['genre']
    topic = user_input['topic']

    print("Topic: " + topic)
    print("Type: " + type)
    print("Genre: " + genre)

    user_prompt_title = {"role": "user", "content": "Give me a title for it"}

    url = None
    if type == "Mnemonic":
        print("Generating mnemonic...")
        title = topic

        options = {}
        user_prompt_poem = {"role": "user", "content": "Write some " + genre + " to help memorise the names of " + topic}

        options["messages"] = [user_prompt_poem]
        openai_response = aifunctions.chatCompletionQuery(options)
        transcript = openai_response.choices[0].message.content

    elif type == "Poem":
        print("Generating poem...")

        options = {}
        user_prompt_poem = {"role": "user", "content": "Write a short poem in the genre " + genre + " to help memorise the names of " + topic}

        options["messages"] = [user_prompt_poem]
        openai_response = aifunctions.chatCompletionQuery(options)
        transcript = openai_response.choices[0].message.content

        options = {}
        options["messages"] = [user_prompt_poem, {"role": "assistant", "content": transcript}, user_prompt_title]
        openai_response = aifunctions.chatCompletionQuery(options)
        title = openai_response.choices[0].message.content

        options = {}
        options["input"] = title + "\n\n" + transcript
        options["voice"] = "fable"

        spoken_transcript_file_path = Path(__file__).parent / "spoken_transcript.wav"
        spoken_transcript = aifunctions.audioGenerationQuery(options)
        spoken_transcript.stream_to_file(spoken_transcript_file_path)

        # url = googledrivefunctions.upload_File("spoken_transcript.wav")

    elif type == "Song":
        print("Generating song...")

        if genre == "Dark trap":
            title = "\"Imperial Echoes: The Roman Ten\""
            transcript = "(Verse)\nIn the heart of Rome, a tale unfolds,\nTen emperors' stories, as history molds.\nAugustus, the first, with Caesar's might,\nTiberius followed, in power's light.\n\nCaligula's whims, a tumultuous ride,\nClaudius then ruled, his wit as guide.\nNero's fiddle played a haunting song,\nGalba, Otho, Vitellius, a sequence strong.\n\n(Chorus)\nImperial echoes through time cascade,\nThe Roman ten, in history laid.\nFrom Augustus to Vespasian's reign,\nTheir legacies in memory remain."
            url = "LOCAL"

            # Still calling openAI to make sure there is a delay
            options = {}
            user_prompt_song = {"role": "user", "content": "Write lyrics to a very short song of the genre " + genre + " to help memorise the names of " + topic + ". The song should have no bridge and less than 32 lines."}

            options["messages"] = [user_prompt_song]
            aifunctions.chatCompletionQuery(options)

        else:
            options = {}
            user_prompt_song = {"role": "user", "content": "Write lyrics to a very short song of the genre " + genre + " to help memorise the names of " + topic + ". The song should have no bridge and less than 32 lines."}

            options["messages"] = [user_prompt_song]
            openai_response = aifunctions.chatCompletionQuery(options)
            transcript = openai_response.choices[0].message.content

            options = {}
            options["messages"] = [user_prompt_song, {"role": "assistant", "content": transcript}, user_prompt_title]
            openai_response = aifunctions.chatCompletionQuery(options)
            title = openai_response.choices[0].message.content

            url = uberduckfunctions.generate_rap(transcript)
    else:
        print("Error: Unsupported mnemonic type")
        return {}

    return {
        "title": title,
        "transcript": transcript,
        "url": url
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
