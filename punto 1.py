import subprocess
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")

class Ping:
    def __init__(self):
        pass

    def execute(self, ip_address: str) -> None:
        if ip_address.startswith("192."):
            for _ in range(10):
                result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE)
                print(result.stdout.decode('utf-8'))
        else:
            print("Invalid IP address. Must start with '192.'")

    def executefree(self, ip_address: str) -> None:
        for _ in range(10):
            result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE)
            print(result.stdout.decode('utf-8'))

class PingProxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        ip_address = input("Enter IP address: ")
        if ip_address == "192.168.0.254":
            ping = Ping()
            ping.executefree("www.google.com")
        else:
            self._real_subject.request()

def client_code(subject: Subject) -> None:
    subject.request()

if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)

    print("")

    print("Client: Executing the client code with PingProxy:")
    ping_proxy = PingProxy(real_subject)
    client_code(ping_proxy)