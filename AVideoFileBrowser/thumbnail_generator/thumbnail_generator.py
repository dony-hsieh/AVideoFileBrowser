import numpy as np
import cv2
import pathlib
import uuid


class ThumbnailGenerator:
    THUMBNAIL_FILETYPE = ".jpg"

    @staticmethod
    def __fetchFrames(video_filepath: str, frames: int) -> list:
        capture = cv2.VideoCapture(video_filepath)
        if not capture.isOpened():
            return []
        frameCounts = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        if frames >= frameCounts:
            return []
        interval = frameCounts // (frames + 1)
        frameIndex = [interval * i for i in range(1, frames + 1)]
        fetched = []
        for f in frameIndex:
            capture.set(cv2.CAP_PROP_POS_FRAMES, f)
            ret, frame = capture.read()
            if ret:
                fetched.append(frame)
        capture.release()
        return fetched

    @staticmethod
    def __createCollage(frame_list: list, row_thumb: int, col_thumb: int) -> np.ndarray:
        if not frame_list or len(frame_list) != row_thumb * col_thumb:
            return np.array([])
        frameSize = frame_list[0].shape
        collageCols = 1024
        resizeFactor = frame_list[0].shape[1] / (collageCols / col_thumb)
        tnSize = (int(frameSize[0] / resizeFactor), int(frameSize[1] / resizeFactor))
        rowStack = []
        for i in range(len(frame_list)):
            frame_list[i] = cv2.resize(frame_list[i], (tnSize[1], tnSize[0]), interpolation=cv2.INTER_CUBIC)
        for h in range(0, len(frame_list), col_thumb):
            rowStack.append(np.hstack(frame_list[h: h + col_thumb]))
        collage = np.vstack(rowStack)
        return collage

    @staticmethod
    def generate(
            video_filepath: str,
            dest_path: str,
            row_thumb: int = 4,
            col_thumb: int = 4,
            compress_quality: int = 50
    ) -> bool:
        collage = ThumbnailGenerator.__createCollage(
            ThumbnailGenerator.__fetchFrames(video_filepath, row_thumb * col_thumb), row_thumb, col_thumb
        )
        originalDestPathHolder = pathlib.Path(dest_path)
        if originalDestPathHolder.suffix == ThumbnailGenerator.THUMBNAIL_FILETYPE:
            # Because the dest_path parameter of cv2.imwrite() can only be ASCII character set,
            #   if there is an path formed by UNICODE character set,
            #   we use a random generated ASCII path to save it first,
            #   then rename that file to its original filename.
            tempRandDestPathHolder = originalDestPathHolder.parent.joinpath(
                uuid.uuid4().hex + ThumbnailGenerator.THUMBNAIL_FILETYPE
            )
            cv2.imwrite(str(tempRandDestPathHolder), collage, [cv2.IMWRITE_JPEG_QUALITY, compress_quality])
            if tempRandDestPathHolder.exists():
                tempRandDestPathHolder.rename(originalDestPathHolder)
            return True
        return False


if __name__ == "__main__":
    url1 = r"D:\LocalAVVideoBrowser\test_av.mp4"
    url2 = r"D:\LocalAVVideoBrowser\test_video.mp4"
    print(ThumbnailGenerator.generate(url1, r"D:\LocalAVVideoBrowser\友人の妹 mia - TOKYO Motion.jpg"))
