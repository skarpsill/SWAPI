---
title: "GetMenu Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "GetMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenu.html"
---

# GetMenu Method (IFrame)

Gets the menu handle for the main frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMenu() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim value As System.Integer

value = instance.GetMenu()
```

### C#

```csharp
System.int GetMenu()
```

### C++/CLI

```cpp
System.int GetMenu();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Menu handle for the main frame

## VBA Syntax

See

[Frame::GetMenu](ms-its:sldworksapivb6.chm::/sldworks~Frame~GetMenu.html)

.

## Remarks

If your application must be x64 compatible, then use

[IFrame::GetMenux64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~GetMenux64.html)

.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)

[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)

[IFrame::GetHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
