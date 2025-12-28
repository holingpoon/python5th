email = {
  "From": "j.smith@example.com",
  "To": "zed.shaw@example.com",
  "Subject": "I HAVE AN AMAZING INVESTMENT FOR YOU!!"
}

print(email["From"])
print(email["To"])
print(email["Subject"])

messages = [
  {"to": 'Sun', "from": 'Moon', "message": 'Hi!'},
  {"to": 'Moon', "from": 'Sun', "message": 'What do you want Sun?'},
  {"to": 'Sun', "from": 'Moon', "message": "I'm awake!"},
  {"to": 'Moon', "from": 'Sun', "message": 'I can see that Sun.'}
]

# The 'to' and 'from' values are incorrect, this conversation makes more sense
print(f"{messages[0]["to"]}: {messages[0]["message"]}")
print(f"{messages[1]["to"]}: {messages[1]["message"]}")
print(f"{messages[2]["to"]}: {messages[2]["message"]}")
print(f"{messages[3]["to"]}: {messages[3]["message"]}")
