# https://learn.microsoft.com/en-us/python/api/overview/azure/ai-contentsafety-readme?view=azure-python#analyze-text-with-blocklists
import os
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.contentsafety.models import AnalyzeTextOptions
from azure.core.exceptions import HttpResponseError

key = os.environ["CONTENT_SAFETY_KEY"]
endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

# Create a Content Safety client
client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

blocklist_name = "TestBlocklist"
input_text = "I h*te you and I want to k*ll you."

try:
    # After you edit your blocklist, it usually takes effect in 5 minutes, please wait some time before analyzing with blocklist after editing.
    analysis_result = client.analyze_text(
        AnalyzeTextOptions(text=input_text, blocklist_names=[blocklist_name], halt_on_blocklist_hit=False)
    )
    if analysis_result and analysis_result.blocklists_match:
        print("\nBlocklist match results: ")
        for match_result in analysis_result.blocklists_match:
            print(
                f"BlocklistName: {match_result.blocklist_name}, BlockItemId: {match_result.blocklist_item_id}, "
                f"BlockItemText: {match_result.blocklist_item_text}"
            )
except HttpResponseError as e:
    print("\nAnalyze text failed: ")
    if e.error:
        print(f"Error code: {e.error.code}")
        print(f"Error message: {e.error.message}")
        raise
    print(e)
    raise