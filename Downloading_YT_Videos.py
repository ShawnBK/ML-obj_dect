{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pytube3\n",
      "  Downloading pytube3-9.6.4-py3-none-any.whl (38 kB)\n",
      "Collecting typing-extensions\n",
      "  Downloading typing_extensions-3.7.4.2-py3-none-any.whl (22 kB)\n",
      "Installing collected packages: typing-extensions, pytube3\n",
      "Successfully installed pytube3-9.6.4 typing-extensions-3.7.4.2\n"
     ]
    }
   ],
   "source": [
    "!pip install pytube3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting opencv-python\n",
      "  Downloading opencv_python-4.2.0.34-cp37-cp37m-win_amd64.whl (33.0 MB)\n",
      "Requirement already satisfied: numpy>=1.14.5 in c:\\users\\shawn\\anaconda3\\lib\\site-packages (from opencv-python) (1.18.1)\n",
      "Installing collected packages: opencv-python\n",
      "Successfully installed opencv-python-4.2.0.34\n"
     ]
    }
   ],
   "source": [
    "!pip install opencv-python\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "from pytube import YouTube\n",
    "\n",
    "# misc\n",
    "import os\n",
    "import shutil\n",
    "import math\n",
    "import datetime\n",
    "\n",
    "# plots\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "\n",
    "# image operation\n",
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# instance of Youtube Class \n",
    "video = YouTube('    YOUTUBE VIDEO LINK    ')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Shawn\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:1: DeprecationWarning: Call to deprecated function all (This object can be treated as a list, all() is useless).\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[<Stream: itag=\"18\" mime_type=\"video/mp4\" res=\"360p\" fps=\"30fps\" vcodec=\"avc1.42001E\" acodec=\"mp4a.40.2\" progressive=\"True\" type=\"video\">,\n",
       " <Stream: itag=\"134\" mime_type=\"video/mp4\" res=\"360p\" fps=\"30fps\" vcodec=\"avc1.4d401e\" progressive=\"False\" type=\"video\">,\n",
       " <Stream: itag=\"243\" mime_type=\"video/webm\" res=\"360p\" fps=\"30fps\" vcodec=\"vp9\" progressive=\"False\" type=\"video\">,\n",
       " <Stream: itag=\"133\" mime_type=\"video/mp4\" res=\"240p\" fps=\"30fps\" vcodec=\"avc1.4d4015\" progressive=\"False\" type=\"video\">,\n",
       " <Stream: itag=\"242\" mime_type=\"video/webm\" res=\"240p\" fps=\"30fps\" vcodec=\"vp9\" progressive=\"False\" type=\"video\">,\n",
       " <Stream: itag=\"160\" mime_type=\"video/mp4\" res=\"144p\" fps=\"30fps\" vcodec=\"avc1.4d400c\" progressive=\"False\" type=\"video\">,\n",
       " <Stream: itag=\"278\" mime_type=\"video/webm\" res=\"144p\" fps=\"30fps\" vcodec=\"vp9\" progressive=\"False\" type=\"video\">,\n",
       " <Stream: itag=\"140\" mime_type=\"audio/mp4\" abr=\"128kbps\" acodec=\"mp4a.40.2\" progressive=\"False\" type=\"audio\">,\n",
       " <Stream: itag=\"249\" mime_type=\"audio/webm\" abr=\"50kbps\" acodec=\"opus\" progressive=\"False\" type=\"audio\">,\n",
       " <Stream: itag=\"250\" mime_type=\"audio/webm\" abr=\"70kbps\" acodec=\"opus\" progressive=\"False\" type=\"audio\">,\n",
       " <Stream: itag=\"251\" mime_type=\"audio/webm\" abr=\"160kbps\" acodec=\"opus\" progressive=\"False\" type=\"audio\">]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "video.streams.all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Shawn\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:2: DeprecationWarning: Call to deprecated function all (This object can be treated as a list, all() is useless).\n",
      "  \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[<Stream: itag=\"18\" mime_type=\"video/mp4\" res=\"360p\" fps=\"30fps\" vcodec=\"avc1.42001E\" acodec=\"mp4a.40.2\" progressive=\"True\" type=\"video\">,\n",
       " <Stream: itag=\"134\" mime_type=\"video/mp4\" res=\"360p\" fps=\"30fps\" vcodec=\"avc1.4d401e\" progressive=\"False\" type=\"video\">,\n",
       " <Stream: itag=\"133\" mime_type=\"video/mp4\" res=\"240p\" fps=\"30fps\" vcodec=\"avc1.4d4015\" progressive=\"False\" type=\"video\">,\n",
       " <Stream: itag=\"160\" mime_type=\"video/mp4\" res=\"144p\" fps=\"30fps\" vcodec=\"avc1.4d400c\" progressive=\"False\" type=\"video\">,\n",
       " <Stream: itag=\"140\" mime_type=\"audio/mp4\" abr=\"128kbps\" acodec=\"mp4a.40.2\" progressive=\"False\" type=\"audio\">]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# the available streams to mp4 files using the filter method\n",
    "video.streams.filter(file_extension = \"mp4\").all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:/Users/Shawn/Desktop/IBM Hack Challenge/YouTube Videos\\\\YouTube.mp4'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "video.streams.get_by_itag(18).download(\"    PATH TO THE STORED LOCATION    \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Class used for extracting frames from a video file.\n",
    "class FrameExtractor():\n",
    "\n",
    "    # Constructor func        \n",
    "    def __init__(self, video_path):\n",
    "        self.video_path = video_path\n",
    "        self.vid_cap = cv2.VideoCapture(video_path)\n",
    "        self.n_frames = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))\n",
    "        self.fps = int(self.vid_cap.get(cv2.CAP_PROP_FPS))\n",
    "        \n",
    "    # prints the duration of the video    \n",
    "    def get_video_duration(self):\n",
    "        duration = self.n_frames/self.fps\n",
    "        print(f'Duration: {datetime.timedelta(seconds=duration)}')\n",
    "    \n",
    "    # prints number of frames that will be extracted for given xth frame\n",
    "    def get_n_images(self, every_x_frame):\n",
    "        n_images = math.floor(self.n_frames / every_x_frame) + 1\n",
    "        print(f'Extracting every {every_x_frame} (nd/rd/th) frame would result in {n_images} images.')\n",
    "    \n",
    "    # extracts the frame     \n",
    "    def extract_frames(self, every_x_frame, img_name, dest_path=None, img_ext = '.jpg'):\n",
    "        if not self.vid_cap.isOpened():\n",
    "            self.vid_cap = cv2.VideoCapture(self.video_path)\n",
    "        \n",
    "        if dest_path is None:\n",
    "            dest_path = os.getcwd()\n",
    "        else:\n",
    "            if not os.path.isdir(dest_path):\n",
    "                os.mkdir(dest_path)\n",
    "                print(f'Created the following directory: {dest_path}')\n",
    "        \n",
    "        frame_cnt = 0\n",
    "        img_cnt = 0\n",
    "\n",
    "        while self.vid_cap.isOpened():\n",
    "            \n",
    "            success,image = self.vid_cap.read() \n",
    "            \n",
    "            if not success:\n",
    "                break\n",
    "            \n",
    "            if frame_cnt % every_x_frame == 0:\n",
    "                img_path = os.path.join(dest_path, ''.join([img_name, '_', str(img_cnt), img_ext]))\n",
    "                cv2.imwrite(img_path, image)  \n",
    "                img_cnt += 1\n",
    "                \n",
    "            frame_cnt += 1\n",
    "        \n",
    "        self.vid_cap.release()\n",
    "        cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# class obj\n",
    "fe = FrameExtractor('    PATH OF YOUTUBE VIDEO    ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Duration: 0:01:07.040000\n"
     ]
    }
   ],
   "source": [
    "# duration of video\n",
    "fe.get_video_duration()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Extracting every 100 (nd/rd/th) frame would result in 17 images.\n"
     ]
    }
   ],
   "source": [
    "# extracting every 100th frame\n",
    "fe.get_n_images(every_x_frame=100)   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "# extracting the image \n",
    "fe.extract_frames(every_x_frame=100, \n",
    "                  img_name='megaman', \n",
    "                  dest_path='    PATH TO THE STORED LOCATION    ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# viewing the image\n",
    "\n",
    "def show_image(path):\n",
    "    image = cv2.imread(path)\n",
    "    plt.imshow(image)\n",
    "    plt.show()\n",
    "show_image('<    PATH OF THE IMAGE    >')\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
