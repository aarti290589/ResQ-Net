import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# 🎛️ HARDWARE SWITCH
# Set to TRUE when running on Dell GB10
# Set to FALSE when practicing on Mac
# ==========================================
USE_LOCAL_NIM = False

# Model Configuration
MODEL_NAME = "meta/llama-3.2-11b-vision-instruct"
LOCAL_URL = "http://localhost:8000/v1"
CLOUD_API_KEY = os.getenv("NVIDIA_API_KEY")