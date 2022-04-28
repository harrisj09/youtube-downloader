import sys
import tkinter
from tkinter import filedialog
from pytube import YouTube

from PyQt5.QtWidgets import *

"""
GUI Class

Author: John Harris
"""


class YouTubeVideo():

    '''

    url = YouTube(str(link.get()))

    video = url.streams.filter(file_extension=extension).first()

    video.download()
'''
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def downloadVideo(self):
        yt = YouTube(self.url)
        streams = yt.streams.get_by_itag(21)
        streams.download(self.path)


class Application(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 620)
        self.setWindowTitle('YouTube Video Downloader')
        gridLayout = QGridLayout()

        # Groupbox 1
        groupBox = QGroupBox()
        # Creating HBox
        hbox = QHBoxLayout()
        dircLabel = QLabel("Enter your directory for storing: ")
        dircButton = QPushButton("Open Explorer")
        dircTextEdit = QTextEdit()
        dircButton.clicked.connect(lambda: self.openExplorer(dircTextEdit))
        # Adding widgets
        hbox.addWidget(dircLabel)
        hbox.addWidget(dircTextEdit)
        hbox.addWidget(dircButton)
        groupBox.setLayout(hbox)

        # Groupbox 2
        groupBox2 = QGroupBox()
        hbox = QHBoxLayout()
        urlLabel = QLabel("Paste Video URL: ")
        urlEditText = QTextEdit()
        hbox.addWidget(urlLabel)
        hbox.addWidget(urlEditText)
        groupBox2.setLayout(hbox)

        # Groupbox 3
        groupBox3 = QGroupBox()
        hbox = QHBoxLayout()
        downloadButton = QPushButton("Download Video")
        downloadButton.clicked.connect(
            lambda: self.downloadVideo(urlEditText.toPlainText(), dircTextEdit.toPlainText()))
        hbox.addWidget(downloadButton)
        groupBox3.setLayout(hbox)

        # Setting layouts
        gridLayout.addWidget(groupBox)
        gridLayout.addWidget(groupBox2)
        gridLayout.addWidget(groupBox3)
        self.setLayout(gridLayout)
        self.show()

    def openExplorer(self, textedit):
        tkinter.Tk().withdraw()
        folder_path = filedialog.askdirectory()
        textedit.setPlainText(folder_path)

    def downloadVideo(self, URL, directory):
        if not URL and not directory:
            print("Invalid Input")
        else:
            youtube = YouTubeVideo(URL, directory)
            youtube.downloadVideo()


def main():
    app = QApplication(sys.argv)
    gui = Application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams[0].download()
    main()
'''
Error for person reading this

  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\__main__.py", line 181, in fmt_streams
    extract.apply_signature(stream_manifest, self.vid_info, self.js)
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\extract.py", line 409, in apply_signature
    cipher = Cipher(js=js)
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\cipher.py", line 43, in __init__
    self.throttling_plan = get_throttling_plan(js)
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\cipher.py", line 405, in get_throttling_plan
    raw_code = get_throttling_function_code(js)
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\cipher.py", line 311, in get_throttling_function_code
    name = re.escape(get_throttling_function_name(js))
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\cipher.py", line 296, in get_throttling_function_name
    raise RegexMatchError(
pytube.exceptions.RegexMatchError: get_throttling_function_name: could not find match for multiple

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "A:\python projects\youtube downloader\main.py", line 105, in <module>
    YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams[0].download()
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\__main__.py", line 296, in streams
    return StreamQuery(self.fmt_streams)
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\__main__.py", line 188, in fmt_streams
    extract.apply_signature(stream_manifest, self.vid_info, self.js)
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\extract.py", line 409, in apply_signature
    cipher = Cipher(js=js)
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\cipher.py", line 43, in __init__
    self.throttling_plan = get_throttling_plan(js)
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\cipher.py", line 405, in get_throttling_plan
    raw_code = get_throttling_function_code(js)
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\cipher.py", line 311, in get_throttling_function_code
    name = re.escape(get_throttling_function_name(js))
  File "A:\python projects\youtube downloader\venv\lib\site-packages\pytube\cipher.py", line 296, in get_throttling_function_name
    raise RegexMatchError(
pytube.exceptions.RegexMatchError: get_throttling_function_name: could not find match for multiple

Process finished with exit code 1

'''