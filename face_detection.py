# importing libraries
import cv2
# import numpy as npy
import face_recognition as face_rec

# declaring images
chris = face_rec.load_image_file('sample pictures\chris.jpeg')
chris = cv2.cvtColor(chris, cv2.COLOR_BGR2RGB)                                                  # ensuring that the color of the image does not change
MR1 = face_rec.load_image_file('sample pictures\MR1.jpeg')
MR1 = cv2.cvtColor(MR1, cv2.COLOR_BGR2RGB)
MR_test = face_rec.load_image_file('sample pictures\MR2.jpeg')
MR_test = cv2.cvtColor(MR_test, cv2.COLOR_BGR2RGB)

# encoding the image
# image 1
faceLocation_MR1 = face_rec.face_locations(MR1)[0]
encode_MR1 = face_rec.face_encodings(MR1)[0]
cv2.rectangle(MR1, (faceLocation_MR1[3], faceLocation_MR1[0]), (faceLocation_MR1[1], faceLocation_MR1[2]), (255, 0, 255), 3)

# image 2
faceLocation_MR_test = face_rec.face_locations(MR_test)[0]
encode_MR_test = face_rec.face_encodings(MR_test)[0]
cv2.rectangle(MR_test, (faceLocation_MR_test[3], faceLocation_MR_test[0]), (faceLocation_MR_test[1], faceLocation_MR_test[2]), (255, 0, 255), 3)

# image 3
faceLocation_chris = face_rec.face_locations(chris)[0]
encode_chris = face_rec.face_encodings(chris)[0]
cv2.rectangle(chris, (faceLocation_chris[3], faceLocation_chris[0]), (faceLocation_chris[1], faceLocation_chris[2]), (255 ,0 ,255), 3)

# comparing the two and declaring whether the faces match or not
results = face_rec.compare_faces([encode_MR_test], encode_MR1)
print(results)
cv2.putText(encode_MR1, f'{results}', (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

# print encoded results
# print(encode_chris)
# print(encode_MR1)
# print(encode_MR_test)

# show the images
cv2.imshow('main_img1', MR1)
cv2.imshow('main_img2', MR_test)
cv2.waitKey(0)
cv2.destroyAllWindows()