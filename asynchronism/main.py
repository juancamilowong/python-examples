"""
Example using non-blocking tasks
"""
import asyncio
import random 

async def task(name):
    seconds = random.randint(1, 5)
    print(f"task {name} started with {seconds} stop")
    await asyncio.sleep(seconds)
    print(f"task {name} finishing")

async def main():
    await asyncio.gather(task("one"), task("two"), task("three"))

asyncio.run(main())