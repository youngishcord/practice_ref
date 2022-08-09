import os
import pydicom
import numpy as np
import matplotlib
from matplotlib import pyplot


folder_path = "./data/data_to_upl/SE4/"
file_name = "1.2.392.200036.9116.2.5.1.3268.2051117476.1640498598.907503.dcm"
#file_name = "IM2"
file_path = os.path.join(folder_path,file_name)
ds = pydicom.dcmread(file_path)

print(ds.PatientName)
#data = np.array(ds.pixel_array)
#print(data)
#
pyplot.imshow(ds.pixel_array,cmap=pyplot.cm.bone)
pyplot.show()