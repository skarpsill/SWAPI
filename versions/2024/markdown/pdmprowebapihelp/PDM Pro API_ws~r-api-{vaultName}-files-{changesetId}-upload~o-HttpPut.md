---
title: "api/{vaultName}/files/{changesetId}/upload (Put)"
project: ""
interface: "r-api-{vaultName}-files-{changesetId}-upload"
member: "o-HttpPut"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{changesetId}-upload~o-HttpPut.html"
---

# api/{vaultName}/files/{changesetId}/upload (Put)

PDM Pro API Web Service

| Put | api/{vaultName}/files/{changesetId}/upload |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Stage Resource Group : api/{vaultName}/files/{changesetId}/upload (Put) |
| --- |

Description

PUT: api/{vaultname}/files/{changesetId}/upload Upload file to changeset to add files operations

Uploads a changeset.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| changesetId | (URI parameter) Changeset ID (required) | integer |

Response (application/json, text/json)

Returns the changeset ID

#### Sample Data

```
1
```

Response (application/xml, text/xml)

Returns the changeset ID

#### Sample Data

```
<int xmlns="http://schemas.microsoft.com/2003/10/Serialization/">1</int>
```

See Also

[Stage Resource Group](PDM%20Pro%20API_ws~g-ab7aa0c7-6261-4685-9682-f6301732b3ab.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
