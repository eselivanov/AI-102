# # coding: utf-8

#--------------------------------------
# Azure AI Content Safety client library for Python - version 1.0.0
# https://learn.microsoft.com/en-us/python/api/overview/azure/ai-contentsafety-readme?view=azure-python
# https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-documentintelligence_1.0.2/sdk/contentsafety

# Install the package:
# pip install azure-ai-contentsafety

# Get the endpoint for the Azure AI Content Safety service resource:
# az cognitiveservices account show --name "resource-name" --resource-group "resource-group-name" --query "properties.endpoint"
#--------------------------------------

"""
    FILE: analyze_text.py

    DESCRIPTION:
    This sample demonstrates how to ...

    USAGE:
    python analyze_text.py

    See pricing: https://azure.microsoft.com/en-in/pricing/details/cognitive-services/content-safety/
    Free tier: 
    - 5,000 text records per month
    - 5,000 images per month

    Set the environment variables with your own values before running the sample:
    1) CONTENT_SAFETY_ENDPOINT - the endpoint to your Content SAfety resource.
    2) CONTENT_SAFETY_KEY - your Content SAfety API key.

"""

import os
from azure.core.exceptions import HttpResponseError

def analyze_text():
    
    # [START analyze_text]
    from azure.ai.contentsafety import ContentSafetyClient
    from azure.ai.contentsafety.models import TextCategory
    from azure.core.credentials import AzureKeyCredential
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

    # [END analyze_text]


if __name__ == "__main__":
    #    analyze_text()
    from dotenv import find_dotenv, load_dotenv

    try:
        load_dotenv(find_dotenv)
        analyze_text()
    except HttpResponseError as error:
         # Examples of how to check an HttpResponseError
         # Check by error code:
         if error.error is not None:
            if error.error.code == "InvalidText":
                print(f"Received an invalid text error: {error.error}")
            if error.error.code == "InvalidRequest":
                print(f"Received an invalid request error: {error.error}")
            # Raise the error again after printing it
            raise
            # If the inner error is None and then it is possible to check the message to get more information:
            if "Invalid request".casefold() in error.message.casefold():
                print(f"Uh-oh! Seems there was an invalid request: {error}")
            # Raise the error again
            raise