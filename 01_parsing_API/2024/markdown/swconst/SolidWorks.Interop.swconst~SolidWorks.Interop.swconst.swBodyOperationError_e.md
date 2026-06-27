---
title: "swBodyOperationError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swBodyOperationError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBodyOperationError_e.html"
---

# swBodyOperationError_e Enumeration

Body operation errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swBodyOperationError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swBodyOperationError_e
```

### C#

```csharp
public enum swBodyOperationError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swBodyOperationError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBodyOperationBooleanFail | 1058 = Boolean fail error |
| swBodyOperationDisjointBodies | 5 = Disjoint bodies error |
| swBodyOperationEmptyBody | 6 = Empty body error |
| swBodyOperationEmptyInputBody | 7 = Empty input body error |
| swBodyOperationFailGeomCondition | 3 = Failed geometry condition |
| swBodyOperationFailToCutBody | 4 = Failed to cut body error |
| swBodyOperationIntersectSolidWithSheets | 972 = Intersect solid with sheets error |
| swBodyOperationInvalidInputBody | 8 = Invalid input body |
| swBodyOperationMissingGeom | 96 = Missing geometry error |
| swBodyOperationNoError | 0 = No error |
| swBodyOperationNoIntersect | 1067 = No intersect error |
| swBodyOperationNonApiBody | 1 = Non API body error |
| swBodyOperationNonManifold | 547 = Nonmanifold error |
| swBodyOperationOpposedSheets | 951 = Boolean fail error; invalid orientation for operation |
| swBodyOperationPartialCoincidence | 1040 = Partial coincidence error |
| swBodyOperationSameToolAndTarget | 545 = Same tool and target error |
| swBodyOperationUniteSolidSheet | 543 = Unite solid sheet error |
| swBodyOperationUnknownError | -1 = Unknown error |
| swBodyOperationWrongType | 2 = Wrong type error |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
