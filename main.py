import face_recognition
import os
import shutil
import sys

your_images = ['ena.jpeg', 'dyo.jpeg', 'tria.jpeg']

your_face_encodings = []
for image_file in your_images:
    your_image = face_recognition.load_image_file(image_file)

    face_encodings = face_recognition.face_encodings(your_image)

    if face_encodings:
        your_face_encodings.append(face_encodings[0])
    else:
        print(f"No faces found in {image_file}. Please check the image.")

if not your_face_encodings:
    print("No faces were found in your images. Please check the images and try again.")
    sys.exit()

os.makedirs("Dimi", exist_ok=True)

all_pictures = os.listdir("confer")
n_pictures = len(all_pictures)

for i, filename in enumerate(all_pictures):
    try:
        conference_image = face_recognition.load_image_file(f"confer/{filename}")

        face_encodings = face_recognition.face_encodings(conference_image)

        if not face_encodings:
            continue

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(your_face_encodings, face_encoding,
                                                     tolerance=0.45)  # tolerance

            if True in matches:
                shutil.copy(f"confer/{filename}", f"Dimi/{filename}")
                break

    except Exception as e:
        print(f"Skipping {filename} due to errors.")

    progress = (i + 1) / n_pictures
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('=' * int(20 * progress), 100 * progress))
    sys.stdout.flush()

sys.stdout.write('\n')
