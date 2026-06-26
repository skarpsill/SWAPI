---
title: "swPackAndGoSaveStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPackAndGoSaveStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPackAndGoSaveStatus_e.html"
---

# swPackAndGoSaveStatus_e Enumeration

Status of each document intended for Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPackAndGoSaveStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPackAndGoSaveStatus_e
```

### C#

```csharp
public enum swPackAndGoSaveStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPackAndGoSaveStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPackAndGoSaveStatus_FileAlreadyExist | 2 = File already exists |
| swPackAndGoSaveStatus_SaveError | 4 = Save error |
| swPackAndGoSaveStatus_SaveToEmpty | 3 = Saving empty file |
| swPackAndGoSaveStatus_Succeed | 0 = Success |
| swPackAndGoSaveStatus_UserInputNotCorrect | 1 = User input not correct |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
