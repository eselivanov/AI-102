# Content Moderation

https://learn.microsoft.com/en-us/python/api/overview/azure/ai-contentsafety-readme?view=azure-python

# MS Samples repo
https://github.com/Azure/azure-sdk-for-python/tree/azure-ai-contentsafety_1.0.0/sdk/contentsafety/azure-ai-contentsafety/samples

## Install the package

```
pip install azure-ai-contentsafety
```

## Authenticate the client
### Get the endpoint for the Azure AI Content Safety service resource

```
az cognitiveservices account show --name "resource-name" --resource-group "resource-group-name" --query "properties.endpoint"
```
### 1. Get API key

```
az cognitiveservices account keys list --name "<resource-name>" --resource-group "<resource-group-name>"
```

### 2. Get credentials 

```
credential = AzureKeyCredential("<api_key>")
```

### 3. Pass key to the client

```
content_safety_client = ContentSafetyClient(endpoint, *credential*)
blocklist_client = BlocklistClient(endpoint, *credential*)
```

Contect classification, 4 categories (could be multi-labeled):
- Hate
- Sectual
- Violense
- Self-hard

Severety levels for Text and Image
- 4 levels by default:
[0,1] -> 0
[2.3] -> 2
[4,5] -> 4
[6.7] -> 6

Can be changed using outputType=EightSeverityLevels in request
Then output: 0,1,2,3,4,5,6,7.


