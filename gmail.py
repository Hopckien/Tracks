from simplegmail import Gmail
from simplegmail.query import construct_query



gmail = Gmail()

labels = gmail.list_labels()
given_label = list(filter(lambda x: x.name == 'given', labels))[0]

# Unread messages in your inbox
# messages = gmail.get_unread_inbox()

messages = gmail.get_unread_inbox(labels=[given_label])

# messages = gmail.list_labels()
# Starred messages
# messages = gmail.get_starred_messages()

# ...and many more easy to use functions can be found in gmail.py!

# Print them out!
lines = []
for message in messages:
#     # print("To: " + message.recipient)
#     # print("From: " + message.sender)
#     # print("Subject: " + message.subject)
#     # # print("Date: " + message.date)
#     # print("Preview: ")
#     # print(type(message.snippet))
    lines.append(message.snippet+'\n')

# print(lines)


with open('tracks.txt','w',encoding="utf-8") as file:
    file.writelines(lines)



#    # print("Message Body: " + message.plain)  # or message.html
#     print("Message Body: " + message.labels)  # or message.html
# for l in labels:
#     print(l)
# print(given_label)
