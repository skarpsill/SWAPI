---
title: "swcCostingType_e Enumeration"
project: "SOLIDWORKS Costing API Help"
interface: "swcCostingType_e"
member: ""
kind: "enum"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcCostingType_e.html"
---

# swcCostingType_e Enumeration

Costing types.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swcCostingType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swcCostingType_e
```

### C#

```csharp
public enum swcCostingType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swcCostingType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swcCostingType_Common | 0 = Common Costing analysis; i.e., costing common to all Costing analyses (see Remarks ) |
| swcCostingType_Machining | 2 = Machining Costing analysis; includes 3D printing, casting, machining, and plastic |
| swcCostingType_SheetMetal | 1 = Sheet metal Costing analysis; includes machined plate and sheet metal |
| swcCostingType_Structural | 3 = Structural Costing analysis; includes 3D printing, casting, machining, and plastic |

## Remarks

A complete Costing analysis includes the common Costing analysis and a specific Costing analysis; i.e., machining, sheet metal, or structural.

## See Also

[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
