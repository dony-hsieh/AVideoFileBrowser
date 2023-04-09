import pathlib

_PROJECT_ROOT = pathlib.Path(__file__).parent.parent.absolute()

DB_FILE_PATH = _PROJECT_ROOT.joinpath("AVideoFileBrowser", "program_db.db").absolute()
VIDEO_DIR_PATH = _PROJECT_ROOT.joinpath("Data", "Video").absolute()
THUMBNAIL_DIR_PATH = _PROJECT_ROOT.joinpath("Data", "Thumbnail").absolute()
RESOURCE_DIR_PATH = _PROJECT_ROOT.joinpath("res").absolute()

if __name__ == "__main__":
    paths = {
        "_PROJECT_ROOT": _PROJECT_ROOT,
        "DB_FILE_PATH": DB_FILE_PATH,
        "VIDEO_DIR_PATH": VIDEO_DIR_PATH,
        "THUMBNAIL_DIR_PATH": THUMBNAIL_DIR_PATH,
        "RESOURCE_DIR_PATH": RESOURCE_DIR_PATH
    }
    for k, v in paths.items():
        print(f"{k:.<30}: {str(v):>5}")
