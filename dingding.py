import datetime

import requests
import traceback

ding_alert_url = 'xxx'


def ding_push(content, md=True):
    """钉钉报警通知"""
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    url = ding_alert_url

    try:
        text = f'#### 小破站报警通知 \n\n {content}\n\n##### 当前时间: {current_time}'

        if not md:
            text = f'小破站报警通知 \n\n{content}\n\n{current_time}'

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "报警通知",
                "text": text,
            },
        }
        requests.post(url, json=data)
    except:
        traceback.print_exc()


if __name__ == '__main__':
    content = '当前数据有问题当前数据有问题当前数据有问题当前数据有问题'

    ding_push(content)