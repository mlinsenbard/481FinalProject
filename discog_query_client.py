
import discogs_client

user_agent = "MXPO/1.0"

token = "DfVagowbDawoqOLydLgUTbQqjEUUlYJXTptoUUvl"

d = discogs_client.Client(user_agent, user_token=token)

results = d.search("Gorillaz")

print results[0]