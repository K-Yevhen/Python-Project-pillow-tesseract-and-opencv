from ipywebrtc import CameraStream, ImageRecorder
from PIL import Image
import io

# print(help(CameraStream))
# print(help(ImageRecorder))

camera = CameraStream.facing_user(audio=False)
image_recorder = ImageRecorder(stream=camera)

image_recorder.recording = True
image_recorder.download()

# print(type(image_recorder.image))
img = Image.open(io.BytesIO(image_recorder.image.value))
img.show()
