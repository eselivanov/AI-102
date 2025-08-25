# Azure AI Content Safety client library for Python - version 1.0.0
# https://learn.microsoft.com/en-us/python/api/overview/azure/ai-contentsafety-readme?view=azure-python
#
# Install the package:
# pip install azure-ai-contentsafety

# Get the endpoint for the Azure AI Content Safety service resource:
# az cognitiveservices account show --name "resource-name" --resource-group "resource-group-name" --query "properties.endpoint"

import os
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import TextCategory
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions

key = os.environ["CONTENT_SAFETY_KEY"]
endpoint = os.environ["CONTENT_SAFETY_ENDPOINT"]

# Create a Content Safety client
client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

# Construct a request
request = AnalyzeTextOptions(text="You are an idiot")

# Analyze text
try:
    response = client.analyze_text(request)
except HttpResponseError as e:
    print("Analyze text failed.")
    if e.error:
        print(f"Error code: {e.error.code}")
        print(f"Error message: {e.error.message}")
        raise
    print(e)
    raise

hate_result = next(item for item in response.categories_analysis if item.category == TextCategory.HATE)
self_harm_result = next(item for item in response.categories_analysis if item.category == TextCategory.SELF_HARM)
sexual_result = next(item for item in response.categories_analysis if item.category == TextCategory.SEXUAL)
violence_result = next(item for item in response.categories_analysis if item.category == TextCategory.VIOLENCE)

if hate_result:
    print(f"Hate severity: {hate_result.severity}")
if self_harm_result:
    print(f"SelfHarm severity: {self_harm_result.severity}")
if sexual_result:
    print(f"Sexual severity: {sexual_result.severity}")
if violence_result:
    print(f"Violence severity: {violence_result.severity}")