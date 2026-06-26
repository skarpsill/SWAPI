---
title: "GetHWnd Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "GetHWnd"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetHWnd.html"
---

# GetHWnd Method (IFrame)

Gets the window handle for the main frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHWnd() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim value As System.Integer

value = instance.GetHWnd()
```

### C#

```csharp
System.int GetHWnd()
```

### C++/CLI

```cpp
System.int GetHWnd();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Window handle

## VBA Syntax

See

[Frame::GetHWnd](ms-its:sldworksapivb6.chm::/sldworks~Frame~GetHWnd.html)

.

## Remarks

If your application must be x64 compatible, then

[use IFrame::GetHWndx64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~GetHWndx64.html)

.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)

[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)

[IFrame::ShowModelWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ShowModelWindow.html)

[IFrame::ModelWindows Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~ModelWindows.html)

[IFrame::GetModelWindowCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetModelWindowCount.html)

[IFrame::IGetModelWindows Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetModelWindows.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
