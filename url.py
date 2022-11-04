import json
import requests


url = "https://dailyprayer.abdulrcs.repl.co/api/samarqand"
response = requests.get(url)
data = response.json()
print(data['city'])
print(data['date'])
for prayer in data["today"]:
  print(prayer + ": " + data["today"][prayer])
# If you want to request for tomorrow prayer's time:
# for prayer in data["tomorrow"]:
#     print(prayer + ": " + data["tomorrow"][prayer])
# url = "https://dailyprayer.abdulrcs.repl.co/api/andijon"
#     response = requests.get(url)
#     data = response.json()
#     # await message.answer(data['city'])
#     # await message.answer(data['date'])
#     for prayer in data["today"]:
#         await message.answer(prayer + ": " + data["today"][prayer])
#     for prayer in data["tomorrow"]:
#         print(prayer + ": " + data["tomorrow"][prayer])



# import requests
# import json
#
# inputs = str(input(""))
# url = "https://api.pray.zone/v2/times/today.json?city=" + inputs
#
# responses = requests.get(url)
# rest = json.loads(responses.text)
# print(rest)