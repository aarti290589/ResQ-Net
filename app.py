import streamlit as st
import whisper  # <--- NEW LIBRARY
from PIL import Image
from src.agent import analyze_situation
from src.utils import process_image
from src.config import USE_LOCAL_NIM

st.set_page_config(page_title="ResQ-Net: Command Center", layout="wide", page_icon="🚁")


# Load the "Ear" (Whisper Model)
# We cache it so it doesn't reload every time
@st.cache_resource
def load_whisper():
    return whisper.load_model("base")  # "base" is fast and accurate enough for radio


model = load_whisper()

st.title("🚁 ResQ-Net: Autonomous Command")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. 👁️ Visual Feed")
    uploaded_image = st.file_uploader("Upload Drone Image", type=['jpg', 'jpeg', 'png'])

    st.subheader("2. 📻 Radio Signal")
    # NEW: Audio Uploader
    uploaded_audio = st.file_uploader("Upload Radio Frequency (.mp3/wav)", type=['mp3', 'wav'])

    if uploaded_image and uploaded_audio:
        # Display Image
        image = Image.open(uploaded_image)
        st.image(image, caption="Live Drone Feed", use_column_width=True)

        # Play Audio for the Judges
        st.audio(uploaded_audio)

        if st.button("🚨 ACTIVATE MULTIMODAL AGENT"):
            with col2:
                st.subheader("🧠 Mission Analysis")

                with st.status("Initializing Edge AI...", expanded=True) as status:
                    # STEP A: TRANSCRIBE (The Ear)
                    st.write("🎧 Transcribing Radio Frequency...")

                    # Save audio to temp file so Whisper can read it
                    with open("assets/temp_radio.mp3", "wb") as f:
                        f.write(uploaded_audio.getbuffer())

                    # Run Whisper locally
                    # Add fp16=False to fix the Mac/Python 3.13 crash
                    audio_result = model.transcribe("temp_radio.mp3", fp16=False)
                    transcript_text = audio_result["text"]

                    st.info(f"**Decoded Signal:** \"{transcript_text}\"")

                    # STEP B: REASONING (The Brain)
                    st.write("👁️ Correlating with Visuals...")
                    img_b64 = process_image(image)

                    # Pass the REAL transcript to the Agent
                    result = analyze_situation(img_b64, transcript_text)

                    status.update(label="✅ Command Sequence Generated", state="complete")
                    st.success("Analysis Complete")
                    # ------------------------------------------------
                    # REPLACE 'st.write(result)' WITH THIS VISUALIZER:
                    # ------------------------------------------------

                    # Attempt to parse JSON (if the model followed instructions)
                    import json

                    try:
                        # Clean up markdown code blocks if the AI added them
                        clean_json = result.replace("```json", "").replace("```", "").strip()
                        mission_data = json.loads(clean_json)

                        # 1. Top Level Metrics
                        m1, m2, m3 = st.columns(3)
                        m1.metric("Hazard Type", mission_data.get("hazard_type", "Unknown"), delta="Detected")
                        m2.metric("Survivors", mission_data.get("survivor_count", "0"), delta_color="inverse")
                        m3.metric("Severity Score", f"{mission_data.get('severity_score', 0)}/10")

                        # 2. The Recommendation
                        st.info(f"**🚨 RECOMMENDED ASSET:** {mission_data.get('recommended_asset', 'Analyze Further')}")

                        # 3. Reasoning
                        with st.expander("See Tactical Reasoning"):
                            st.write(mission_data.get("reasoning", result))

                    except:
                        # Fallback if AI didn't output perfect JSON
                        st.warning("Raw Mission Log:")
                        st.write(result)