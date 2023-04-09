from PySide2.QtWidgets import QApplication, QMainWindow, QShortcut
from PySide2.QtCore import QUrl, QTime
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtGui import QKeySequence, QCloseEvent
import ffms2
import imageio
import sys

from AVideoFileBrowser.video_player.ui import video_player_ui


class MediaInfo:
    def __init__(self):
        self.url = ""
        self.duration = 0  # ms
        self.frameNums = 0

    @property
    def frameTimeMS(self) -> int:
        return int(self.duration / self.frameNums)

    def getFrameNums(self) -> int:
        try:
            vsource = ffms2.VideoSource(self.url)
            self.frameNums = vsource.properties.NumFrames
            return self.frameNums
        except (ValueError, ffms2.Error) as err:
            vsource = imageio.get_reader(self.url)
            self.frameNums = vsource.count_frames()
            return self.frameNums
        except:
            return 0

    def reset(self):
        self.url = ""
        self.duration = 0
        self.frameNums = 0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = video_player_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.controlButtonIcon = {"play": u"\u23F5", "pause": u"\u23F8"}
        self.ui.controlButton.clicked.connect(self.controlButtonClicked)
        self.ui.timeSlider.sliderMoved.connect(self.sliderMoved)

        self.keyShortcut = {
            "full_screen": QShortcut(QKeySequence("f"), self),
            "cancel_full_screen": QShortcut(QKeySequence("escape"), self),
            "forward_10s": QShortcut(QKeySequence("right"), self),
            "backward_10s": QShortcut(QKeySequence("left"), self),
            "play_pause": QShortcut(QKeySequence("space"), self),
            "forward_1frame": QShortcut(QKeySequence("ctrl+right"), self),
            "backward_1frame": QShortcut(QKeySequence("ctrl+left"), self)
        }
        self.keyShortcut["full_screen"].activated.connect(self.controlFullScreen)
        self.keyShortcut["cancel_full_screen"].activated.connect(self.cancelFullScreen)
        self.keyShortcut["forward_10s"].activated.connect(self.timeForward10s)
        self.keyShortcut["backward_10s"].activated.connect(self.timeBackward10s)
        self.keyShortcut["play_pause"].activated.connect(self.controlButtonClicked)
        self.keyShortcut["forward_1frame"].activated.connect(self.timeForward1Frame)
        self.keyShortcut["backward_1frame"].activated.connect(self.timeBackward1Frame)

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setVideoOutput(self.ui.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.mediaStatusChanged.connect(self.mediaStatusChanged)
        self.mediaInfo = MediaInfo()

    def loadMedia(self, url: str):
        self.show()
        mediaContent = QMediaContent(QUrl.fromLocalFile(url))
        self.mediaInfo.url = url
        self.mediaPlayer.setMedia(mediaContent)
        self.mediaPlayer.play()

    def mediaStateChanged(self, state: QMediaPlayer.State):
        if state == QMediaPlayer.PlayingState:
            self.ui.controlButton.setText(self.controlButtonIcon["pause"])
        else:
            self.ui.controlButton.setText(self.controlButtonIcon["play"])

    def mediaStatusChanged(self, status: QMediaPlayer.MediaStatus):
        if status == QMediaPlayer.EndOfMedia:
            self.mediaPlayer.play()
        if status == QMediaPlayer.BufferedMedia:
            f = self.mediaInfo.getFrameNums()
            if f == 0:
                self.mediaInfo.frameNums = self.mediaPlayer.metaData("VideoFrameRate")

    def durationChanged(self, duration):
        timeObj = QTime(0, 0, 0, 0).addMSecs(duration)
        self.ui.timeSlider.setRange(0, duration)
        self.ui.labelDurTime.setText(timeObj.toString())
        if duration > 0:
            self.mediaInfo.duration = duration

    def positionChanged(self, position):
        timeObj = QTime(0, 0, 0, 0).addMSecs(self.mediaPlayer.position())
        self.ui.labelCurTime.setText(timeObj.toString())
        self.ui.timeSlider.setValue(position)

    def controlButtonClicked(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def sliderMoved(self, position):
        self.mediaPlayer.setPosition(position)

    def controlFullScreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def cancelFullScreen(self):
        if self.isFullScreen():
            self.showNormal()

    def timeForward10s(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 10 * 1000)

    def timeBackward10s(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 10 * 1000)

    def timeForward1Frame(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + self.mediaInfo.frameTimeMS)

    def timeBackward1Frame(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - self.mediaInfo.frameTimeMS)

    def closeEvent(self, event: QCloseEvent) -> None:
        # set to empty media content to stop it completely
        self.mediaPlayer.setMedia(QMediaContent())
        self.mediaInfo.reset()


if __name__ == "__main__":
    # change import path in line 8 to "from ui import video_player_ui" if you want to run this section
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.loadMedia(r"D:\LocalAVVideoBrowser\test_video.mp4")
    sys.exit(app.exec_())
