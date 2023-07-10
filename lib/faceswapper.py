import cv2
import insightface
from insightface.app import FaceAnalysis


class FaceSwapper:
    def __init__(self, model_path):
        self.app = FaceAnalysis(name='buffalo_l')
        self.app.prepare(ctx_id=0, det_size=(640, 640))
        self.swapper = insightface.model_zoo.get_model(model_path, download=False, download_zip=False)

    def swap(self, file_with_face, file_to_swap, file_output):
        # import picture and extract the first founded face
        picture_with_source_face = cv2.imread(file_with_face)
        source_faces = self.app.get(picture_with_source_face)
        source_faces = sorted(source_faces, key=lambda x: x.bbox[0])
        source_face = source_faces[0]

        # import picture to swap and extract faces
        picture_to_swap = cv2.imread(file_to_swap)
        to_swap_faces = self.app.get(picture_to_swap)
        to_swap_faces = sorted(to_swap_faces, key=lambda x: x.bbox[0])
        # replace each face of the picture by source face
        swapped_picture = picture_to_swap
        for to_swap_face in to_swap_faces:
            swapped_picture = self.swapper.get(swapped_picture, to_swap_face, source_face, paste_back=True)
        cv2.imwrite(file_output, swapped_picture)

