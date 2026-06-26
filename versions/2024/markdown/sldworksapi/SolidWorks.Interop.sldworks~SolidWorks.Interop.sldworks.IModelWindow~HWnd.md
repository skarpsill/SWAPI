---
title: "HWnd Property (IModelWindow)"
project: "SOLIDWORKS API Help"
interface: "IModelWindow"
member: "HWnd"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow~HWnd.html"
---

# HWnd Property (IModelWindow)

Gets the handle to this model window.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HWnd As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelWindow
Dim value As System.Integer

value = instance.HWnd
```

### C#

```csharp
System.int HWnd {get;}
```

### C++/CLI

```cpp
property System.int HWnd {
   System.int get();
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Handle for this model window

## VBA Syntax

See

[ModelWindow::HWnd](ms-its:sldworksapivb6.chm::/sldworks~ModelWindow~HWnd.html)

.

## Examples

[Switch Documents (C#)](Switch_Documents_Example_CSharp.htm)

[Switch Documents (VB.NET)](Switch_Documents_Example_VBNET.htm)

[Switch Documents (VBA)](Switch_Documents_Example_VB.htm)

## Remarks

If your application must be x64 compatible, then use

[IModelWindow::HWndx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelWindow~HWndx64.html)

.

## See Also

[IModelWindow Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow.html)

[IModelWindow Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
