import requests

def send_slack_message(message):
    webhook_url = 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL'
    slack_data = {'text': message}

    response = requests.post(webhook_url, json=slack_data)

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

def check_prometheus_alerts():
    response = requests.get('http://localhost:9090/api/v1/alerts')
    alerts = response.json()['data']['alerts']

    for alert in alerts:
        if alert['state'] == 'firing':
            message = f"Alert: {alert['labels']['alertname']} - {alert['annotations']['description']}"
            send_slack_message(message)

if __name__ == "__main__":
    check_prometheus_alerts()
