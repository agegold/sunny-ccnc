import numpy as np

CAMERA_OFFSET_METERS = 0.1016  # 4 inches. Positive = Right of Center, Negative = Left of Center


def apply_camera_offset(model_transform, intrinsics, height):
  cy = intrinsics[1, 2]
  shear = np.eye(3, dtype=np.float32)
  shear[0, 1] = CAMERA_OFFSET_METERS / height
  shear[0, 2] = -CAMERA_OFFSET_METERS / height * cy
  model_transform = (shear @ model_transform).astype(np.float32)
  return model_transform
