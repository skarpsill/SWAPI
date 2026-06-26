---
title: "swTabSlotFeatureHeightType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swTabSlotFeatureHeightType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTabSlotFeatureHeightType_e.html"
---

# swTabSlotFeatureHeightType_e Enumeration

Types of tab height calculations in Tab and Slot groups.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swTabSlotFeatureHeightType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swTabSlotFeatureHeightType_e
```

### C#

```csharp
public enum swTabSlotFeatureHeightType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swTabSlotFeatureHeightType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| Blind | 0 = Specify a tab height |
| OffsetFromSurface | 2 = Specify an offset and the slot face from which to offset the tab |
| UpToSurface | 1 = The height is calculated internally in reference to the slot face |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
