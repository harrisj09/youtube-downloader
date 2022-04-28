import sys
import tkinter
from tkinter import filedialog
from pytube import YouTube

from PyQt5.QtWidgets import *


class YouTubeVideo():

    def __init__(self, url, path):
        self.url = url
        self.path = path

    '''
    YouTube broke the API basically, but this does work
    https://stackoverflow.com/a/46562895/13604948
    '''
    def downloadVideo(self):
        print("Downloading video")
        # YouTube(self.url).streams.first().download(self.path)

    def videoData(self):
        data = []
        data.append(YouTube(self.url).author)
        data.append(YouTube(self.url).title)
        data.append(YouTube(self.url).length)
        print("Getting data")
        print(data)
        return data


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
            lambda: self.downloadVideo(urlEditText.toPlainText(), dircTextEdit.toPlainText(), author,
                                       title, length))
        hbox.addWidget(downloadButton)
        groupBox3.setLayout(hbox)

        # Groupbox 4
        groupBox4 = QGroupBox()
        # author, title, descr, date,  length
        author = QLabel("Author: ")
        title = QLabel("Title: ")
        length = QLabel("Length: ")
        vbox = QVBoxLayout()
        vbox.addWidget(author)
        vbox.addWidget(title)
        vbox.addWidget(length)
        groupBox4.setLayout(vbox)

        # Setting layouts
        gridLayout.addWidget(groupBox)
        gridLayout.addWidget(groupBox2)
        gridLayout.addWidget(groupBox3)
        gridLayout.addWidget(groupBox4)
        self.setLayout(gridLayout)
        self.show()

    def openExplorer(self, textedit):
        tkinter.Tk().withdraw()
        folder_path = filedialog.askdirectory()
        textedit.setPlainText(folder_path)

    def downloadVideo(self, URL, directory, author, title, length):
        data = None
        if not URL and not directory:
            print("Invalid Input")
        else:
            youtube = YouTubeVideo(URL, directory)
            youtube.downloadVideo()
            data = youtube.videoData()
            # Use a loop
            author.setText("Author: " + data[0])
            title.setText("Title: " + data[1])
            length.setText("Length: " + str(data[2]))



def main():
    app = QApplication(sys.argv)
    gui = Application()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()