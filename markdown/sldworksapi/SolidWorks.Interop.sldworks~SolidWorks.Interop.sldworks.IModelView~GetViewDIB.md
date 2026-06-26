---
title: "GetViewDIB Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetViewDIB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewDIB.html"
---

# GetViewDIB Method (IModelView)

Gets an image of the document as it looks in Normal view or in the print preview.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViewDIB() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

value = instance.GetViewDIB()
```

### C#

```csharp
System.int GetViewDIB()
```

### C++/CLI

```cpp
System.int GetViewDIB();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Pointer to DIBSECTION for image

## VBA Syntax

See

[ModelView::GetViewDIB](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetViewDIB.html)

.

## Remarks

If your application must be x64 compatible, then use[IModelView::GetViewDIBx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetViewDIBx64.html).

The image type and resolution can be controlled interactively under TIFF export options.

If TIFF export is set to screen, then the output from this method is based on the current screen resolution. If it's set to print, then the output is based on the DPI specified in the TIFF options dialog.

The memory for the image bits (DIBSECTION.dsBm.bmBits) and this structure are allocated by the SOLIDWORKS application and must be deleted by the caller. For more information, see the description of Bitmap structures and DIBSECTION in Microsoft Help.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)

[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
