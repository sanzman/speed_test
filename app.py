import speedtest
from flask import Flask, render_template

app = Flask(__name__)

def get_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = round(st.download() / 1024 / 1024, 2)  # Round to 2 decimal places
    upload_speed = round(st.upload() / 1024 / 1024, 2)      # Round to 2 decimal places
    return download_speed, upload_speed

@app.route('/')
def home():
    download_speed, upload_speed = get_speed()
    return render_template('index.html', download_speed=download_speed, upload_speed=upload_speed)

if __name__ == '__main__':
    app.run(debug=True)