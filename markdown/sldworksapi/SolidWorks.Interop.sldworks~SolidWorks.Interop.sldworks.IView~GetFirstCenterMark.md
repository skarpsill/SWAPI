---
title: "GetFirstCenterMark Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstCenterMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterMark.html"
---

# GetFirstCenterMark Method (IView)

Gets the first center mark in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstCenterMark() As CenterMark
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As CenterMark

value = instance.GetFirstCenterMark()
```

### C#

```csharp
CenterMark GetFirstCenterMark()
```

### C++/CLI

```cpp
CenterMark^ GetFirstCenterMark();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

First

[center mark](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark.html)

## VBA Syntax

See

[View::GetFirstCenterMark](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstCenterMark.html)

.

## Examples

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

[Select All Center Marks (C#)](Select_All_Center_Marks_Example_CSharp.htm)

[Select All Center Marks (VB.NET)](Select_All_Center_Marks_Example_VBNET.htm)

[Select All Center Marks (VBA)](Select_All_Center_Marks_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetCenterMarkCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.html)

[IView::GetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.html)

[IView::GetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.html)

[IView::IGetCenterMarkInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarkInfo.html)

[IView::IGetCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterMarks.html)

[ICenterMark::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetNext.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
