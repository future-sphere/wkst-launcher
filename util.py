import os
import socket


def get_current_pc_id():
    hostname = socket.gethostname()
    # hostname format XXX_PCYY, get the YY
    return hostname[-2:]
