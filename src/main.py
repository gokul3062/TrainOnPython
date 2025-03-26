import asyncio

async def my_task():
    print("Inside async function")
    await asyncio.sleep(1)  # Non-blocking wait
    print("Task completed")

async def main():
    print("Start")
    asyncio.create_task(my_task())  # Schedules task but does NOT wait
    print("End")
    await asyncio.sleep(2)  # Keeps the event loop running

asyncio.run(main())  # Starts event loop manually
