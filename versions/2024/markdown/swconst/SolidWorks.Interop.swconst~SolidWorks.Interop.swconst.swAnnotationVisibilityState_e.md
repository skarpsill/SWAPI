---
title: "swAnnotationVisibilityState_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swAnnotationVisibilityState_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAnnotationVisibilityState_e.html"
---

# swAnnotationVisibilityState_e Enumeration

Annotation visibility states.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swAnnotationVisibilityState_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swAnnotationVisibilityState_e
```

### C#

```csharp
public enum swAnnotationVisibilityState_e : System.Enum
```

### C++/CLI

```cpp
public enum class swAnnotationVisibilityState_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAnnotationHalfHidden | 2 = Annotation is half-hidden (grayed out) or hidden depending on the interactive user's actions. For example, if the annotation's visibility is set to swAnnotationHalfHidden by IAnnotation::Visible , then that annotation is in a half-hidden state, which is not a permanent state. During a Hide/Show Annotations operation in a drawing, a half-hidden annotation is displayed in gray if the interactive user selects to show all annotations. Any annotation set to swAnnotationHalfHidden is hidden when the interactive user finishes using Hide/Show Annotations. |
| swAnnotationHidden | 3 = Annotation is hidden |
| swAnnotationVisibilityUnknown | 0 = Annotation visibility is not known |
| swAnnotationVisible | 1 = Annotation is visible |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
