import os
import random
import PIL 
from PIL import Image
import shutil

classes = {'Bicycle':2269-1471, 'Bridge':2022-1471, 'Bus':2698-1471, 'Car':5047-1471, 
'Cross':2729-1471, 'Hydrant':2441-1471, 'Palm':2401-1471, 'Tlight':2280-1471}

def generate(category):
    labels = []
    filepath = f"images/{category}/"
    otherfilepath = f"images/Other/"
    if os.path.exists(os.path.dirname("images/")):
        shutil.rmtree(os.path.dirname("images/"))
    for i in range(9):
        if random.random() < .5:
            rand = random.randrange(1,classes[category])
            imagepath = f'data/{category}/{category}/{category} ({rand}).png'
            picture = Image.open(imagepath)  
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            picture.save(filepath + f'pic{i+1}.png', 'PNG')
            labels.append(1)
        else:
            rand = random.randrange(1, 1465)
            imagepath = f'data/{category}/Other/Other ({rand}).png'
            picture = Image.open(imagepath)
            os.makedirs(os.path.dirname(otherfilepath), exist_ok=True)
            picture.save(otherfilepath + f'pic{i+1}.png', 'PNG')
            labels.append(0)
    return labels
    

