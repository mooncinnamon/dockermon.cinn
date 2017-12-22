from celery import Celery
import psutil

app = Celery()


@app.task
def cpu_monitor():
    cpu = 0
    for x in range(2):
        cpu += psutil.cpu_percent(interval=1)
    return round(float(cpu) / 3, 2)
