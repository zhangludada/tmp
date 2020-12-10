import asyncio

async def w(n):
    print("star--{}".format(n))
    await asyncio.sleep(0.1)
    print("end--{}".format(n))
    return n

async def main():
    ls=[asyncio.create_task(w(x)) for x in range(10)]
    done,pending=await asyncio.wait(ls)
    for i in done:
        print(str(i).split(' ')[-1])


asyncio.run(main())