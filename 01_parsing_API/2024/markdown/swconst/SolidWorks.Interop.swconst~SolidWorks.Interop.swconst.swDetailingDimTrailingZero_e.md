---
title: "swDetailingDimTrailingZero_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swDetailingDimTrailingZero_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDetailingDimTrailingZero_e.html"
---

# swDetailingDimTrailingZero_e Enumeration

Detailing dimension trailing zero styles.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDetailingDimTrailingZero_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDetailingDimTrailingZero_e
```

### C#

```csharp
public enum swDetailingDimTrailingZero_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDetailingDimTrailingZero_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDimRemoveOnlyOnZero | 4 = Remove only on zero |
| swDimRemoveTrailingZeroes | 2 = Trailing zeroes do not appear |
| swDimSameAsDimension | 8 = Use the dimension's trailing zeroes setting |
| swDimSameAsDocumentDimension | 6 = Use the document dimension's trailing zeroes setting |
| swDimSameAsDocumentTolerance | 7 = Use the document tolerance's trailing zeroes setting |
| swDimSameAsSource | 5 = Use the source's trailing zeroes setting |
| swDimShowTrailingZeroes | 1 = Trailing zeroes appear |
| swDimSmartTrailingZeroes | 0 = OBSOLETE; do not use to set document properties |
| swDimStandardTrailingZeroes | 3 = OBSOLETE; do not use to set document properties |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
