import requests, config, random
from IPython.display import Audio

uberduck_auth = ('pub_rokwpztlkrbewdbhcl', config.UBERDUCK_API_KEY)

def is_lyric(x):
    if len(x) == 0:
        return False
    if x.startswith("Verse"):
        return False
    elif x.startswith("(Verse"):
        return False
    elif x.startswith("(Chorus"):
        return False
    elif x.startswith("(Note"):
        return False
    elif x.startswith("(Outro"):
        return False
    else:
        return True

def get_parsed_lyrics(lyrics):
    for line in lyrics:
        if not is_lyric(line):
            continue
        yield line

def generate_rap(lyrics):
    lyrics_as_list = list(get_parsed_lyrics(lyrics.splitlines()))

#     print(requests.get("https://api.uberduck.ai/voices", params=dict(mode="tts-basic")).json())

    backing_tracks = requests.get("https://api.uberduck.ai/reference-audio/backing-tracks", auth=uberduck_auth).json()
    backing_track = random.choice(backing_tracks['backing_tracks'])
    backing_track_uuid = backing_track['uuid']

    rap = requests.post(
        "https://api.uberduck.ai/tts/freestyle",
        json=dict(
            lyrics=[lyrics_as_list],
            lines=32,
#             voicemodel_uuid='4ec5c264-0a49-47c8-a3eb-c0d3518a65a1',
            voicemodel_uuid='3b7973b2-741f-40df-96dc-3cd70c868291',
            backing_track=backing_track_uuid
        ),
        auth=uberduck_auth,
    )

    return rap.json()["mix_url"]
