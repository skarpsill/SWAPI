---
title: "api/{vaultName}/checkin/addfiles/{changesetId} (Put)"
project: ""
interface: "r-api-{vaultName}-checkin-addfiles-{changesetId}"
member: "o-HttpPut"
kind: "topic"
source: "pdmprowebapihelp/PDM Pro API_ws~r-api-{vaultName}-checkin-addfiles-{changesetId}~o-HttpPut.html"
---

# api/{vaultName}/checkin/addfiles/{changesetId} (Put)

PDM Pro API Web Service

| Put | api/{vaultName}/checkin/addfiles/{changesetId} |
| --- | --- |

Spacing

Collapse All

Expand All

| PDM Pro API Web Service > Stage Resource Group : api/{vaultName}/checkin/addfiles/{changesetId} (Put) |
| --- |

Description

PUT: api/{vaultname}/checkin/addfiles/{changesetId=0} Upload files or document ids to changeset to the check in operation

Uploads files to the specified changeset for checkin.

Parameters

| Name | Description | Data Type |
| --- | --- | --- |
| vaultName | (URI parameter) Vault name (required) | string |
| changesetId | (URI and response parameter) Changeset ID (URI required) | integer |
| References | (Response) Array of FileInfo objects; each FileInfo consists of: File (File object that consists of: FileId (integer) FileName (string) ) Folder (Folder object that consist of: FolderId (integer) FolderPath (string) ) Version (integer) Config (Config object that consists of: ConfigurationName (string) ConfigurationId (integer) ) | Collection of FileInfo |

Response (application/json, text/json)

#### Sample Data

```
{
  "ChangesetId": 1,
  "References": [
    {
      "File": {
        "FileId": 1,
        "FileName": "sample string 2"
      },
      "Folder": {
        "FolderId": 1,
        "FolderPath": "sample string 2"
      },
      "Version": 1,
      "Config": {
        "ConfigurationName": "sample string 1",
        "ConfigurationId": 2
      }
    },
    {
      "File": {
        "FileId": 1,
        "FileName": "sample string 2"
      },
      "Folder": {
        "FolderId": 1,
        "FolderPath": "sample string 2"
      },
      "Version": 1,
      "Config": {
        "ConfigurationName": "sample string 1",
        "ConfigurationId": 2
      }
    }
  ]
}
```

Response (application/xml, text/xml)

#### Sample Data

```
<UploadModel xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.datacontract.org/2004/07/SWPDM.Models">
  <ChangesetId>1</ChangesetId>
  <References>
    <FileInfo>
      <Config>
        <ConfigurationId>2</ConfigurationId>
        <ConfigurationName>sample string 1</ConfigurationName>
      </Config>
      <File>
        <FileId>1</FileId>
        <FileName>sample string 2</FileName>
      </File>
      <Folder>
        <FolderId>1</FolderId>
        <FolderPath>sample string 2</FolderPath>
      </Folder>
      <Version>1</Version>
    </FileInfo>
    <FileInfo>
      <Config>
        <ConfigurationId>2</ConfigurationId>
        <ConfigurationName>sample string 1</ConfigurationName>
      </Config>
      <File>
        <FileId>1</FileId>
        <FileName>sample string 2</FileName>
      </File>
      <Folder>
        <FolderId>1</FolderId>
        <FolderPath>sample string 2</FolderPath>
      </Folder>
      <Version>1</Version>
    </FileInfo>
  </References>
</UploadModel>
```

Remarks

This operation takes a body parameter that consists of an array of document IDs of documents you want to check in. The body must contain a multipart/form-data content type with a unique boundary. A content-type header must match the content type and boundary specified in the body.

Example Content-Type header:

multipart/form-data;boundary=bee21932-0a3e-45a3-957d-e0b5f3e8f12e

Example raw body:

--bee21932-0a3e-45a3-957d-e0b5f3e8f12e
Content-Type: multipart/form-data; boundary = "9e73357f-6a62-452b-a1b8-2b48586435e5"
Content-Disposition: form-data

--9e73357f-6a62-452b-a1b8-2b48586435e5
Content-Type: application/x-www-form-urlencoded
Content-Disposition: form-data

**DocumentId=1006**
--9e73357f-6a62-452b-a1b8-2b48586435e5

--9e73357f-6a62-452b-a1b8-2b48586435e5--

--bee21932-0a3e-45a3-957d-e0b5f3e8f12e--

See Also

[Stage Resource Group](PDM%20Pro%20API_ws~g-ab7aa0c7-6261-4685-9682-f6301732b3ab.html)

|

[PDM Pro API Web Service](PDM%20Pro%20API_ws.html)
