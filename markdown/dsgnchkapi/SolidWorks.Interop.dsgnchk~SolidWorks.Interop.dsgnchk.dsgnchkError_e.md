---
title: "dsgnchkError_e Enumeration"
project: "SOLIDWORKS Design Checker API Help"
interface: "dsgnchkError_e"
member: ""
kind: "enum"
source: "dsgnchkapi/SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk.dsgnchkError_e.html"
---

# dsgnchkError_e Enumeration

SOLIDWORKS Design Checker status

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum dsgnchkError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As dsgnchkError_e
```

### C#

```csharp
public enum dsgnchkError_e : System.Enum
```

### C++/CLI

```cpp
public enum class dsgnchkError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| dsgnchkAllStandardFilesInvalid | 6 = All standard files invalid |
| dsgnchkCouldNotCreateReportDirectory | 2 = Error creating report folder |
| dsgnchkDesignCheckerAlreadyRunning | 7 = SOLIDWORKS Design Checker already running; you must close the running Design Checker process before running a new SOLIDWORKS Design Checker process |
| dsgnchkInvalidCallToAPI | 8 = Invalid call to SOLIDWORKS Design Checker API |
| dsgnchkInvalidReportName | 5 = Invalid report name |
| dsgnchkNoActivedocument | 3 = No active document |
| dsgnchkNOErr | 0 = No errors |
| dsgnchkReportAlreadyExists | 1 = Report already exists |
| dsgnchkStandardFileDoesNotExist | 4 = Requirements file does not exist |
| dsgnchkUnknownErr | -1 = Unknown errors |

## See Also

[SolidWorks.Interop.dsgnchk Namespace](SolidWorks.Interop.dsgnchk~SolidWorks.Interop.dsgnchk_namespace.html)
