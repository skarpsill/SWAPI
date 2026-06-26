---
title: "swFeatureScope_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swFeatureScope_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureScope_e.html"
---

# swFeatureScope_e Enumeration

Feature scope options.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swFeatureScope_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swFeatureScope_e
```

### C#

```csharp
public enum swFeatureScope_e : System.Enum
```

### C++/CLI

```cpp
public enum class swFeatureScope_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swFeatureScope_AllBodies | 0 = All of the bodies in the multibody part are affected by the Mirror feature. |
| swFeatureScope_SelectedBodiesWithAutoSelect | 1 = Only the specified bodies in the multibody part are affected by the Mirror feature when AutoSelect is true. |
| swFeatureScope_SelectedBodiesWithOutAutoSelect | 2 = Only the specified bodies in the multibody part are affected by the Mirror feature when AutoSelect is false. |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
