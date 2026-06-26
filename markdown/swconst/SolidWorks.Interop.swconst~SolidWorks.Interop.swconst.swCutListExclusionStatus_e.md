---
title: "swCutListExclusionStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCutListExclusionStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCutListExclusionStatus_e.html"
---

# swCutListExclusionStatus_e Enumeration

Status of excluding the selected faces and features in the cut list sort exclusion list.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCutListExclusionStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCutListExclusionStatus_e
```

### C#

```csharp
public enum swCutListExclusionStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCutListExclusionStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCutListExclusionStatus_InvalidEntities | 1 = Selected faces and features are invalid because they are not of selection type BODYFEATURE or FACE. Other examples of face and features that are invalid for exclusion: Chamfers that remove an entire face. Suppressed features. Features that create new bodies from sketches, such as boss-extrude, revolve, and sweep. Certain sheet metal features. |
| swCutListExclusionStatus_Success | 0 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
