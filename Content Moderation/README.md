# Content Moderation

https://learn.microsoft.com/en-us/python/api/overview/azure/ai-contentsafety-readme?view=azure-python

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