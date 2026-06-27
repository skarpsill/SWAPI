---
title: "GetViewHWnd Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetViewHWnd"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewHWnd.html"
---

# GetViewHWnd Method (IModelView)

Gets the Microsoft window handle for this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViewHWnd() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

value = instance.GetViewHWnd()
```

### C#

```csharp
System.int GetViewHWnd()
```

### C++/CLI

```cpp
System.int GetViewHWnd();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Microsoft window handle

## VBA Syntax

See

[ModelView::GetViewHWnd](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetViewHWnd.html)

.

## Remarks

If your application must be x64 compatible, then use[IModelView::GetViewHWndx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetViewHWndx64.html).

Window handles are not unique across computers.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)

[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

[IModelWindow::HWnd Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWnd.html)
