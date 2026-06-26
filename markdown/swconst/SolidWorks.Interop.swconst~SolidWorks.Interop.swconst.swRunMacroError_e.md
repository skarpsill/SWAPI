---
title: "swRunMacroError_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swRunMacroError_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRunMacroError_e.html"
---

# swRunMacroError_e Enumeration

VBA macro error codes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swRunMacroError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swRunMacroError_e
```

### C#

```csharp
public enum swRunMacroError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swRunMacroError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swRunMacroError_BadParmCount | 9 |
| swRunMacroError_BadVarType | 10 |
| swRunMacroError_Busy | 17 |
| swRunMacroError_CallFailed | 20 |
| swRunMacroError_CallRejected | 19 |
| swRunMacroError_CantSave | 27 |
| swRunMacroError_ConnectionTerminated | 18 |
| swRunMacroError_DiskError | 26 |
| swRunMacroError_Exception | 12 |
| swRunMacroError_InvalidArg | 1 |
| swRunMacroError_Invalidindex | 22 |
| swRunMacroError_InvalidProcname | 6 |
| swRunMacroError_InvalidPropertyType | 7 |
| swRunMacroError_MacrosAreDisabled | 2 |
| swRunMacroError_NoPermission | 23 |
| swRunMacroError_NotInDesignMode | 3 |
| swRunMacroError_OnlyCodeModules | 4 |
| swRunMacroError_OpenFileFailed | 28 |
| swRunMacroError_OutOfMemory | 5 |
| swRunMacroError_Overflow | 13 |
| swRunMacroError_ParmNotOptional | 15 |
| swRunMacroError_Reverted | 24 |
| swRunMacroError_SuborfuncExpected | 8 |
| swRunMacroError_TooManyOpenFiles | 25 |
| swRunMacroError_TypeMismatch | 14 |
| swRunMacroError_UnknownLcid | 16 |
| swRunMacroError_UserInterrupt | 11 |
| swRunMacroError_Zombied | 21 |

## Remarks

VSTA error codes not yet implementd.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
