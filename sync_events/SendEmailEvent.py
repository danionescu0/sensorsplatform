from blinker import signal

class SendEmailEvent:
    def send(self, address: str, title: str, body: str):
        event = signal("send_email")
        self.address = address
        self.title = title
        self.body = body