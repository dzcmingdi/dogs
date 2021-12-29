import os

root_path = 'out/data/dog_data'
folders = os.listdir(root_path)
contents = []

for f in folders:
    dog_txt = open(os.path.join(root_path, f, f"{f}.txt"), encoding='utf-8')
    content = dog_txt.readlines()
    dog_name, dog_description_text = content[0], content[1]
    contents.append(
        {'name': dog_name, 'text': dog_description_text, 'image': os.path.join(root_path, f, f"{f}.jpg"),
         'audio': os.path.join(root_path, f, f"{f}.wav")})

