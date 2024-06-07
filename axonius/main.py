import asyncio
import time

pages = {
    1: {
        'items': [1, 2, 3]
    },
    2: {
        'items': [11, 12, 13]
    },
    3: {
        'items': [21, 22, 23]
    },
    4: {
        'items': [31, 32, 33]
    }
}


async def get_page(page):
    await asyncio.sleep(1)
    return pages[page]


async def get_all_chars(page):
    print(f"page {page} - {time.time()}")
    res = await get_page(page)
    return res['items']


async def main():
    tasks = [get_all_chars(page) for page in range(1, 5)]
    future = await asyncio.gather(*tasks)
    for result in future:
        for c in result:
            print(c)
            time.sleep(0.5)


if __name__ == '__main__':
    asyncio.run(main())
