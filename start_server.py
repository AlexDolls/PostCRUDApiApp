import subprocess

process1 = subprocess.Popen(["python3", "manage.py", "runserver", "0.0.0.0:8000"])
process2 = subprocess.Popen(["python3", "manage.py", "upvote_eraser"])
process1.wait()
process2.wait()
