import numpy
from rtclient.ui.main_window import run_ui 

def run():
    print("Real-time client")
    print(f"Numpy: {numpy.__version__}")
    run_ui()

if __name__ == '__main__':
    run()

