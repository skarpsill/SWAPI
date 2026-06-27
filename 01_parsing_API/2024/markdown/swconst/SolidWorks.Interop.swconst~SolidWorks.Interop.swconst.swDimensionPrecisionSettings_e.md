---
title: "swDimensionPrecisionSettings_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDimensionPrecisionSettings_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionPrecisionSettings_e.html"
---

# swDimensionPrecisionSettings_e Enumeration

Precision settings for dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDimensionPrecisionSettings_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDimensionPrecisionSettings_e
```

### C#

```csharp
public enum swDimensionPrecisionSettings_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDimensionPrecisionSettings_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDoNotChangePrecisionSetting | -1 = Used by IDisplayDimension::SetPrecision2 only |
| swPrecisionFollowsDocumentSetting | -2 = Precision equals the document default precision value |
| swTolerancePrecisionFollowsNominal | -3 = Tolerance precision equals the dimension precision value |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
