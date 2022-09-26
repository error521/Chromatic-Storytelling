# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os
from os import listdir
# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import cv2
import numpy as np
import PIL
from PIL import Image
import streamlit as st

def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)
    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()
    # return the histogram
    return hist

def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    startX = 0
    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

st.write("# Palette Generator thing")

uploaded_file = st.file_uploader("Choose an image file", type=['png','jpg'])
   
start = st.button("Generate Palette")


if uploaded_file is not None: 
    
    uploaded_image = Image.open(uploaded_file)
    st.image(uploaded_image, caption='Uploaded image', use_column_width=True)
    image = np.array(uploaded_image)
    
    # placeholder for fixed sized textbox
    txtbox = st.empty()
    txt = "Generating palette..."
    txtbox.write(txt)
    
    if start:          
        # load the image and convert it from BGR to RGB so that
        # we can display it with matplotlib
        
        #image = cv2.imread(image_path)
        scale_percent = 30 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        
        # resize image
        image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # reshape the image to be a list of pixels
        image = image.reshape((image.shape[0] * image.shape[1], 3))
        image = np.delete(image, np.where(image == [255, 255, 255]), axis=0)
        image = np.delete(image, np.where(image == [0, 0, 0]), axis=0)
        
        # K means clustering magic
        clt = KMeans(n_clusters = 5)
        clt.fit(image)
        
        
        txt = "Generated palette"
        txtbox.write(txt)
        
        # Plot that palette bar chart
        hist = centroid_histogram(clt)
        bar = plot_colors(hist,clt.cluster_centers_)
        fig = plt.figure()
        plt.axis("off")
        plt.imshow(bar)
        st.pyplot(fig)
        
    
