from IPython.display import Image
import numpy as np
import cv2
from datetime import datetime
import itertools
import warnings
warnings.filterwarnings("ignore")

letters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def words_from_labels(labels):
    """
    converts the list of encoded integer labels to word strings like eg. [12,10,29] returns CAT 
    """
    txt=[]
    for ele in labels:
        if ele == len(letters): # CTC blank space
            txt.append("")
        else:
            txt.append(letters[ele])
    return "".join(txt)

def decode_label(out):
    """
    Takes the predicted ouput matrix from the Model and returns the output text for the image
    """
    # out : (1, 48, 37)
    out_best = list(np.argmax(out[0,2:], axis = 1))

    out_best = [k for k, g in itertools.groupby(out_best)]  # remove overlap value

    outstr=words_from_labels(out_best)
    return outstr


#image height
img_h = 32
#image width
img_w = 170
#image Channels
img_c = 1
# classes for softmax with number of letters +1 for blank space in ctc
num_classes = len(letters) + 1
batch_size = 64
max_length = 15 # considering max length of ground truths labels to be 15


def single_image_Prediction(model, img_path):
    img = cv2.imread(img_path)
    img_resized = cv2.resize(img, (img_w, img_h))
    img = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    img = cv2.fastNlMeansDenoising(img, None, 20, 7, 21) 
    img = img.T 
    img = np.expand_dims(img, axis=-1)
    img = np.expand_dims(img, axis=0)
    img = img/255
    model_output = model.predict(img)
    predicted_output = decode_label(model_output)
    return predicted_output
