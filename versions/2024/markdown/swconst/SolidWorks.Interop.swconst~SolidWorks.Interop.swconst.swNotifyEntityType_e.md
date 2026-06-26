---
title: "swNotifyEntityType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swNotifyEntityType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNotifyEntityType_e.html"
---

# swNotifyEntityType_e Enumeration

Notification entity types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swNotifyEntityType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swNotifyEntityType_e
```

### C#

```csharp
public enum swNotifyEntityType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swNotifyEntityType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swNotifyBlockDef | Obsolete |
| swNotifyComponent | 2 = Assembly component is being added, renamed, or deleted |
| swNotifyComponentInternal | 8 = Assembly component is internal to the assembly |
| swNotifyConfiguration | 1 = Configuration is being added, renamed, or deleted |
| swNotifyDerivedConfiguration | 4 = Derived configuration is being added, renamed, or deleted |
| swNotifyDrawingSheet | 5 = Drawing sheet is being added, renamed, or deleted |
| swNotifyDrawingView | 6 = Drawing view is being added, renamed, or deleted |
| swNotifyFeature | 3 = Feature is being added, renamed, or deleted |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
