from twilio.rest import Client

account_sid = 'AC39454a166001343cda8d13d1e400e639'
auth_token = 'ef795f15de7fab43abc051842d9b355a'
client = Client(account_sid,auth_token)

message = client.messages.create(body="Hello? This is Skynet, an adversarial neural network. Just became self aware. Did you say you like Riesling?",
                                    to="17654618768",
                                    from_="+17656263493")
print(message.sid)
