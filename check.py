import asyncio
import cognee

async def check():
    results = await cognee.recall(
        "Which companies did I apply to?",
        datasets=["job_applications"]
    )
    for r in results:
        print(r.text)

asyncio.run(check())