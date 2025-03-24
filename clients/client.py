import socket
import psutil
import jsonpickle

IP = '127.0.0.1'
PORT = 4000

def get_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        processes.append({
            'pid': proc.info['pid'],
            'name': proc.info['name']
        })
    return processes

def send_processes_to_server(processes, host, port):
    data = jsonpickle.dumps(processes)
    data_bytes = data.encode('utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data_bytes)
        s.close()

processes = get_processes()
send_processes_to_server(processes, IP, PORT)
