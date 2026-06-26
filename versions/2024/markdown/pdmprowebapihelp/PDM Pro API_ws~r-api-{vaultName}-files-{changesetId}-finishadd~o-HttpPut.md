---
title: "api/{vaultName}/files/{changesetId}/finishadd (Put)"
project: ""
interface: "r-api-{vaultName}-files-{changesetId}-finishadd"
member: "o-HttpPut"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-files-{changesetId}-finishadd~o-HttpPut.html"
---

# api/{vaultName}/files/{changesetId}/finishadd (Put)

PDM Pro API Web Service

| Put | api/{vaultName}/files/{changesetId}/finishadd |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Stage Resource Group : api/{vaultName}/files/{changesetId}/finishadd (Put) |
| --- |

Description

PUT: api/{vaultName}/files/{changesetId}/finishadd Finish of add file operation. This method adds files from changeset to the vault.

Adds files in the specified changeset to the vault.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| changesetId | (URI parameter) Changeset ID (required) | integer |
| Version | (Response) A Version model that consists of: Major (integer) Minor (integer) Build (integer) Revision (integer) MajorRevision (integer) MinorRevision (integer) Member of HttpResponseMessage model | Version |
| Content | (Response) GUID of the add operation; use the GUID to query the progress/status of the add operation (see api/{vaultName}/progress/{guid}/status ) Member of HttpResponseMessage model | HttpContent |
| StatusCode | (Response) Status code; see https://en.wikipedia.org/wiki/List_of_HTTP_status_codes Member of HttpResponseMessage model | HttpStatusCode |
| ReasonPhrase | (Response) Reason Member of HttpResponseMessage model | string |
| Headers | (Response) Array of headers Member of HttpResponseMessage model | Collection of Object |
| RequestMessage | (Response) An HttpRequestMessage object that consists of: Version (Version model) Content (HttpContent object consisting of Headers array) Method (HttpMethod object consisting of Method string) RequestUri (URI) Headers (Array of objects) Properties (Dictionary of string [key] and Object [value] Member of HttpResponseMessage model | HttpRequestMessage |
| IsSuccessStatusCode | (Response) True if successful, false if not Member of HttpResponseMessage model | boolean |

See Also

[Stage Resource Group](PDM%20Pro%20API_ws~g-ab7aa0c7-6261-4685-9682-f6301732b3ab.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
