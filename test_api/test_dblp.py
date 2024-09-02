
import requests
from urllib.parse import urlencode

from typing import List, Dict, Union
BASE_URL = 'https://dblp.org/search/publ/api'

def search(queries: list[str]):
    results = []
    for query in queries:
        entry = {
            'query': query,
            'title': None,
            'year': None,
            'venue': None,
            'doi': None,
            'url': None,
            'bibtex': None,
        }
        options = {
            'q': query,
            'format': 'json',
            'h': 1,
        }
        r = requests.get(f'{BASE_URL}?{urlencode(options)}').json()
        hits = r.get('result').get('hits').get('hit')
        print(hits[0])
        titles = [hit.get('info').get('title') for hit in hits]
        print(titles)
        exit()
        hit = r.get('result').get('hits').get('hit')
        if hit is not None:
            info = hit[0].get('info')
            entry['title'] = info.get('title')
            entry['year'] = info.get('year')
            entry['venue'] = info.get('venue')
            entry['doi'] = info.get('doi')
            entry['url'] = info.get('ee')
            entry['bibtex'] = f'{info.get("url")}?view=bibtex'
        results.append(entry)
    return results


def search_for_papers_dblp(query, result_limit=1) -> Union[None, List[Dict]]:
    if not query:
        return None
    BASE_URL = 'https://dblp.org/search/publ/api'
    params = {
        'q': query,
        'format': 'json',
        'h': result_limit
    }
    rsp = requests.get(BASE_URL, params=params)
    print(f"Response Status Code: {rsp.status_code}")
    # print(f"Response Content: {rsp.text[:500]}")  # Print the first 500 characters of the response content
    rsp.raise_for_status()
    results = rsp.json()
    
    hits = results.get('result', {}).get('hits', {}).get('hit', [])
    if not hits:
        return None

    papers = []
    for hit in hits:
        info = hit.get('info', {})
        # authors = [author.get('text') for author in info.get('authors', {}).get('author', []) if isinstance(author, dict)]
        # authors = [author.get('text') for author in info.get('authors').get('author')]
        # 有的paper author为空，比如第二个paper
        paper = {
            'title': info.get('title'),
            'authors': [author.get('text') for author in info.get('authors', {}).get('author', []) if isinstance(author, dict)],
            'venue': info.get('venue'),
            'year': info.get('year'),
            'abstract': info.get('abstract', 'No abstract available'),
            'citationCount': info.get('citationCount', 0),
            'url': info.get('url')
        }
        papers.append(paper)
    
    return papers

def test():
    info = {'authors': {'author': [{'@pid': '09/3666', 'text': 'Lei Chen'}, {'@pid': '69/2980', 'text': 'Qun-Xiong Zhu'}, {'@pid': '143/0525', 'text': 'Yan-Lin He'}]}, 'title': 'Adversarial Attacks for Neural Network-Based Industrial Soft Sensors: Mirror Output Attack and Translation Mirror Output Attack.', 'venue': 'IEEE Trans. Ind. Informatics', 'volume': '20', 'number': '2', 'pages': '2378-2386', 'year': '2024', 'type': 'Journal Articles', 'access': 'closed', 'key': 'journals/tii/ChenZH24', 'doi': '10.1109/TII.2023.3291717', 'ee': 'https://doi.org/10.1109/TII.2023.3291717', 'url': 'https://dblp.org/rec/journals/tii/ChenZH24'}
    print([author.get('text') for author in info.get('authors').get('author')])

if __name__ == "__main__":
    queries = ["adversarial attack"]
    results = search_for_papers_dblp(queries)
    print(results)