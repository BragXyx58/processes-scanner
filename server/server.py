import socket
import jsonpickle

IP = '127.0.0.1'
PORT = 4000

def receive_processes_from_client(IP, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((IP , PORT))
        s.listen(1)
        print("Сервер запущен")
        conn, addr = s.accept()
        with conn:
            print("Подключено:", addr)
            data = b''
            while True:
                chunk = conn.recv(4096)
                if not chunk:
                    break
                data += chunk
            try:
                processes = jsonpickle.loads(data)
                return processes
            except Exception as e:
                print(f"Ошибка: {e}")
                return []

def display_processes(processes):
    if not processes:
        print("Нет процессов для отображения.")
        return
    for proc in processes:
        print(f"PID: {proc['pid']}, Name: {proc['name']}")

processes = receive_processes_from_client(IP, PORT)
display_processes(processes)
