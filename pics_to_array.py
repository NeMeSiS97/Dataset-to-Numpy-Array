import numpy as np
import glob
from PIL import Image
filelist = glob.glob('Folder_name/*.jpg')
x = np.array([np.array(Image.open(fname)) for fname in filelist])
x.dump('file.npy')
