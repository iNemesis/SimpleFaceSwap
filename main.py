import sys
import uuid

import insightface

from lib.faceswapper import FaceSwapper

assert insightface.__version__ >= '0.7'

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: python main.py image_to_swap image_with_face")
        print(sys.argv)
        exit(1)

    image_to_swap = sys.argv[1]
    image_with_face = sys.argv[2]

    FaceSwapper().swap(image_with_face, image_to_swap, "./result/" + str(uuid.uuid4()) + ".jpg")
