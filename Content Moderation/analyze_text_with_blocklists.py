# https://learn.microsoft.com/en-us/python/api/overview/azure/ai-contentsafety-readme?view=azure-python#list-text-blocklists
import os
from azure.ai.contentsafety import BlocklistClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError

key = os.environ["CONTENT_SAFETY_KEY"]
endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

# Create a Blocklist client
client = BlocklistClient(endpoint, AzureKeyCredential(key))

try:
    blocklists = client.list_text_blocklists()
    if blocklists:
        print("\nList blocklists: ")
        for blocklist in blocklists:
            print(f"Name: {blocklist.blocklist_name}, Description: {blocklist.description}")
except HttpResponseError as e:
    print("\nList text blocklists failed: ")
    if e.error:
        print(f"Error code: {e.error.code}")
        print(f"Error message: {e.error.message}")
        raise
    print(e)
    raise