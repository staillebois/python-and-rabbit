import asyncio
# import logging
import time

import aio_pika


async def main() -> None:
    # logging.basicConfig(level=logging.DEBUG)
    connection = await aio_pika.connect_robust(
        "amqp://user:password@localhost/",
    )

    queue_name = "test_queue"

    async with connection:
        # Creating channel
        channel = await connection.channel()

        # Will take no more than 10 messages in advance
        await channel.set_qos(prefetch_count=1)

        # Declaring queue
        queue = await channel.declare_queue(queue_name, arguments={'x-max-priority': 120})

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(message.body)
                    time.sleep(2)

                    # if queue.name in message.body.decode():
                    #     break


if __name__ == "__main__":
    asyncio.run(main())
