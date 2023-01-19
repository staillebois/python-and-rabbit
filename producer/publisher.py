import asyncio

import aio_pika


async def main() -> None:
    connection = await aio_pika.connect_robust(
        "amqp://user:password@localhost/",
    )

    async with connection:
        routing_key = "test_queue"

        channel = await connection.channel()

        for i in range(100):
            priority = 120 if i % 5 == 0 else 1
            await channel.default_exchange.publish(
                aio_pika.Message(body=f"Hello {i} {routing_key}".encode(), priority=priority),
                routing_key=routing_key,
            )

if __name__ == "__main__":
    asyncio.run(main())
