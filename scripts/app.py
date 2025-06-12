from flask import Flask, request, redirect, render_template
from funcs import *
import threading
import subprocess
import time

import getpass
print("Running as user:", getpass.getuser())


app = Flask(__name__, template_folder='../templates')


def get_active_window_title():
    try:
        window_id = subprocess.check_output(['xdotool', 'getactivewindow']).decode().strip()
        window_name = subprocess.check_output(['xdotool', 'getwindowname', window_id]).decode().strip()
        return window_name
    except subprocess.CalledProcessError:
        return "No active window"


def background_logger():
    while True:
        time.sleep(60)
        dbAdd(get_active_window_title())
        print("Next update in 1 minute...")


@app.route('/')
def index():

    activities = dbActivities()
    return render_template('main.html', activities = activities)

if __name__ == "__main__":
    threading.Thread(target=background_logger, daemon=True).start()

    app.run(debug=True, use_reloader=False)



