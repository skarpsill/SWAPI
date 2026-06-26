---
title: "swsContactComponentEndEditError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsContactComponentEndEditError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsContactComponentEndEditError_e.html"
---

# swsContactComponentEndEditError_e Enumeration

Contact component editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsContactComponentEndEditError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsContactComponentEndEditError_e
```

### C#

```csharp
public enum swsContactComponentEndEditError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsContactComponentEndEditError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsContactComponentEndEditErrorBodiesNotTouchingBodies | 8 = Specified bodies for bonding or node to node contact condition are not touching other bodies |
| swsContactComponentEndEditErrorCannotSpecifyFreeContact | 7 = Free contact may not be specified for components that interfere with other components |
| swsContactComponentEndEditErrorContactComponentCannotBeCreated | 1 = Contact component cannot be created for this study type |
| swsContactComponentEndEditErrorIncorrectCoefficientOfFriction | 4 = Coefficient of friction must be greater than or equal to 0 and less than or equal to 1.0 |
| swsContactComponentEndEditErrorInvalidContactType | 2 = Invalid contact type |
| swsContactComponentEndEditErrorSelectComponentOrBody | 3 = Select one component or one body |
| swsContactComponentEndEditErrorSelectSolidBodyOrComponent | 5 = Select only one solid body or component |
| swsContactComponentEndEditErrorSuccessful | 0 = Successful |
| swsContactComponentEndEditErrorTooManyBodiesOrComponents | 6 = At least one body or component is specified more than once |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
