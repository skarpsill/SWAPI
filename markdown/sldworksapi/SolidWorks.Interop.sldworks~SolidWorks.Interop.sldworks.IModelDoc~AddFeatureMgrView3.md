---
title: "AddFeatureMgrView3 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddFeatureMgrView3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddFeatureMgrView3.html"
---

# AddFeatureMgrView3 Method (IModelDoc)

Obsolete. Superseded by

[IModelDoc2::AddFeatureMgrView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFeatureMgrView3( _
   ByRef Bitmap As System.Integer, _
   ByRef AppView As System.Integer, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Bitmap As System.Integer
Dim AppView As System.Integer
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As System.Boolean

value = instance.AddFeatureMgrView3(Bitmap, AppView, ToolTip, WhichPane)
```

### C#

```csharp
System.bool AddFeatureMgrView3(
   ref System.int Bitmap,
   ref System.int AppView,
   System.string ToolTip,
   System.int WhichPane
)
```

### C++/CLI

```cpp
System.bool AddFeatureMgrView3(
   System.int% Bitmap,
   System.int% AppView,
   System.String^ ToolTip,
   System.int WhichPane
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
- `WhichPane`:

## VBA Syntax

See

[ModelDoc::AddFeatureMgrView3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddFeatureMgrView3.html)

.

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)

[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
