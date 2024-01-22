import socket
import platform
from contextlib import closing


def check_mm_server_alive(mm_ip='127.0.0.1', mm_port=4827):
    """
    Verify that micromanger 2.0 server is alive and actively
    accepting connections on windows where you have installed
    device adapters and configurations

    Args:
        mm_ip: ip address if you are running remotely
    
    Returns:
        True if micromanager server is accessible else false (default)
    """
    if platform.system() in ['Linux', 'Darwin']:
        return False
    elif platform.system() == 'Windows':
        # check if mm server is alive
        connection_alive = False
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((mm_ip, mm_port)) == 0:
                connection_alive = True
        return connection_alive



