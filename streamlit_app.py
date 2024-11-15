import os
import ipinfo
import socket
import streamlit as st

# Retrieve IPinfo token from the environment variable
IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")

# Function to get server location
def get_server_location(domain):
    handler = ipinfo.getHandler(IPINFO_TOKEN)
    try:
        # Convert domain to IP address
        ip_address = socket.gethostbyname(domain)
        details = handler.getDetails(ip_address)
        return details.all
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def main():
    st.title("Geopolitical Cyber Risk Tool")
    url = st.text_input("Enter a website URL (e.g., example.com)")

    if st.button("Check Risk"):
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        st.write("## Results")
        display_server_location(domain)

if __name__ == "__main__":
    main()
