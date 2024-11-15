import streamlit as st
import ipinfo
import socket

# Replace with your IPinfo API token
IPINFO_TOKEN = "ce0360f4a4f6fd"

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

# Function to display server location
def display_server_location(domain):
    location_data = get_server_location(domain)
    if location_data:
        st.write("### Server Location")
        st.write(f"**Country:** {location_data.get('country_name', 'Unknown')}")
        st.write(f"**Region:** {location_data.get('region', 'Unknown')}")
        st.write(f"**City:** {location_data.get('city', 'Unknown')}")
    else:
        st.error("Failed to retrieve server location.")

# Streamlit interface
def main():
    st.title("Geopolitical Cyber Risk Tool")
    url = st.text_input("Enter a website URL (e.g., example.com)")

    if st.button("Check Risk"):
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        st.write("## Results")
        display_server_location(domain)

if __name__ == "__main__":
    main()