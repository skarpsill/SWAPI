---
title: "swClearanceVerificationSetEntityErrors_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swClearanceVerificationSetEntityErrors_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swClearanceVerificationSetEntityErrors_e.html"
---

# swClearanceVerificationSetEntityErrors_e Enumeration

Error codes when setting entities for clearance verification.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swClearanceVerificationSetEntityErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swClearanceVerificationSetEntityErrors_e
```

### C#

```csharp
public enum swClearanceVerificationSetEntityErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swClearanceVerificationSetEntityErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swClearanceVerification_swComponentAlreadySelected | 2 = Same component added twice or component added whose face is in face array |
| swClearanceVerification_swFacesAlreadySelected | 1 = Same face added twice |
| swClearanceVerification_swInsufficientEntities | 5 = Face and component arrays are empty |
| swClearanceVerification_swInvalidComponent | 3 = Not a valid SOLIDWORKS component |
| swClearanceVerification_swInvalidFace | 4 = Not a valid SOLIDWORKS face |
| swClearanceVerification_swSuccess | 0 |
| swClearanceVerification_Unknown | -1 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
