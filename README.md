ResQ-Net is an agentic AI system designed to assist first responders during critical search and rescue missions. By leveraging high-performance NVIDIA NIM microservices and multimodal models, it analyzes drone footage, transcribes radio communications, and coordinates rescue efforts in real-time.

✨ Key Features
Multimodal Vision Agent: Uses Llama 3.2-11B-Vision (or Qwen-VL) to analyze high-resolution drone imagery, identifying survivors, structural damage, and optimal paths.

Speech-to-Text (ASR): Integrates NVIDIA Parakeet-CTC via the NeMo framework to transcribe field radio signals into actionable text.

Coordinator Agent: A central logic engine powered by Llama 3.1-8B or Nemotron-Nano that manages resource allocation and task prioritization.

Real-time Dashboard: A comprehensive Streamlit interface for visualizing drone feeds, transcripts, and agentic decisions.

Secure Data Lake: Integration with Google Cloud Storage (GCS) for archiving mission logs and Google Places API for location intelligence.

🛠️ Prerequisites
Hardware (Host)

Workstation: Dell Pro Max GB10.

GPU: NVIDIA GPU with 24GB+ VRAM (e.g., RTX 3090/4090, A100, A6000).

Drivers: NVIDIA GPU Driver Version 535+.

Software

OS: Linux (Ubuntu 22.04 recommended).

Containerization: Docker Engine 23.0.1+ & NVIDIA Container Toolkit.

Python: 3.12 (Note: 3.13 is currently incompatible with certain library builds like Pillow).

🚀 Installation & Setup
1. Clone the Repository

Bash
git clone https://github.com/aarti290589/Rss.git
cd ResQ_Net
2. Environment Configuration

Create a .env file or export your keys directly:

Bash
export NVIDIA_API_KEY="nvapi-your-key-here"
export GOOGLE_API_KEY="your-gcp-key-here"
export PYTHONPATH=$PWD:$PYTHONPATH
3. Python Environment Setup

Bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
🐳 Deployment (NVIDIA NIM)
Launch the Vision model container before starting the app:

Bash
export LOCAL_NIM_CACHE=~/.cache/nim
mkdir -p "$LOCAL_NIM_CACHE"

docker run -it --rm \
  --gpus all \
  --shm-size=16GB \
  -e NGC_API_KEY \
  -v "$LOCAL_NIM_CACHE:/opt/nim/.cache" \
  -p 8000:8000 \
  nvcr.io/nim/meta/llama-3.2-11b-vision-instruct:latest
🖥️ Running the Application
To start the ResQ-Net dashboard:

Bash
streamlit run src/frontend/app.py
📂 Project Structure
Directory	Description
src/agents/	Logic for Coordinator, Vision, and Communication agents.
src/models/	Client wrappers for NVIDIA NIM, NeMo, and LLM APIs.
src/frontend/	Streamlit UI components and layout.
src/utils/	Helpers for GCS uploads, image processing, and ASR.
💡 Troubleshooting
ModuleNotFoundError: Ensure you run the app from the root directory and that PYTHONPATH is exported.

Pillow Build Error: Ensure you are using Python 3.12. Python 3.13 fails on the __version__ metadata check for legacy Pillow builds.

403 Forbidden (Git): GitHub passwords are deprecated. Use a Personal Access Token (PAT) with repo scopes for authentication.

Missing API Key: If the CoordinatorAgent fails to initialize, verify that NVIDIA_API_KEY is set in your current shell.

📄 License
This project is licensed under the Llama 3.2 Community License. See LICENSE for details.
