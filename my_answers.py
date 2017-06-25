import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
import re


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []
    
    # get the length of the series
    series_len = len(series)
    
    # iterate from index 0
    for idx, val in enumerate(series):
        # check whether the end is reached or not, if yes, then leave the loop
        if ((idx+window_size) >= series_len):
            break
        # get the series values of window size
        X.append(series[idx:idx+window_size])
        # get the series value after the window size
        y.append(series[idx+window_size])
    
        
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
     
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    pass


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    
    unique_characters = list(set(text))
    print(unique_characters)
    
    # remove as many non-english characters and character sequences as you can 
    text = re.sub(r"\d", " ", text.strip()) # remove all numbers
    text = text.replace('-',' ')
    text = text.replace('*',' ')
    text = text.replace('!',' ')
    text = text.replace(')',' ')
    text = text.replace('(',' ')
    text = text.replace('é',' ')
    text = text.replace('/',' ')
    text = text.replace('&',' ')
    text = text.replace('%',' ')
    text = text.replace('è',' ')
    text = text.replace('â',' ')
    text = text.replace('.',' ')
    text = text.replace(';',' ')
    text = text.replace(',',' ')
    text = text.replace('@',' ')
    text = text.replace(':',' ')
    text = text.replace('"',' ')
    text = text.replace('à',' ')
    text = text.replace('?',' ')
    text = text.replace('$',' ')
    text = text.replace("'",' ')
    
    # print again to double check
    unique_characters = list(set(text))
    print(unique_characters)
        
    # shorten any extra dead space created above
    text = text.replace('  ',' ')

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    
    # get the length of the series
    text_len = len(text)
    text = list(text)
    
    # iterate from index 0
    idx = 0
    for val in text:
        # check whether the end is reached or not, if yes, then leave the loop
        if ((idx+window_size) >= text_len):
            break
        # get the series values of window size
        inputs.append(text[idx:idx+window_size])
        # get the series value after the window size
        outputs.append(text[idx+window_size])
        # next step
        idx = idx + step_size
    
    # reshape each
    inputs = np.asarray(inputs)
    inputs.shape = (np.shape(inputs)[0:2])
    outputs = np.asarray(outputs)
    outputs.shape = (len(outputs),1)
    
    return inputs,outputs

