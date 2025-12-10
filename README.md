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