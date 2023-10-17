# Ultimate Vocal Remover GUI v5.6 - OpenCL Branch
<img src="https://raw.githubusercontent.com/Anjok07/ultimatevocalremovergui/master/gui_data/img/UVR_v5.6.png?raw=true" />

[![Release](https://img.shields.io/github/release/anjok07/ultimatevocalremovergui.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/anjok07/ultimatevocalremovergui/total.svg)](https://github.com/anjok07/ultimatevocalremovergui/releases)

## Branch Details

This branch is branch is meant for AMD GPU support. 

- This code works with:
   - VR Arch
   - MDX-Net & MDX23C
   - Demucs (v3 & v4 only)

- Current issues:
   - The GPU memory cache does not clear the same way it can with Cuda, so running ensembles might be difficult unless you have a lot of V-RAM.
   - The MDX23C models can't handle songs over 3 minutes with OpenCL using 8GB of video memory (V-RAM).
   - Some VR 5.1 & Demucs v3 models might run slower with OpenCL. 

## About

This application uses state-of-the-art source separation models to remove vocals from audio files. UVR's core developers trained all of the models provided in this package (except for the Demucs v3 and v4 4-stem models).

- **Core Developers**
    - [Anjok07](https://github.com/anjok07)
    - [aufr33](https://github.com/aufr33)

- **Support the Project**
    - [Donate](https://www.buymeacoffee.com/uvr5)

## Installation

These bundles contain the UVR interface, Python, PyTorch, and other dependencies needed to run the application effectively. No prerequisites are required.

### Windows Installation

- Please Note:
    - This installer is intended for those running Windows 10 or higher. 
    - Application functionality for systems running Windows 7 or lower is not guaranteed.
    - Application functionality for Intel Pentium & Celeron CPUs systems is not guaranteed.
    - You must install UVR to the main C:\ drive. Installing UVR to a secondary drive will cause instability.

- Download the UVR installer for Windows via the link below:
    - [Main Download Link](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_v5.6.0_setup_opencl.exe)

<details id="WindowsManual">
  <summary>Windows Manual Installation</summary>

### Manual Windows Installation

- Download and extract the repository [here](https://github.com/Anjok07/ultimatevocalremovergui/archive/refs/heads/master.zip)
- Download and install Python [here](https://www.python.org/ftp/python/3.9.8/python-3.9.8-amd64.exe)
   - Make sure to check "Add python.exe to PATH" during the install
- Run the following commands from the extracted repo directory:

```
python.exe -m pip install -r requirements.txt
```

If you have a compatible Nvidia GPU, run the following command:

```
python.exe -m pip install --upgrade torch --extra-index-url https://download.pytorch.org/whl/cu117
```

If you do not have FFmpeg or Rubber Band installed and want to avoid going through the process of installing them the long way, follow the instructions below.

**FFmpeg Installation**

- Download the precompiled build [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)
- From the archive, extract the following file to the UVR application directory:
   - ```ffmpeg-5.1.2-essentials_build/bin/ffmpeg.exe```

**Rubber Band Installation**

In order to use the Time Stretch or Change Pitch tool, you'll need Rubber Band.

- Download the precompiled build [here](https://breakfastquay.com/files/releases/rubberband-3.1.2-gpl-executable-windows.zip)
- From the archive, extract the following files to the UVR application directory:
   - ```rubberband-3.1.2-gpl-executable-windows/rubberband.exe```
   - ```rubberband-3.1.2-gpl-executable-windows/sndfile.dll```

</details>

### Linux Installation

<details id="LinuxInstall">
  <summary>See Linux Installation Instructions</summary>

<br />
    
**These install instructions are for Debian & Arch based Linux systems.**

- Download and save this repository [here](https://github.com/Anjok07/ultimatevocalremovergui/archive/refs/heads/master.zip)
- From the saved directory run the following commands in this order- 

**For Debian Based (Ubuntu, Mint, etc.):**
```
sudo apt update && sudo apt upgrade
sudo apt-get update
sudo apt install ffmpeg
sudo apt install python3-pip
sudo apt-get -y install python3-tk
pip3 install -r requirements.txt
python3 UVR.py
```

**For Arch Based (EndeavourOS):**
```
sudo pacman -Syu
sudo pacman -Sy
sudo pacman -S python-pip
sudo pacman -S --noconfirm tk
sudo pacman -S ffmpeg
```

To bypass environment setup and proceed with the installation, use:

- Take caution; this modifies system files.

```
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
```

Then proceed with the following in order:

```
chmod +x install_packages.sh
./install_packages.sh
python UVR.py
```

</details>

### Other Application Notes
- GPUs with at least 8GBs of V-RAM are recommended.
- This application is only compatible with 64-bit platforms. 
- This application relies on the Rubber Band library for the Time-Stretch and Pitch-Shift options.
- This application relies on FFmpeg to process non-wav audio files.
- The application will automatically remember your settings when closed.
- Conversion times will significantly depend on your hardware. 
- These models are computationally intensive. 

### Performance:
- Model load times are faster.
- Importing/exporting audio files is faster.

## Troubleshooting

### Common Issues

- If FFmpeg is not installed, the application will throw an error if the user attempts to convert a non-WAV file.
- Memory allocation errors can usually be resolved by lowering the "Segment" or "Window" sizes.

#### MacOS Sonoma Left-click Bug
There's a known issue on MacOS Sonoma where left-clicks aren't registering correctly within the app. This seems to be impacting all applications built with Tkinter on Sonoma.

Temporary solutions:
- Ensure you move your mouse slightly when left-clicking within the application; this ensures the left-click is registered.
- I'm developing a temporary fix that lets you use the middle mouse button or space bar as substitutes for left-clicks until the issue is fully resolved.

This issue is being tracked [here](https://github.com/Anjok07/ultimatevocalremovergui/issues/840).

### Issue Reporting

Please be as detailed as possible when posting a new issue. 

If possible, click the "Settings Button" to the left of the "Start Processing" button and click the "Error Log" button for detailed error information that can be provided to us.

## License

The **Ultimate Vocal Remover GUI** code is [MIT-licensed](LICENSE). 

- **Please Note:** For all third-party application developers who wish to use our models, please honor the MIT license by providing credit to UVR and its developers.

## Credits
- [ZFTurbo](https://github.com/ZFTurbo) - Created & trained the weights for the new MDX23C models. 
- [DilanBoskan](https://github.com/DilanBoskan) - Your contributions at the start of this project were essential to the success of UVR. Thank you!
- [Bas Curtiz](https://www.youtube.com/user/bascurtiz) - Designed the official UVR logo, icon, banner, and splash screen.
- [tsurumeso](https://github.com/tsurumeso) - Developed the original VR Architecture code. 
- [Kuielab & Woosung Choi](https://github.com/kuielab) - Developed the original MDX-Net AI code. 
- [Adefossez & Demucs](https://github.com/facebookresearch/demucs) - Developed the original Demucs AI code. 
- [KimberleyJSN](https://github.com/KimberleyJensen) - Advised and aided the implementation of the training scripts for MDX-Net and Demucs. Thank you!
- [Hv](https://github.com/NaJeongMo/Colab-for-MDX_B) - Helped implement chunks into the MDX-Net AI code. Thank you!

## Contributing

- For anyone interested in the ongoing development of **Ultimate Vocal Remover GUI**, please send us a pull request, and we will review it. 
- This project is 100% open-source and free for anyone to use and modify as they wish. 
- We only maintain the development and support for the **Ultimate Vocal Remover GUI** and the models provided. 

## References
- [1] Takahashi et al., "Multi-scale Multi-band DenseNets for Audio Source Separation", https://arxiv.org/pdf/1706.09588.pdf
