import requests

PROMETHEUS_URL = 'http://localhost:9090'

def query_prometheus(query):
    response = requests.get(f'{PROMETHEUS_URL}/api/v1/query', params={'query': query})
    results = response.json()['data']['result']
    return results

if __name__ == "__main__":
    query = 'up'  # Beispiel-Query
    results = query_prometheus(query)
    for result in results:
        print(result)
