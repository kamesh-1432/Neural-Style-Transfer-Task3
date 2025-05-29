import os
from pyngrok import ngrok

# Kill any existing tunnels (optional)
ngrok.kill()

# Start the Streamlit app
os.system("streamlit run app.py &")

# Correct tunnel config for Ngrok v3+
public_url = ngrok.connect(addr="8501")  # ✅ Use 'addr' not 'port'
print("🔗 Streamlit app is live at:", public_url)
