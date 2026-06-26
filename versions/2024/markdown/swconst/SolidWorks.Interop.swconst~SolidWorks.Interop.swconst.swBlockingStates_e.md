---
title: "swBlockingStates_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swBlockingStates_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBlockingStates_e.html"
---

# swBlockingStates_e Enumeration

Blocking states.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swBlockingStates_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swBlockingStates_e
```

### C#

```csharp
public enum swBlockingStates_e : System.Enum
```

### C++/CLI

```cpp
public enum class swBlockingStates_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swEditorBlock | 4 = A valid return value for IModelDoc2::GetBlockingState , but it is not a valid input for IModelDoc2::SetBlockingState ; editing or inserting blocks are blocked |
| swEditSketchAllowExitBlock | 8 = Block model changes but allow sketching and exiting sketch edit mode |
| swEditSketchBlock | 5 = A block is being edited in the drawing |
| swFullBlock | 1 = Most actions are blocked; you cannot edit features, add features, change views (rotate, pan, and so on), exit the SOLIDWORKS software, or change a document; however, you can open a document |
| swModifyBlock | 2 = Similar to swFullBlock except that view-related (rotate, pan, and so on) operations are not blocked |
| swNoBlock | 0 = No actions are blocked |
| swPartialModifyBlock | 3 = Similar to swModifyBlock except that you can change documents |
| swSystemBlock | 6 = Similar to swFullBlock except that you cannot open a document |
| swViewOnlyBlock | 7 = A valid return value for IModelDoc2::GetBlockingState when a document is open in View only/Selective open mode; not a valid input for IModelDoc2::SetBlockingState |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
