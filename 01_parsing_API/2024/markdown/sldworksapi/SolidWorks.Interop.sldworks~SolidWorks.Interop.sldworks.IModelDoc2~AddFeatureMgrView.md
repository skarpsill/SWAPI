---
title: "AddFeatureMgrView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddFeatureMgrView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView.html"
---

# AddFeatureMgrView Method (IModelDoc2)

Obsolete. Superseded by

[IModelDoc2::AddFeatureMgrView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html)

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
Dim instance As IModelDoc2
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

[ModelDoc2::AddFeatureMgrView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddFeatureMgrView.html)

.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)

[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
