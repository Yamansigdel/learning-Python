# import requests

# res=requests.get('https://sherlock-holm.es/stories/plain-text/cano.txt')
# res.raise_for_status()
# print(res.status_code)
# print(len(res.text))
# # print(res.text[:500])


import requests

try:
    res = requests.get('https://sherlock-holm.es/stories/plain-text/cano.txt')
    res.raise_for_status()
    print(f"Status Code: {res.status_code}")
    print(f"Response Length: {len(res.text)}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
