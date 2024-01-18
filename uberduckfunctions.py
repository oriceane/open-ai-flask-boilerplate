import requests, config, random
from IPython.display import Audio

uberduck_auth = ('pub_rokwpztlkrbewdbhcl', config.UBERDUCK_API_KEY)


def generate_rap(lyrics):
    print(lyrics)

    # voices = requests.get("https://api.uberduck.ai/voices", params=dict(mode="tts-basic")).json()
    # voice = random.choice(voices)
    # print("Selected voice")
    # print(voice)
    # voice_uuid = voice['voicemodel_uuid']

    backing_tracks = requests.get("https://api.uberduck.ai/reference-audio/backing-tracks", auth=uberduck_auth).json()
    backing_track = random.choice(backing_tracks['backing_tracks'])
    # print("Selected track")
    # print(backing_track)
    backing_track_uuid = backing_track['uuid']

    lyrics = [[
        "From Julius to Domitian",
        "A dynasty of mighty men",
        "Their stories written deep in stone",
        "The emperors of ancient Rome"
    ]]

    rap = requests.post(
        "https://api.uberduck.ai/tts/freestyle",
        json=dict(
            lyrics=lyrics,
            lines=len(lyrics[0]),
            voicemodel_uuid='4ec5c264-0a49-47c8-a3eb-c0d3518a65a1',
            # voicemodel_uuid=voice_uuid,
            backing_track=backing_track_uuid
        ),
        auth=uberduck_auth,
    )

    print(rap.json())

    return rap.json()["mix_url"]
