'''
    image_to_digit.py

    written by Quan Zhou on 12/16/14

    Reads an 8x8 image and guesses the numerical digit associated with it. 

    Example argument: python image_to_digit.py 5.png
'''
import sys                                      # To parse command line arguments
import numpy as np                              # Python's scientific Package
# from skimage import io                          # skimage's io package reads image formats
from svm_util import train_digit_classifier     # The util file I wrote that trains a classifier
import warnings
warnings.filterwarnings("ignore") # ignore warnings for now

# Name of the image we want to classify
fname = sys.argv[1]     # IMPORTANT! This should be a .png that is  8-pixel by 8-pixel in size. 

# Train the classifier
classifier = train_digit_classifier()   #Check out digit_classifier.py for more details

#Convert .png file -> python readible matrix (numpy)
from scipy import misc
pixel_data = misc.imread(fname, flatten=True)

#Do some data processing over our image
pixel_data = (255-pixel_data)                     # Invert the image
pixel_data = pixel_data/pixel_data.max()        # Normalize the data
pixel_data = pixel_data * 16                    # Rescale to 16.0 (so our svm can understand it)
pixel_data = np.round(pixel_data)               # convert decimal -> int
#Reshape the 8x8 -> 16x1 vector
pixel_vector = pixel_data.reshape(1,-1)

#Make a prediction!  (Make sure you ran digit_classification first!)
guess = classifier.predict(pixel_vector)

print
print "SVM predicts the digit as: %s" % (guess[0])
