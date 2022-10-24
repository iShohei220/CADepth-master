FROM pytorch/pytorch:latest

RUN pip install tensorboardX==2.1 opencv-python albumentations==0.5.2 matplotlib
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN apt-get install -y libglib2.0-0
