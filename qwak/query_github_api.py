import re
from typing import List
import requests


def exec_queries(queries: List[str]):
    total_count = 0
    items = []
    for query in queries:
        q_count, q_items = exec_query(query)
        total_count += q_count
        items.extend(q_items)

    return total_count, items


def get_next_page_query(res):
    if 'Link' in res.headers:
        link = res.headers['Link']
        queries = re.split(r'; rel="\w+"', link)

        queries.remove('')
        query = queries[0] if len(queries) <= 2 else queries[1]
        query = query[query.index('<')+1:-1]

        return query
    return None


def exec_query(query: str):
    res = requests.get(query)
    result = res.json()

    total_count = result['total_count']
    items = result['items']

    query = get_next_page_query(res)

    while query:
        res = requests.get(query)
        result = res.json()
        items.extend(result['items'])
        query = get_next_page_query(res)

    return total_count, items


if __name__ == '__main__':
    query = "https://api.github.com/search/issues?q=factory in:file language:java repo:openjdk/jdk"
    exec_query(query)
