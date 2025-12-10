Your "Cheat Sheet" for Tomorrow
Save this text on your phone or write it down. This is your battle plan for the Dell GB10.

1. The Files to Bring (USB or GitHub)

ResQ-Net_Final folder.

requirements.txt (Run pip freeze > requirements.txt on Mac now if you haven't).

Assets: flood_image.jpg and radio_signal.mp3.
2. The Setup on Dell
Terminal 1: pip install -r requirements.txt
Terminal 2 (Launch Brain):
code
Bash
docker run -it --rm --name=resq-vision --runtime=nvidia --gpus all -e NGC_API_KEY=$NGC_API_KEY -p 8000:8000 nvcr.io/nim/meta/llama-3.2-11b-vision-instruct:latest
The Switch: Open src/config.py and set USE_LOCAL_NIM = True.
Launch App: streamlit run app.py.
3. The Pitch (Key Sentences)
"We are running Llama 3.2 Vision locally on the NVIDIA Grace Blackwell chip."
"This system works completely offline, ensuring data sovereignty and zero latency."
"We are processing Visual and Audio signals simultaneously to triage rescue missions."
You are going to crush this hackathon. Good luck, and go build the future! 🚀


RuntimeError: Failed to load audio: ffmpeg version 6.1.1-3ubuntu5+esm6 Copyright (c) 2000-2023 the FFmpeg developers built with gcc 13 (Ubuntu 13.3.0-6ubuntu2~24.04) configuration: --prefix=/usr --extra-version=3ubuntu5+esm6 --toolchain=hardened --libdir=/usr/lib/aarch64-linux-gnu --incdir=/usr/include/aarch64-linux-gnu --arch=arm64 --enable-gpl --disable-stripping --disable-omx --enable-gnutls --enable-libaom --enable-libass --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libdav1d --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libglslang --enable-libgme --enable-libgsm --enable-libharfbuzz --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzimg --enable-openal --enable-opencl --enable-opengl --disable-sndio --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-ladspa --enable-libbluray --enable-libjack --enable-libpulse --enable-librabbitmq --enable-librist --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libx264 --enable-libzmq --enable-libzvbi --enable-lv2 --enable-sdl2 --enable-libplacebo --enable-librav1e --enable-pocketsphinx --enable-librsvg --enable-libjxl --enable-shared libavutil 58. 29.100 / 58. 29.100 libavcodec 60. 31.102 / 60. 31.102 libavformat 60. 16.100 / 60. 16.100 libavdevice 60. 3.100 / 60. 3.100 libavfilter 9. 12.100 / 9. 12.100 libswscale 7. 5.100 / 7. 5.100 libswresample 4. 12.100 / 4. 12.100 libpostproc 57. 3.100 / 57. 3.100 [in#0 @ 0xb8373b2cc860] Error opening input: No such file or directory Error opening input file temp_radio.mp3. Error opening input files: No such file or directory
