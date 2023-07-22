from pyrogram import Client

api_id =  21216598
api_hash = '31616e8347a66fc3a20270dd3a85ff4a'
app = Client('sessions/aeoenzbxsx', api_id=api_id, api_hash=api_hash)
app.connect()

app.send_message('@el7ot_support', 'hello')

app.disconnect()