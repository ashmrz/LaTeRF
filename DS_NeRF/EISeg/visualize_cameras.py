import trimesh
import shapely
import numpy as np

DATA_DIR = '../../../nerf-supervision-public/logs/office/renderonly_train_199999'

def visualize_poses(poses, size=0.1):
    # poses: [B, 4, 4]

    axes = trimesh.creation.axis(axis_length=4)
    sphere = trimesh.creation.icosphere(radius=1)
    objects = [axes, sphere]

    for pose in poses:
        # a camera is visualized with 8 line segments.
        pos = pose[:3, 3]
        a = pos + size * pose[:3, 0] + size * pose[:3, 1] + size * pose[:3, 2]
        b = pos - size * pose[:3, 0] + size * pose[:3, 1] + size * pose[:3, 2]
        c = pos - size * pose[:3, 0] - size * pose[:3, 1] + size * pose[:3, 2]
        d = pos + size * pose[:3, 0] - size * pose[:3, 1] + size * pose[:3, 2]

        segs = np.array([[pos, a], [pos, b], [pos, c], [pos, d], [a, b], [b, c], [c, d], [d, a]])
        segs = trimesh.load_path(segs)
        objects.append(segs)

    trimesh.Scene(objects).show()

def visualize_cameras(num_of_images):
    poses = []
    for i in range(num_of_images):
        poses.append(np.loadtxt(f'./{DATA_DIR}/pose/{i:06}.txt'))
    poses = np.array(poses)
    print(poses.shape)
    visualize_poses(poses)
    
visualize_cameras(72)
