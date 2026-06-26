---
title: "swBOMConfigurationCreationErrors_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swBOMConfigurationCreationErrors_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBOMConfigurationCreationErrors_e.html"
---

# swBOMConfigurationCreationErrors_e Enumeration

BOM table configuration creation errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swBOMConfigurationCreationErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swBOMConfigurationCreationErrors_e
```

### C#

```csharp
public enum swBOMConfigurationCreationErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swBOMConfigurationCreationErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBOMTableCreation_AlreadyExists | -3 = BOM table already exists for this drawing view |
| swBOMTableCreation_ExcelDisabled | -4 = BOM table cannot be created because Microsoft Excel is disabled on this system |
| swBOMTableCreation_Failed | -5 = BOM table creation failed because the specified template is not valid |
| swBOMTableCreation_MustBeDrawingView | -2 = BOM tables can only be added to a drawing view |
| swBOMTableCreation_NoModelForView | -6 = No model available for drawing view |
| swBOMTableCreation_Okay | 0 = Table was successfully created |
| swBOMTableCreation_UnspecifiedError | -1 = Table could not be created for unknown reasons |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
