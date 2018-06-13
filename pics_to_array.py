import numpy as np
import glob
from PIL import Image
filelist = glob.glob('Folder_name/*.jpg') #Enter the folder name containing the required images
x = np.array([np.array(Image.open(fname)) for fname in filelist])
x.dump('filename.npy') #Enter the file name that you preffer for the numpy array
