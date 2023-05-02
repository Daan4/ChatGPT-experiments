from helpers import *
import os
import json

prompt = 'Your task is to generate a hot new meme.' \
         'Use the following format for your response:' \
         'Image: <Describe the image>' \
         'Caption: <Describe the main text>' \
         'Subtitle (optional): <Describe the secondary text>' \
         'Note: <Give the idea behind the meme and how the image and text are related in at most 50 words>' \
         'The meme should not be related to AI, programming or mondays.' \
         'Format your response as a JSON dict with the keys image, caption, subtitle, note'

response = get_completion_from_prompt(prompt, temperature=1)

if not os.path.exists('output'):
    os.mkdir('output')

with open('output/memes.json', 'a+') as f:
    f.seek(0)
    text = f.read()
    if text == '':
        json.dump(json.loads('['+response+']'), f, indent=4)
    else:
        memes = json.loads(text)
        memes.append(json.loads(response))
        f.seek(0)
        f.truncate()
        json.dump(memes, f, indent=4)
