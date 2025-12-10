from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage
from src.config import USE_LOCAL_NIM, MODEL_NAME, LOCAL_URL, CLOUD_API_KEY


def get_llm():
    """Returns the correct model connection based on hardware."""
    if USE_LOCAL_NIM:
        # DELL CONFIG (Local)
        return ChatNVIDIA(
            base_url=LOCAL_URL,
            model=MODEL_NAME,
            api_key="dummy",
            temperature=0.2,
            max_tokens=1024
        )
    else:
        # MAC CONFIG (Cloud)
        if not CLOUD_API_KEY:
            raise ValueError("❌ Missing NVIDIA_API_KEY in .env file for Mac mode.")
        return ChatNVIDIA(
            model=MODEL_NAME,
            api_key=CLOUD_API_KEY,
            temperature=0.2,
            max_tokens=1024
        )


def analyze_situation(img_base64, radio_transcript):
    """Core Agentic Logic"""
    llm = get_llm()

    prompt = f"""
    You are ResQ-Net, an autonomous disaster response agent.

    INPUT DATA:
    1. Visual: A drone image of the sector.
    2. Audio Transcript: "{radio_transcript}"

    MISSION:
    1. Analyze the image: Identify hazards (fire, flood, debris) and survivors.
    2. Correlate with Audio: Does the visual confirm the radio report?
    3. Action Plan: Recommend specific assets (Boat, Helicopter) and priority (1-5).

    Output format: JSON.
    """

    message = HumanMessage(content=[
        {"type": "text", "text": prompt},
        {"type": "image_url", "image_url": {"url": img_base64}}
    ])

    response = llm.invoke([message])
    return response.content