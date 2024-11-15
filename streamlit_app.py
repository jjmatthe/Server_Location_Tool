import streamlit as st
import socket

def get_ip_address(domain):
    try:
        # Convert domain to IP address
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except Exception as e:
        st.error(f"Error fetching IP address: {e}")
        return None

def main():
    st.title("Basic IP Address Tool")
    url = st.text_input("Enter a website URL (e.g., example.com)")

    if st.button("Get IP Address"):
        domain = url.replace("http://", "").replace("https://", "").split("/")[0]
        ip_address = get_ip_address(domain)

        if ip_address:
            st.write("## Results")
            st.write(f"**IP Address:** {ip_address}")
        else:
            st.error("Failed to retrieve IP address.")

if __name__ == "__main__":
    main()
