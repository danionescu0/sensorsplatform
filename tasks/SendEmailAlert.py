import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tasks.BaseTask import BaseTask

class SendEmailAlert(BaseTask):

    def __init__(self, address: str, password: str, notified_address: str):
        self.address = address
        self.password = password
        self.notified_address = notified_address

    def run(self, event_data):
        if event_data['type'] == 'PS' and int(event_data['value']) > 1000:
            self.__send_alert("Got alert!!", "Value is:{0}".format(event_data['value']))

    def get_name(self):
        return 'send_alert'


    def __send_alert(self, subject: str, body: str) -> None:
        msg = MIMEMultipart()
        msg['From'] = self.address
        msg['To'] = self.notified_address
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.address, self.password)
        text = msg.as_string()
        server.sendmail(self.address, self.notified_address, text)
        server.quit()