---
title: "AddFeatureMgrView Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddFeatureMgrView.html"
---

# AddFeatureMgrView Method (IModelDoc)

Obsolete. Superseded by

[IModelDoc2::AddFeatureMgrView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddFeatureMgrView.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFeatureMgrView( _
   ByRef Bitmap As System.Integer, _
   ByRef AppView As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim AppView As System.Integer
Dim value As System.Boolean

value = instance.AddFeatureMgrView(Bitmap, AppView)
```

### C#

```csharp
System.bool AddFeatureMgrView(
   ref System.int Bitmap,
   ref System.int AppView
)
```

### C++/CLI

```cpp
System.bool AddFeatureMgrView(
   System.int% Bitmap,
   System.int% AppView
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Bitmap`:
- `AppView`:

## VBA Syntax

See

[ModelDoc::AddFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddFeatureMgrView.html)

.

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)

[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
