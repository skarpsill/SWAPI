---
title: "DisplayWindowFromHandle Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "DisplayWindowFromHandle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DisplayWindowFromHandle.html"
---

# DisplayWindowFromHandle Method (ITaskpaneView)

Adds a .NET control to the Task Pane view.

## Syntax

### Visual Basic (Declaration)

```vb
Function DisplayWindowFromHandle( _
   ByVal WindowHandle As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim WindowHandle As System.Integer
Dim value As System.Boolean

value = instance.DisplayWindowFromHandle(WindowHandle)
```

### C#

```csharp
System.bool DisplayWindowFromHandle(
   System.int WindowHandle
)
```

### C++/CLI

```cpp
System.bool DisplayWindowFromHandle(
   System.int WindowHandle
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `WindowHandle`: Handle of .NET control

### Return Value

True if .NET control is added, false if not

## VBA Syntax

See

[TaskpaneView::DisplayWindowFromHandle](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~DisplayWindowFromHandle.html)

.

## Remarks

If your application must be x64 compatible, then use

[ITaskPaneView::DisplayWindowFromHandlex64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITaskpaneView~DisplayWindowFromHandlex64.html)

.

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)

[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)

[ITaskpaneView::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddControl.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
