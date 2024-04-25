import re
from typing import List
import requests
import math


def exec_queries(queries: List[str]):
    total_count = 0
    items = []
    exception = None
    for query in queries:
        try:
            q_count, q_items = exec_query(query)
        except Exception as e:
            exception = e
            break
        total_count += q_count
        items.extend(q_items)

    return total_count, items, exception


def get_next_page_query(res):
    if 'Link' in res.headers:
        link = res.headers['Link']
        ma = re.search(r'(?<=<).+(?=>; rel="next")', link)
        if not ma:
            return None

        query = ma.group()
        return query

    return None


def exec_query(query: str):
    res = requests.get(f"{query}&per_page=1")
    result = res.json()
    if not res.ok:
        raise Exception(f"query failed: {query}\nstatus_code={res.status_code}\nmessage: {result['message']}")

    total_count = result['total_count']
    if total_count == 0:
        return 0, []
    rate_limit = int(res.headers['X-RateLimit-Remaining'])
    if rate_limit == 0:
        raise Exception(f"Api rate limit equals {rate_limit}. Handled query: {query}")
    items = []
    page_size = max(math.ceil(total_count / rate_limit), 1000)
    query = f"{query}&per_page={page_size}"

    while query:
        res = requests.get(query)
        result = res.json()
        items.extend(result.get('items', []))
        query = get_next_page_query(res)

    return total_count, items


if __name__ == '__main__':
    # query = "https://api.github.com/search/issues?q=factory in:file language:java repo:openjdk/jdk"
    with open('queries.txt', 'r') as file:
        context = file.read()
        queries = map(str.strip, context.split('\n'))

    total_count, items, e = exec_queries(queries)
    with open('output.txt', 'w') as file:
        if e:
            file.write(f"{e}\n\n")

        file.write(f"total_count: {total_count}\n")
        file.write(f"items: {items}")
