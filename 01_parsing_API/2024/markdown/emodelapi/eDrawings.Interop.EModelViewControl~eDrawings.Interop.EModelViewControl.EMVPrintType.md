---
title: "EMVPrintType Enumeration"
project: "eDrawings API Help"
interface: "EMVPrintType"
member: ""
kind: "enum"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVPrintType.html"
---

# EMVPrintType Enumeration

Print types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum EMVPrintType
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As EMVPrintType
```

### C#

```csharp
public enum EMVPrintType : System.Enum
```

### C++/CLI

```cpp
public enum class EMVPrintType : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| eOneToOne | 2 = Print actual size; for drawings only |
| ePrintSelection | 3 = Not used |
| eScaled | 4 = Scaled; scaling factor and offsets apply |
| eScaleToFit | 1 = Scale to fit; for drawings only |
| eWYSIWYG | 0 = What You See Is What You Get; for parts, assemblies, and drawings |

## See Also

[eDrawings.Interop.EModelViewControl Namespace](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl_namespace.html)
