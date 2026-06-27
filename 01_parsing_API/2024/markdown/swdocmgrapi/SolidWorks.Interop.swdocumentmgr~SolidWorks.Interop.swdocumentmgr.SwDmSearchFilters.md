---
title: "SwDmSearchFilters Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmSearchFilters"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmSearchFilters.html"
---

# SwDmSearchFilters Enumeration

Search filters. Bitmask.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmSearchFilters
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmSearchFilters
```

### C#

```csharp
public enum SwDmSearchFilters : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmSearchFilters : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| SwDmSearchExternalReference | 16 = Search for simple assembly references to parts and subassemblies |
| SwDmSearchForAssembly | 8 = Search for assemblies |
| SwDmSearchForDrawing | 4 = Search for drawings |
| SwDmSearchForPart | 2 = Search for parts |
| SwDmSearchInContextReference | 32 = Search for references to base parts for derived parts, mirrored parts, derived component parts, and parts designed in the context of assemblies |
| SwDmSearchPartToBaseAssemblyReference | 128 = Search for references to assemblies that have been inserted into parts using the Insert Assembly feature |
| SwDmSearchRootAssemblyFolder | 64 = Search all the way to the assembly's root folder |
| SwDmSearchSubfolders | 1 = Recursively search all of the subfolders. This is only applicable when used with ISwDMDocument::WhereUsed and ISwDMComponent4::GetDocument2 |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
