import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "e918dfe0-4718-413d-8e90-5b11a1a5175b"
FLOW_ID = "d7618542-4553-49d1-ab45-f6e47fb44241"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "customer" # The endpoint name of the flow

def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    # Set page title and icon
    st.set_page_config(page_title="Chat Interface", page_icon="💬")

    # Title with emoji
    st.title("💬 Chat Interface")

    # Divider
    st.markdown("<hr style='border: 2px solid red;'>", unsafe_allow_html=True)

    # Sidebar for additional info or controls
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("This is a chat interface powered by LangFlow API.")
        st.markdown("You can ask anything and get a response from the flow.")
        st.markdown("---")
        st.markdown("Made with ❤️ by [Your Name]")

    # Main content area
    st.subheader("📝 Enter your message below:")
    message = st.text_area("Message", placeholder="Ask something...", height=100)

    if st.button("🚀 Run Flow", help="Click to run the flow with your message"):
        if not message.strip():
            st.error("⚠️ Please enter a message")
            return
    
        try:
            with st.spinner("⏳ Running flow..."):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            
            # Display response in a styled box
            st.markdown("---")
            st.subheader("📤 Response:")
            st.success(response)
            st.markdown("---")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()