FROM dorowu/ubuntu-desktop-lxde-vnc:bionic

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1001 ubuntu

WORKDIR /home/ubuntu

USER root

RUN sudo apt update && sudo apt install -y wget vim python3-pip \
    && pip3 install future

# Install ROS Melodic
# Tested with this version https://raw.githubusercontent.com/PX4/Devguide/5e42a551ecb26a6fb77715f9f55f8075447d64d2/build_scripts/ubuntu_sim_ros_melodic.sh
RUN wget https://raw.githubusercontent.com/PX4/Devguide/master/build_scripts/ubuntu_sim_ros_melodic.sh
### ERRORS with https://github.com/PX4/Devguide/issues/1063
RUN /bin/bash -c "USER=ubuntu source ubuntu_sim_ros_melodic.sh"
RUN rm ubuntu_sim_ros_melodic.sh

# Install commonly used packages
RUN sudo apt update \
    && sudo apt install ros-melodic-uuv-simulator vim -y 

# Install ROS package dependencies
RUN sudo apt-get update \
    && sudo apt-get install ros-melodic-image-pipeline ros-melodic-rqt -y # For image_view \
    && rosmake image_view rqt

# Add setup files to bashrc
RUN echo source /opt/ros/melodic/setup.bash >> ~/.bashrc \
    && echo source ~/catkin_ws/devel/setup.bash >> ~/.bashrc

# Set some environment variables
ENV DISPLAY :0.0
ENV GAZEBO_MODEL_PATH ~/catkin_ws/src/descriptions/vortex_descriptions/world_models:~/catkin_ws/src/descriptions/vortex_descriptions/models

USER root

# "catkin build" needs to be run in ~/catkin_ws/src whenever a new package is added
