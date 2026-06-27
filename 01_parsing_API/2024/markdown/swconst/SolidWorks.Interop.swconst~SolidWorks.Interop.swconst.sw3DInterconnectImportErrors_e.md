---
title: "sw3DInterconnectImportErrors_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "sw3DInterconnectImportErrors_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DInterconnectImportErrors_e.html"
---

# sw3DInterconnectImportErrors_e Enumeration

3D Interconnect import errors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum sw3DInterconnectImportErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As sw3DInterconnectImportErrors_e
```

### C#

```csharp
public enum sw3DInterconnectImportErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class sw3DInterconnectImportErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| sw3DInterconnectImportErrors_AssemblyNotSaved | 3 |
| sw3DInterconnectImportErrors_BreakLinkUnavailable | 4 = Break link is not available for the selected 3D Interconnect feature; break link is only available for top-level assemblies |
| sw3DInterconnectImportErrors_Disabled | 1 = 3D Interconnect is not enabled; to enable set Tools > Options > System Options > Import > Enable 3D Interconnect or call calling ISldWorks::SetUserPreferenceToggle ( swUserPreferenceToggle_e .swMultiCAD_Enable3DInterconnect, True) |
| sw3DInterconnectImportErrors_IncompatibleType | 2 = Specified file type is not correct |
| sw3DInterconnectImportErrors_None | 0 |
| sw3DInterconnectImportErrors_ParametersUnavailable | 5 = Only top-level 3D Interconnect features can be edited |
| sw3DInterconnectImportErrors_TransferOptionNeeded | 6 = One or more import options need to be specified for this import |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
