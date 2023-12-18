**python 3.6 or grater version**

**install rasa**
**create a conda environment with more than py 3.6 environment that satisfy the rasa**
conda activate <your environment name>
pip install rasa


**telegram api**
use telegram botfather for create the bot with unique name
**api connection** 
curl -X POST "https://api.telegram.org/botYOUR_TELEGRAM_BOT_TOKEN/setWebhook?url=https://YOUR_NGROK_URL/webhooks/telegram/webhook"


**start rasa server and enable api**
rasa run --enable-api --cors "*"
rasa run --enable-api
rasa run
rasa train

**http tunneling server**
ngrok http 5005