import asyncio
import cognee

async def main():
    await cognee.forget(everything=True)
    await cognee.remember(
        "I applied to Razorpay on June 29. Role: AI Engineer.",
        dataset_name="job_tracker"
    )
    results = await cognee.recall(
        "Which companies did I apply to?",
        datasets=["job_tracker"]
    )
    print(results)

asyncio.run(main())