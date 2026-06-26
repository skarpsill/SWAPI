---
title: "swConfigTreeSortType_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swConfigTreeSortType_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConfigTreeSortType_e.html"
---

# swConfigTreeSortType_e Enumeration

Order in which configurations are listed in the ConfigurationManager.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swConfigTreeSortType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swConfigTreeSortType_e
```

### C#

```csharp
public enum swConfigTreeSortType_e : System.Enum
```

### C++/CLI

```cpp
public enum class swConfigTreeSortType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSortType_DesignTable | 3 = Order of the configurations in the ConfigurationManager is dictated by the order of the configurations in the design table |
| swSortType_History | 0 = Order of the configurations in the ConfigurationManager is dictated by the date the configuration was created, from earliest created at the top of the list to most recently created at the bottom of the list |
| swSortType_Literal | 2 = Order of the configurations in the ConfigurationManager is alphabetical |
| swSortType_Numeric | 1 = Order of the configurations in the ConfigurationManager is by ascending alpha or numeric value |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
