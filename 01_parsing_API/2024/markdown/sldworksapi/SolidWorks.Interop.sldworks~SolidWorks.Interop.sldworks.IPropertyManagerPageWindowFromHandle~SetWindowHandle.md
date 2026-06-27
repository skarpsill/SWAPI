---
title: "SetWindowHandle Method (IPropertyManagerPageWindowFromHandle)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageWindowFromHandle"
member: "SetWindowHandle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle~SetWindowHandle.html"
---

# SetWindowHandle Method (IPropertyManagerPageWindowFromHandle)

Sets the handle of this .NET control.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetWindowHandle( _
   ByVal WindowHandle As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageWindowFromHandle
Dim WindowHandle As System.Integer
Dim value As System.Boolean

value = instance.SetWindowHandle(WindowHandle)
```

### C#

```csharp
System.bool SetWindowHandle(
   System.int WindowHandle
)
```

### C++/CLI

```cpp
System.bool SetWindowHandle(
   System.int WindowHandle
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `WindowHandle`: Handle of the .NET control

### Return Value

True if handle is set, false if not

## VBA Syntax

See

[PropertyManagerPageWindowFromHandle::SetWindowHandle](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageWindowFromHandle~SetWindowHandle.html)

.

## Remarks

If your application must be x64 compatible, then use[IPropertyManagerPageWindowFromHandle::SetWindowHandlex64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageWindowFromHandle~SetWindowHandlex64.html).

You must call this method to initialize the .NET control handle whenever you call[IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html), because .NET control handles are destroyed with their forms when the PropertyManager page closes.

## See Also

[IPropertyManagerPageWindowFromHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle.html)

[IPropertyManagerPageWindowFromHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
