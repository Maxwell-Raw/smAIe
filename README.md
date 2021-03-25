# smAIe
(1)本机基础环境
操作系统：Windows 10 , GPU：NVIDIA GeForce GTX 1050
(2)安装Anaconda3-2019.03-Windows-x86_64（自带python3.6.7）
下载地址：https://www.anaconda.com/distribution/
选择下载：Windows 64-bit Graphical Installer
安装文件：Anaconda3-2019.03-Windows-x86_64.exe
安装时，勾选下面两个选项：
√□Add Anaconda to the system PATH environment variable
√□Register Anaconda as the system Python
(3)安装Visual Studio Enterprise+update3中文版
下载地址：http://download.microsoft.com
安装文件：vs2015.3.ent_chs.iso
安装时，可按默认选项安装
(4)安装cmake3.10
下载地址：www.cmake.org
选择下载：Windows Win64-x64 installer
安装文件：cmake-3.10.0-rc1-win64-x64.msi
安装时，勾选添加系统环境变量（重启机器后生效）
(5)安装cuda10.1
下载地址：https://developer.nvidia.com/cuda-downloads
安装文件：cuda_10.1.168_425.25_win10.exe
安装时，按默认选项安装
(6)安装cudnn10.1
下载地址：https://developer.nvidia.com/rdp/cudnn-download
需要注册nvidia的账号，然后下载cudnn：
安装文件：cudnn-10.1-windows10-x64-v7.6.0.64.zip
先将安装文件解压缩，然后把cudnn目录下的bin、include以及lib目录中的文件拷贝到相应的cuda目录中的bin、include和lib目录中去（如：C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1），因为cuda会需要cudnn中的库文件以及头文件。
(7)安装dlib19.17
下载地址：dlib.net
安装文件：dlib-19.17.zip
安装时，先解压缩到本地磁盘，然后使用cmake编译。
(8)编译C++ dlib19.17
Windows重启（使系统环境变量生效）之后，打开cmake，然后点击“configure”按钮选择相应的vs版本，对于vs2015 update3应该选择“visual studio 14 2015 win64”选项。
(9)StyleGAN2需要安装定制开发的“TensorFlow ops”，建议安装TensorFlow 1.14，在anaconda中建立一个虚拟环境，之后所有第三方库都安装在此环境下：
conda create -n tensorflow2  python=3.6
之后进入此环境，安装tensorflow
conda install tensorflow-gpu=1.14
conda install keras
(10)安装定制开发的“TensorFlow ops”，还需要C语言编译器。
如果Visual Studio没有默认安装在“C：\”盘目录下，需要到“.\dnnlib\tflib\custom_ops.py”里修改一下编译器所在的路径，如：
compiler_bindir_search_path = ['C:/Program Files (x86)/Microsoft Visual Studio/2017/
Community/VC/Tools/MSVC/14.14.26428/bin/Hostx64/x64',
'C:/Program Files (x86)/Microsoft Visual Studio/2019/ Community/VC/Tools/MSVC/14.23.28105
/bin/Hostx64/x64',
'C:/Program Files (x86)/Microsoft Visual Studio 14.0/vc/bin',]
以上三个目录，分别是Visual Studio 2017、2019、2015的默认目录，可以修改为你自己安装的文件目录。
(11) 安装django
在cmd中进入之前创建的虚拟环境tensorflow2，之后安装django 2.1.3：
pip install django==2.1.3
(12)完成上述所有环境配置后，下载代码：
(13)运行项目：
打开cmd，进入文件夹中bysms1，之后使用通过python打开文件夹下的manage.py文件来运行服务器：python manage.py runserver 80
之后在浏览器中输入网址127.0.0.1:80/index.html就可以进入我们的网页
