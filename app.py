from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = "FrontKick"
    
    # Get current server time in IST
    server_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
    
    # Get the top command output
    try:
        top_output = subprocess.check_output("top -n 1", shell=True).decode('utf-8')
    except subprocess.CalledProcessError:
        top_output = "Error fetching top output."

    # Return the HTML content
    return f"""
    <html>
    <head><title>System Info</title></head>
    <body>
        <h1>System Info</h1>
        <p><strong>Name:</strong> Soumy Jain</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
