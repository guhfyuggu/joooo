from flask import Flask, request, render_template
import yt_dlp
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["url"]
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s'
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            return "✅ تم التحميل بنجاح!"
        except Exception as e:
            return f"❌ حدث خطأ: {e}"
    return render_template("index.html")