Following setup shows the recipe to enable the GPU enabled Tensorflow on Ububtu 18.04. 

Following instruction tested for the following config:
GFX Card: Nvidia 1070 Ti
Tensorflow: 1.10.0
Ubuntu:18.04
Keras: 2.2.4

```
1. Install CUDA Driver:
	Goto software and updates. Select Additional Drivers tab. Install nvidia-driver-390
	
	Command Line:
		#first get the PPA repository driver
		sudo add-apt-repository ppa:graphics-drivers/ppa
        
        	# install nvidia driver 
		sudo apt install nvidia-384 nvidia-384-dev

2: Install other required packages.
	sudo apt-get install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
	# CUDA 9 requires gcc 6
	sudo apt install gcc-6
	sudo apt install g++-6

        # set up symlinks for gcc/g++
        sudo ln -s /usr/bin/gcc-6 /usr/local/cuda/bin/gcc
        sudo ln -s /usr/bin/g++-6 /usr/local/cuda/bin/g++


3: Install CUDA Toolkit:
	Goto https://developer.nvidia.com/cuda-90-download-archive. Select the appropriate options and download the .run file
	Commandline:
		# download one of the "runfile (local)" installation packages from cuda toolkit archive 
		wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run

	# make the download file executable
	chmod +x cuda_9.0.176_384.81_linux-run 
	sudo ./cuda_9.0.176_384.81_linux-run --override

	# Answer questions following while installation begin
	# You are attempting to install on an unsupported configuration. Do you wish to continue? y
	# **Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 384.81? n**
	# Install the CUDA 9.0 Toolkit? y


	# setup your paths
	echo 'export PATH=/usr/local/cuda-9.0/bin:$PATH' >> ~/.bashrc
	echo 'export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64:$LD_LIBRARY_PATH' >> ~/.bash.rc
	source ~/.bashrc

4: Install cuDNN v7.0.5
	Goto https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.0.5/prod/9.0_20171129/cudnn-9.0-linux-x64-v7. 
	Login into the account and download it.
	tar -xzvf cudnn-9.0-linux-x64-v7.tgz

	#copy the following files into the cuda toolkit directory.
	sudo cp -P cuda/include/cudnn.h /usr/local/cuda-9.0/include
	sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-9.0/lib64/
	sudo chmod a+r /usr/local/cuda-9.0/lib64/libcudnn*

5: Install Tensorflow and Keras:
pip install tensorflow-gpu==1.10.0

```
