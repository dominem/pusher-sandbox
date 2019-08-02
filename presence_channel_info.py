import secrets
import pusher


pusher_client = pusher.Pusher(
    app_id=secrets.APP_ID,
    key=secrets.KEY,
    secret=secrets.SECRET,
    cluster=secrets.CLUSTER,
    ssl=secrets.SSL
)


print(pusher_client.channel_info('presence-channel', ['user_count']))
