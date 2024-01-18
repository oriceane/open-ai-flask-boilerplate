import requests, config
from IPython.display import Audio

uberduck_auth = ('pub_rokwpztlkrbewdbhcl', config.UBERDUCK_API_KEY)


def generate_rap(lyrics):
    # print(
    #     requests.get("https://api.uberduck.ai/voices", params=dict(mode="tts-basic")).json()
    # )
    #
    # print(
    #     requests.get(
    #         "https://api.uberduck.ai/reference-audio/backing-tracks", auth=uberduck_auth
    #     )
    # )

    lyrics = [[
        "From Julius to Domitian",
        "A dynasty of mighty men",
        "Their stories written deep in stone",
        "The emperors of ancient Rome"
    ]]

    lines = len(lyrics[0])

    rap = requests.post(
        "https://api.uberduck.ai/tts/freestyle",
        json=dict(lyrics=lyrics, lines=lines,
                  voicemodel_uuid='4ec5c264-0a49-47c8-a3eb-c0d3518a65a1',
                  backing_track='726f4142-c85a-4afc-a1e8-e76342692329'),
        auth=uberduck_auth,
    )
    print(rap.json()["mix_url"])
    return rap.json()["mix_url"]
