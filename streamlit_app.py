import geocoder
import streamlit as st
import socket

def get_server_location(domain):
    try:
        # Convert domain to IP address
        ip_address = socket.gethostbyname(domain)
        location = geocoder.ip(ip_address)
        return location
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def display_server_location(domain):
    location = get_server_location(domain)
    if location and location.latlng:
        st.write("### Server Location")
        st.write(f"**Latitude:** {location.latlng[0]}")
        st.write(f"**Longitude:** {location.latlng[1]}")
        st.write(f"**City:** {location.city}")
        st.write(f"**Country:** {location.country}")
    else:
        st.error("Failed to retrieve server location.")

def main():
    st.title("Server Location Tool")
    url = st.text_input("Enter a website URL (e.g., example.com)")

    if st.button("Check Location"):
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        st.write("## Results")
        display_server_location(domain)

if __name__ == "__main__":
    main()
