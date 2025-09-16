from abc import ABC, abstractmethod


class Notifier(ABC):

    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotifier(Notifier):

    def send(self, message: str) -> None:
        print("Sending an Email")

class SmsNotifier(Notifier):

    def send(self, message: str) -> None:
        if message is not None:
            print(f"Sending message {message}")

def notify(notifier: Notifier, message: str) -> None:
    notifier.send(message)


email = EmailNotifier()
sms = SmsNotifier()

notify(email, "Sending a mail")
notify(sms, "Sending an sms")