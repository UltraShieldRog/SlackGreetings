import sys
import os
import shutil
import time
import argparse
import yaml
from datetime import datetime

from functions import time_converter
from slack import SlackMessaging


def main(cfg):
    scheduled_time = cfg['slack']['time'] if cfg['slack']['time'] else None
    slack_messager = SlackMessaging(cfg['slack']['channel'], scheduled_time, cfg['slack']['token'])

    try:
        slack_messager.send_message(
            cfg['slack']['message'])
    except Exception as e:
        slack_messager.send_message(
            'Error')

if __name__ == '__main__':
    start = time.time()

    parser = argparse.ArgumentParser(description='config')
    parser.add_argument(
        "--config",
        nargs="?",
        type=str,
        default="configs/default.yml",
        help="Configuration file to use"
    )
    
    args = parser.parse_args()

    with open(args.config, 'r') as stream:
        try:
            cfg = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            exit()

    main(cfg)
    
    end = time.time()
    elapsed = end - start
    print('The total time is: {}'.format(time_converter(elapsed)))