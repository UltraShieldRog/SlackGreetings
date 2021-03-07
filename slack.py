from datetime import datetime
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackMessaging:
    def __init__(self, channel, time, token):
        self.client = WebClient()
        self.channel = channel
        self.time = datetime.strptime(time, '%d/%m/%Y %H:%M:%S') if time else None
        self.schedule = True if time else False
        self.token = token

    def send_message(self, text):
        try:
            if self.schedule:
            # Call the chat.scheduleMessage method using the WebClient
                result = self.client.chat_scheduleMessage(
                    token=self.token,
                    channel='#general',
                    text=text,
                    post_at=datetime.timestamp(self.time)
                )
            else:
                result = self.client.chat_postMessage(
                    token=self.token,
                    channel='#general',
                    text=text,
                    as_use='true'
                )
            print(result)
        except SlackApiError as e:
            print(e)