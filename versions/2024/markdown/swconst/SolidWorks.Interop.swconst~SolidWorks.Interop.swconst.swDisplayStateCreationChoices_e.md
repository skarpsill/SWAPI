---
title: "swDisplayStateCreationChoices_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDisplayStateCreationChoices_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayStateCreationChoices_e.html"
---

# swDisplayStateCreationChoices_e Enumeration

Display-state preserve options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDisplayStateCreationChoices_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDisplayStateCreationChoices_e
```

### C#

```csharp
public enum swDisplayStateCreationChoices_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDisplayStateCreationChoices_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDisplayStateCreation_AskUser | -1; Display the dialog where the user can select the display states (PhotoWorks material and SOLIDWORKS colors) he or she wants to preserve; however, if swDisplayStateCreation_AskUser is set and the user opens the file using ISldWorks::OpenDoc n (where n is the version number of the method), then both display states are preserved and the dialog is not displayed; valid in documents created in SOLIDWORKS 2009 and earlier |
| swDisplayStateCreation_BothPWSW | 3; Preserve both PhotoWorks and SOLIDWORKS display states; valid in documents created in SOLIDWORKS 2009 and earlier |
| swDisplayStateCreation_PW | 1; Preserve PhotoWorks material display state only; valid in documents created in SOLIDWORKS 2009 and earlier |
| swDisplayStateCreation_SW | 2; Preserve SOLIDWORKS color display state only; valid in documents created in SOLIDWORKS 2009 and earlier |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
