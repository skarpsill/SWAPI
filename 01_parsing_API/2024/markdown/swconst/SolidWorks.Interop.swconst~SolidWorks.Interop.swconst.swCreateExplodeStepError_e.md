---
title: "swCreateExplodeStepError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCreateExplodeStepError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateExplodeStepError_e.html"
---

# swCreateExplodeStepError_e Enumeration

Return codes when creating an explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCreateExplodeStepError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCreateExplodeStepError_e
```

### C#

```csharp
public enum swCreateExplodeStepError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCreateExplodeStepError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCreateExplodeStepError_EditingComponentInContext | 6 = A component being edited in context is blocking explode step creation. |
| swCreateExplodeStepError_Generic | 1 = Explode step creation failed. |
| swCreateExplodeStepError_InvalidRadialAxis | 4 = A radial explode step is not allowed using the selected components. |
| swCreateExplodeStepError_NoComponents | 3 = Components to move must be selected. |
| swCreateExplodeStepError_NoExplodeView | 2 = An explode view must be active in the current configuration to create an explode step. |
| swCreateExplodeStepError_OpenExplodePMP | 5 = The open Explode PropertyManager is blocking step creation. |
| swCreateExplodeStepError_Successful | 0 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
