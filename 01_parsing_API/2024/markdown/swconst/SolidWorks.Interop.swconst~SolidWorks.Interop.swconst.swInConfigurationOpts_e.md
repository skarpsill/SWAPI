---
title: "swInConfigurationOpts_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swInConfigurationOpts_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html"
---

# swInConfigurationOpts_e Enumeration

Configuration options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swInConfigurationOpts_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swInConfigurationOpts_e
```

### C#

```csharp
public enum swInConfigurationOpts_e : System.Enum
```

### C++/CLI

```cpp
public enum class swInConfigurationOpts_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAllConfiguration | 2 |
| swConfigPropertySuppressFeatures | 0 |
| swLinkedToParent | 4 = Valid only for derived configurations; if specified for non-derived configurations, then the active configuration is used |
| swSpecifyConfiguration | 3 |
| swSpeedpakConfiguration | 5 |
| swThisConfiguration | 1 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
