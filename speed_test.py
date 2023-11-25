import speedtest

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download()
    upload_speed = st.upload()
    print(f"Download speed: {download_speed / 1024 / 1024:.2f} Mbps")
    print(f"Upload speed: {upload_speed / 1024 / 1024:.2f} Mbps")

if __name__ == "__main__":
    test_speed()
