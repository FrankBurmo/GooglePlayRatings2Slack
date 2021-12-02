from google_play_scraper import app
import requests
import json

result = app(
    'app.package.name',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)
print(result)

score = result.get('score')
print(score)
score = round(score, 1)

slack_token = 'xoxb-token'
slack_channel = '#general'
slack_icon_emoji = ':see_no_evil:'
slack_user_name = 'Google Play bot'

def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': text,
        'icon_emoji': slack_icon_emoji,
        'username': slack_user_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()	

slack_info = 'Our rating on Google Play is *{}* of 5'.format(
  score)

post_message_to_slack(slack_info)
