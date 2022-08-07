from pydicom import dcmread

ds = dcmread("./data/01_Баукова/КТ/652121513/DICOM/1.2.392.200036.9116.2.5.1.37.2418211076.1637897663.876915.dcm", force=True)#PA1_0001.dcm
#C:\Users\kulik\Desktop\practice program\orthanc_\data\01_Баукова\КТ\652121513\DICOM\1.2.392.200036.9116.2.5.1.37.2418211076.1637897663.876915.dcm
# Edit the (0010,0020) 'Patient ID' element
print(ds)
ds.PatientID = 40457
print(ds.PatientID)

#ds.save_as("/path/to/file_updated.dcm")