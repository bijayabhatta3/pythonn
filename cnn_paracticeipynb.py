# -*- coding: utf-8 -*-
"""cnn paracticeipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qawnBnxG_Syq2N-PgzH9lcBY912LSlCp
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers,models,datasets
import matplotlib.pyplot as plt

(train_images,train_labels),(test_images, test_labels)=datasets.cifar10.load_data()

train_images.shape

train_labels.shape

test_images.shape

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer','dog', 'frog', 'horse', 'ship', 'truck']

train_images[0]

train_labels[0]

train_labels[0][0]

