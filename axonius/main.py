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
    if page == 1:
        await asyncio.sleep(1)
    return pages[page]


async def get_all_chars(page):
    print(f"page {page} - {time.time()}")
    res = await get_page(page)
    return res['items']


async def main():
    tasks = [await get_all_chars(1), await get_all_chars(2)]
    # results = await asyncio.gather(*tasks)

    for result in tasks:
        for c in result:
            print(c)

    task = await get_all_chars(3)
    for c in task:
        print(c)


if __name__ == '__main__':
    asyncio.run(main())
