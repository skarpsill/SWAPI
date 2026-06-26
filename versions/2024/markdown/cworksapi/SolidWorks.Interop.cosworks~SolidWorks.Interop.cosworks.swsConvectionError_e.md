---
title: "swsConvectionError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsConvectionError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsConvectionError_e.html"
---

# swsConvectionError_e Enumeration

Convection errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsConvectionError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsConvectionError_e
```

### C#

```csharp
public enum swsConvectionError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsConvectionError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsConvectionErrorEmptyArray | 5 = Empty array (no faces or shell edges selected) |
| swsConvectionErrorFacesAndShellEdgesAllowed | 1 = Only faces and shell edges are allowed |
| swsConvectionErrorInvalidArray | 4 = Invalid array |
| swsConvectionErrorInvalidStudyType | 3 = Study type is invalid for convection |
| swsConvectionErrorSelectFacesOrShellEdge | 2 = Select faces or shell edge |
| swsConvectionErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
