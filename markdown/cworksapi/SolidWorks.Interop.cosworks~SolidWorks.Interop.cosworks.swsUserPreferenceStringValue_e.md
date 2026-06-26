---
title: "swsUserPreferenceStringValue_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsUserPreferenceStringValue_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsUserPreferenceStringValue_e.html"
---

# swsUserPreferenceStringValue_e Enumeration

User preference string values

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsUserPreferenceStringValue_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsUserPreferenceStringValue_e
```

### C#

```csharp
public enum swsUserPreferenceStringValue_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsUserPreferenceStringValue_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsEMailAccount | 7 |
| swsEMailPassword | 8 |
| swsEMailPort | 6 |
| swsEMailSendFrom | 3 |
| swsEMailSendTo | 4 |
| swsEMailSMTP | 5 |
| swsSolidWorksDocumentFolderSubFolderLocation | 1 = Get or set the results sub-folder; corresponds to Simulation > Options > Default Options > Results > Results Folder > SOLIDWORKS document folder > Under sub folder |
| swsSolidWorksUserDefinedReportFolderLocation | 2 = Get or set the user-defined report folder; corresponds to Simulation > Options > Default Options > Report > Report publish options > Report folder > User defined |
| swsUserDefinedResultFolderLocation | 0 = Get or set the user-defined results folder; Simulation > Options > Default Options > Results > Results Folder > User defined |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
