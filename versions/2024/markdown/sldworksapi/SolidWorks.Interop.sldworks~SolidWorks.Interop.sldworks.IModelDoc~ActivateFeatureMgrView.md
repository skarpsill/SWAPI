---
title: "ActivateFeatureMgrView Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ActivateFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ActivateFeatureMgrView.html"
---

# ActivateFeatureMgrView Method (IModelDoc)

Obsolete. Superseded by

[IModelDoc2::ActivateFeatureMgrView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ActivateFeatureMgrView.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivateFeatureMgrView( _
   ByRef AppView As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim AppView As System.Integer
Dim value As System.Integer

value = instance.ActivateFeatureMgrView(AppView)
```

### C#

```csharp
System.int ActivateFeatureMgrView(
   ref System.int AppView
)
```

### C++/CLI

```cpp
System.int ActivateFeatureMgrView(
   System.int% AppView
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `AppView`:

## VBA Syntax

See

[ModelDoc::ActivateFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ActivateFeatureMgrView.html)

.

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)

[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
