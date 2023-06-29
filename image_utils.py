import cv2
import numpy as np
from skimage.feature import local_binary_pattern

def extract_color_features(image):
    """extract avgerage R,G,B channels"""
    mean_b, mean_g, mean_r = cv2.mean(image)[:3]
    return mean_b, mean_g, mean_r

def extract_temperature_feature(image):
    """extract temperature of image"""
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mean_h = cv2.mean(hsv_image)[0]
    return mean_h

def extract_texture_features(image):
    """extract histogram of binary pattern ranges
    https://en.wikipedia.org/wiki/Local_binary_patterns
    idk wtf this does
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    n_points = 8  # Number of points in LBP neighborhood
    radius = 1    # Radius of LBP neighborhood
    lbp = local_binary_pattern(gray_image, n_points, radius, method='uniform')
    histogram = np.histogram(lbp, bins=range(0, n_points + 3), density=True)[0]
    return histogram

def extract_sharpness(image):
    "extract sharpness"
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sharpness = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    return sharpness
