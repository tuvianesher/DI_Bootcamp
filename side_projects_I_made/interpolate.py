import os
from PIL import Image

WINDOW_SIZE = 64
ALPHA = 0.5
IMAGE_SIZE = (432, 768)


def get_frame(frames, index):
    n_frames = len(frames)
    half_window_size = WINDOW_SIZE // 2

    frame_range = range(index - half_window_size, index + half_window_size + 1)

    weighted_frames = []
    for i in frame_range:
        if i < 0:
            try:
                # try to access the last frame as if the list is looping around
                f = frames[i % n_frames]
            except FileNotFoundError:
                # if there's an error, fill in with a blank image
                f = Image.new("RGBA", IMAGE_SIZE, (0, 0, 0, 0))
        elif i >= n_frames:
            try:
                # try to access the first frame as if the list is looping around
                f = frames[i % n_frames]
            except FileNotFoundError:
                # if there's an error, fill in with a blank image
                f = Image.new("RGBA", IMAGE_SIZE, (0, 0, 0, 0))
        else:
            f = frames[i]

        img = Image.open(os.path.join(folder_path, f)).convert("RGBA")
        weighted_frames.append(img)

    out_frame = Image.blend(weighted_frames[0], weighted_frames[-1], ALPHA)
    for img in weighted_frames[1:-1]:
        out_frame = Image.blend(out_frame, img, ALPHA)

    return out_frame


def interpolate_frames(folder_path):
    frames = sorted(os.listdir(folder_path))
    frame_count = len(frames)

    out_folder_path = os.path.join(os.path.dirname(folder_path), folder_path + "_i")
    if not os.path.exists(out_folder_path):
        os.mkdir(out_folder_path)

    for i in range(frame_count):
        out_frame = get_frame(frames, i)
        out_path = os.path.join(out_folder_path, frames[i])
        out_frame.save(out_path)


if __name__ == "__main__":
    folder_path = "proj_12"
    interpolate_frames(folder_path)
