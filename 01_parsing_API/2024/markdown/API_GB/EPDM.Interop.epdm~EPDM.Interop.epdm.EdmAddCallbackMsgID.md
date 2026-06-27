---
title: "EdmAddCallbackMsgID Enumeration"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmAddCallbackMsgID"
member: ""
kind: "enum"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmAddCallbackMsgID.html"
---

# EdmAddCallbackMsgID Enumeration

Message IDs used in the message box during an add operation.

## Syntax

### Visual Basic

```vb
Public Enum EdmAddCallbackMsgID
   Inherits System.Enum
```

### C#

```csharp
public enum EdmAddCallbackMsgID : System.Enum
```

### C++/CLI

```cpp
public enum class EdmAddCallbackMsgID : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| EdmAddMsg_ClearUnique | 2 = Copy over the existing file that has unique values? |
| EdmAddMsg_DeleteSource | 5 = Could not delete a source file during a move operation |
| EdmAddMsg_FileFmtReadError | 4 = File could not be read by the file format plugin |
| EdmAddMsg_GenericError | 0 = Generic error |
| EdmAddMsg_MissingPluginComponent | 3 = File format plugin component is missing |
| EdmAddMsg_ReplaceLocal | 1 = Replace the existing file with the same name? |

## See Also

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
