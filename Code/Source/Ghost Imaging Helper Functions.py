#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 21:32:53 2024

@author: kieren
"""

import numpy as np
import random
import cv2 as cv 
import matplotlib.pyplot as plt


def binary_mask(M, N):
    # Generates a list with N sublists of M random bits
    return np.array([[random.randint(0, 1) for _ in range(M)] for _ in range(N)])
 
    
def gaussian_mask(M, N):
    # Generates a list with N sublists of M Gaussian masks 
    return np.random.normal(size=(N, M))
    


def forward_ghost(image, m, mask_func):
    # assumes image is black and white
    # Generates a list of masks for an image
    # returns the cross product of each mask with the image
    # and the masks (for later reversal)
    bucket = []
    image = np.ndarray.flatten(image)
    masks = mask_func(len(image), m)
    for mask in masks:
        bucket.append(np.dot(mask, image))
    return np.array(bucket), masks


def forward_ghost_matrix(image, m, mask_func):
    # same as above but leaving everything in matrix form
    # I'm not as used to thinking interms of matricies so this is more confusing..
    image = np.ndarray.flatten(image)
    masks = mask_func(len(image), m)
    bucket = np.dot(np.expand_dims(image, axis=0), masks.T)
    return bucket, masks
    
def adjoint_ghost(bucket, masks, shape):
    image = np.dot(masks.T,  (bucket - np.mean(bucket)).T)
    image = image.reshape(shape)
    return image

def adjoint_ghost_matrix(bucket, masks, shape):
    image = np.dot(np.linalg.pinv(masks), bucket.T)
    image = image.reshape(shape)
    return image

def simulator(image, m, mask_func):
    bucket, masks = forward_ghost_matrix(image, m, mask_func)
    output = adjoint_ghost_matrix(bucket, masks, image.shape)
    plt.imshow(output)
    return output, bucket
#src_img = cv.imread('/home/kieren/Documents/Projects/Comp. Caustics/monkey.jpg')

src_img = cv.imread('/home/kieren/Documents/Obsidian Vault/Courses/PHYS3042/Code/64x64.png')
src_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
plt.imshow(src_img)