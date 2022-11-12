import os
import random
import PIL 
from PIL import Image
import shutil

classes = {'Bicycle':2269-1471, 'Bridge':2022-1471, 'Bus':2698-1471, 'Car':5047-1471, 
'Cross':2729-1471, 'Hydrant':2441-1471, 'Palm':2401-1471, 'Traffic Light':2280-1471}

def generate():
    filepath = "images/current/"
    if os.path.exists(os.path.dirname(filepath)):
        shutil.rmtree(os.path.dirname(filepath))

    category = random.choice(list(classes.keys()))
    for i in range(9):
        if random.random() < .5:
            rand = random.randrange(1,classes[category])
            imagepath = f'data/{category}/{category}/{category} ({rand}).png'
            picture = Image.open(imagepath)  
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            picture.save(filepath + f'pic{i+1}', 'PNG')
        else:
            rand = random.randrange(1, 1465)
            imagepath = f'data/{category}/Other/Other ({rand}).png'
            picture = Image.open(imagepath)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            picture.save(filepath + f'pic{i+1}', 'PNG')

    

