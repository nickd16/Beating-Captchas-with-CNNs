import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras import layers, regularizers, models
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import random
import json
from generateImages import generate

def create_json():
    height = 120
    width = 120
    batch_size = 1
    classes = {'Bicycle':2269, 'Bridge':2022, 'Bus':2698, 'Car':5047, 'Cross':2729, 'Hydrant':2441, 'Palm':2401, 'Tlight':2280}
    predicted_labels = []

    category = random.choice(list(classes.keys()))
    true_labels = generate(category)

    dataset = tf.keras.utils.image_dataset_from_directory(
        f'images/',
        seed = 123,
        image_size=(height, width),
        batch_size=batch_size
    )

    def normalize_img(image,label):
        return tf.cast(image,tf.float32)/255.0, label

    AUTOTUNE = tf.data.experimental.AUTOTUNE
    dataset = dataset.map(normalize_img, num_parallel_calls = AUTOTUNE)

    acc = 1
    class CustomCallback(keras.callbacks.Callback):
        def on_test_batch_end(self, batch, logs=None):
            keys = list(logs.keys())
            curr = logs['accuracy']
            if curr < acc:
                acc == curr
                predicted_labels.append(-1)
            else:
                predicted_labels.append(1)


    model = keras.models.load_model(f'models/{category}_model/')
    stuff = model.evaluate(dataset, batch_size=batch_size, callbacks=[CustomCallback()])

    js = {
        "true_labels":true_labels,
        "predicted_labels":predicted_labels
    }

    return js


