from TikTokLive.client.client import TikTokLiveClient
from TikTokLive.client.logger import LogLevel
from TikTokLive.events import (
    ConnectEvent, GiftEvent, FollowEvent, LikeEvent, ShareEvent, SubscribeEvent
)

# Define a global list to store the credit messages
credits_log = []

client: TikTokLiveClient = TikTokLiveClient(unique_id="@revenant_oc")

@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    message = f"Connected to @{event.unique_id}!"
    client.logger.info(message)
    credits_log.append(message)

@client.on(GiftEvent)
async def on_gift(event: GiftEvent):
    client.logger.info("Received a gift!")
    if event.gift.streakable and not event.streaking:
        message = f"{event.user.unique_id} sent {event.repeat_count}x \"{event.gift.name}\""
    else:
        message = f"{event.user.unique_id} sent \"{event.gift.name}\""
    print(message)
    credits_log.append(message)
    client.logger.info(message)

@client.on(FollowEvent)
async def on_follow(event: FollowEvent):
    # Adjust attribute usage as needed. Assuming event.follow contains follow details.
    message = f"{event.user.unique_id} followed! Details: {event.follow}"
    print(message)
    credits_log.append(message)
    client.logger.info(message)

@client.on(LikeEvent)
async def on_like(event: LikeEvent):
    client.logger.info("Liked the Live!")
    if hasattr(event, 'streakable') and event.like.streakable and not event.streaking:
        message = f"{event.user.unique_id} sent {event.repeat_count}x like(s)"
    else:
        message = f"{event.user.unique_id} sent like(s)"
    print(message)
    credits_log.append(message)
    client.logger.info(message)

@client.on(ShareEvent)
async def on_share(event: ShareEvent):
    client.logger.info("Shared the Live!")
    message = f"{event.user.unique_id} shared the live! Details: {event.share}"
    print(message)
    credits_log.append(message)
    client.logger.info(message)

@client.on(SubscribeEvent)
async def on_subscribe(event: SubscribeEvent):
    client.logger.info("Subscribed!")
    # Adjust attribute usage if event.subscribe is available
    message = f"{event.user.unique_id} subscribed! Details: {event.subscribe}"
    print(message)
    credits_log.append(message)
    client.logger.info(message)

if __name__ == '__main__':
    client.logger.setLevel(LogLevel.INFO.value)
    client.run()
