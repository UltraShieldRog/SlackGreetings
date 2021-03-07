import requests

class SlackMessaging:
    def __init__(self, web_hook):
        self.web_hook = web_hook

    def send_message(self, text):
        headers = {
            'Content-type': 'application/json',
        }

        data = f'{{"text": "{text}"}}'

        response = requests.post(
            self.web_hook, 
            headers=headers, 
            data=data
        )
