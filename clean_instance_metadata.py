import json
import requests

headers = {'Authorization': "Bearer IiLrsPhpjMC3jc5lABN3VaAXB8cJ8WadvhN1BhUmwM4otAPW1LlOWGRThMIZsW3QTrEtd8itxJPnBd3DAyFiMDsLwrbjaUcpGBXlAfqyOvnP6LE3BeazclMh4hdDRnPu"}


def fetch_instance_data(instance_url):
    response = requests.get(instance_url, headers=headers)
    instance_data = json.loads(response.text)
    return instance_data


def make_complete_url(base_url, params):
    method = 'GET'
    req = requests.Request(method=method, url=base_url, params=params)
    prepped = req.prepare()
    return prepped.url


def dump_into_json(data):
    with open("clean.json", "a") as file1:
        for li in data:
            try:
                file1.write(str(li))
                file1.write('\n')
            except UnicodeEncodeError:
                continue


def clean_data(data):
    cleaned = []
    for li in data:
        meta_data = {}
        for key, value in li.items():
            if key == 'id' or key == 'name' or key == 'info':
                if key == 'info':
                    for k, v in li[key].items():
                        if k == 'other_languages_accepted' or k == 'federates_with':
                            continue
                        else:
                            meta_data[k] = v
                else:
                    meta_data[key] = value
            else:
                continue
        cleaned.append(meta_data)
    dump_into_json(cleaned)


if __name__ == '__main__':
    global_cache = []
    instance_url = "https://instances.social/api/1.0/instances/list"
    params = {'language': 'en', 'count': 1000}
    prepped_url = make_complete_url(instance_url, params)
    instance_data = fetch_instance_data(prepped_url)
    clean_data(instance_data["instances"])