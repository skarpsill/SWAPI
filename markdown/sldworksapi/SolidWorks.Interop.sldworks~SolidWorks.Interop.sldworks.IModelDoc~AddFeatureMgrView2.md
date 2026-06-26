---
title: "AddFeatureMgrView2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddFeatureMgrView2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddFeatureMgrView2.html"
---

# AddFeatureMgrView2 Method (IModelDoc)

Obsolete. Superseded by

[IModelDoc2::AddFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddFeatureMgrView2.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFeatureMgrView2( _
   ByRef Bitmap As System.Integer, _
   ByRef AppView As System.Integer, _
   ByVal ToolTip As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim AppView As System.Integer
Dim ToolTip As System.String
Dim value As System.Boolean

value = instance.AddFeatureMgrView2(Bitmap, AppView, ToolTip)
```

### C#

```csharp
System.bool AddFeatureMgrView2(
   ref System.int Bitmap,
   ref System.int AppView,
   System.string ToolTip
)
```

### C++/CLI

```cpp
System.bool AddFeatureMgrView2(
   System.int% Bitmap,
   System.int% AppView,
   System.String^ ToolTip
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Bitmap`:
- `AppView`:
- `ToolTip`:

## VBA Syntax

See

[ModelDoc::AddFeatureMgrView2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddFeatureMgrView2.html)

.

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)

[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
