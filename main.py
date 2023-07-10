import numpy as np
import cv2
import insightface
from insightface.app import FaceAnalysis

assert insightface.__version__ >= '0.7'

if __name__ == '__main__':
    # setup insightFace
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))
    swapper = insightface.model_zoo.get_model('inswapper_128.onnx', download=False, download_zip=False)

    # import picture and extract the first founded face
    picture_with_source_face = cv2.imread("./face.jpg")
    source_faces = app.get(picture_with_source_face)
    source_faces = sorted(source_faces, key=lambda x: x.bbox[0])
    source_face = source_faces[0]

    # import picture to swap and extract faces
    picture_to_swap = cv2.imread("./imgtoswap.jpg")
    to_swap_faces = app.get(picture_to_swap)
    to_swap_faces = sorted(to_swap_faces, key=lambda x: x.bbox[0])
    # replace each face of the picture by source face
    swapped_picture = picture_to_swap
    for to_swap_face in to_swap_faces:
        swapped_picture = swapper.get(swapped_picture, to_swap_face, source_face, paste_back=True)
    cv2.imwrite("./t1_swapped.jpg", swapped_picture)

    # bonus : get each swapped face
    swapped_faces = []
    for to_swap_face in to_swap_faces:
        _img, _ = swapper.get(picture_to_swap, to_swap_face, source_face, paste_back=False)
        swapped_faces.append(_img)
    swapped_faces = np.concatenate(swapped_faces, axis=1)
    cv2.imwrite("./t1_swapped2.jpg", swapped_faces)
