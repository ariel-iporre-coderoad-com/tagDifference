import starflex


client = starflex.star_client('10.100.1.71')
# Start
client.put_msg(end_point='/rfid/activeProgram/basic')
# client.post_msg(end_point='/apps/inventory') # inventory started
# Listening for 10 seconds
# client.listen_during(5, end_point='/rfid/events/deepInv?override') # same endpoint
# client.listen_during(5, end_point='/rfid/events?override') # same endpoint
client.listen_during(5, end_point='/rfid/events/allAttribs?override') # same endpoint
print '@#$%#@#$%^$#$%^&%$%^&    after listening'

# Stop time
# client.del_msg(end_point='/apps/inventory')
client.del_msg(end_point='/rfid/activeProgram')
# Return summary
print client.summary()


# print r.content
