---
title: "swPropertyManagerPageStatus_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPropertyManagerPageStatus_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertyManagerPageStatus_e.html"
---

# swPropertyManagerPageStatus_e Enumeration

PropertyManager page statuses.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPropertyManagerPageStatus_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPropertyManagerPageStatus_e
```

### C#

```csharp
public enum swPropertyManagerPageStatus_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPropertyManagerPageStatus_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPropertyManagerPage_CreationFailure | -1 |
| swPropertyManagerPage_NoDocument | -2 = A PropertyManager page can only be shown in a SOLIDWORKS document window; you can create and set up the page without a document being active, but there must be a document active when you try to show the page; if there is no active document window, then swPropertyManagerPage_NoDocument is returned |
| swPropertyManagerPage_Okay | 0 |
| swPropertyManagerPage_UnsupportedHandler | 1 = The PropertyManager page is created and shown; however, a problem exists; for example, you must specify the handler when you create the PropertyManager page; your add-in must implement IPropertyManagerPage2Handler4 so that SOLIDWORKS can call back certain methods when operations, such as clicking a button, occur on the PropertyManager page;if the interface that is passed in does not support PropertyManagerPage2Handler4, then swPropertyManagerPage_UnsupportedHandler is returned |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
