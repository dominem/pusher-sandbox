import datetime
import secrets
import pusher


NOW = datetime.datetime.now()


channels_client = pusher.Pusher(
    app_id=secrets.APP_ID,
    key=secrets.KEY,
    secret=secrets.SECRET,
    cluster=secrets.CLUSTER,
    ssl=secrets.SSL
)


message = {
    'message': f'Now is {NOW.isoformat()}',
}


channels_client.trigger(
    secrets.CHANNEL,
    secrets.EVENT,
    message
)
