##--------------##
  # Count the number of user events performed by MacBookPro users.
  # Output the result along with the event name.
  # Sort the result based on the event count in the descending order.
##--------------##

# Import your libraries
import pandas as pd

# Start writing code
playbook_events.head()

df = playbook_events
df = df[df["device"] == "macbook pro"]
df.groupby(["event_name"]).size().to_frame("event_count").reset_index()
