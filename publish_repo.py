from dlhub_sdk import DLHubClient
#client = DLHubClient(force_login=True)
client = DLHubClient()
containerid = client.publish_repository("https://github.com/ericblau/dlhub_noop_publish")

print(f"Container ID is: {containerid}")
