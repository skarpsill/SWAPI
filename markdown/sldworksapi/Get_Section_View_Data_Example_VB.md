---
title: "Get Section View Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Section_View_Data_Example_VB.htm"
---

# Get Section View Data Example (VBA)

This example shows how to get the data for a section view in a part.

```
'-------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\cosmosxpress\aw_rubber_duct.sldprt.
' 2. Create a section view with three sections:
'    a. Right-click Front in the FeatureManager design tree
'       and click Section View.
'    b. Set X Rotation to 45.00deg in Section 1.
'    c. Select Section 2, click Top, and
'       set X Rotation to 45.00deg.
'    d. Select Section 3, click Right, and
'       set X Rotation to 45.00deg.
'    e. Click Save twice.
' 3. Click View > Display > Section View twice.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Gets and prints data about each section in
'    the section view to the Immediate window.
' 2. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelViewMgr As SldWorks.ModelViewManager
    Dim swSectionViewData As SldWorks.SectionViewData
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim status As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    'Get section view
    Set swModelViewMgr = swModel.ModelViewManager
    Set swSectionViewData = swModelViewMgr.GetSectionViewData("")
```

```
    DisplayDebugInformation swSectionViewData, swSelMgr
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```

```
'Select the planes and print each section's data
Sub DisplayDebugInformation(data As SectionViewData, selMgr As SelectionMgr)
    Dim p1 As SldWorks.Feature
    Dim p2 As SldWorks.Feature
    Dim p3 As SldWorks.Feature
    Dim swMathTransform As SldWorks.MathTransform
    Dim transform As Variant
```

```
    Set p1 = data.FirstPlane
    If Not p1 Is Nothing Then p1.Select2 True, 1
```

```
    Set p2 = data.SecondPlane
    If Not p2 Is Nothing Then p2.Select2 True, 2
```

```
    Set p3 = data.ThirdPlane
    If Not p3 Is Nothing Then p3.Select2 True, 4
```

```
    Debug.Print "----------Section 1----------"
    Debug.Print "Offset: " & data.FirstOffset
    Debug.Print "Rotation X: " & data.FirstRotationX
    Debug.Print "Rotation Y: " & data.FirstRotationY
    Debug.Print "Color: " & data.FirstColor
    Debug.Print "Reverse direction: " & data.FirstReverseDirection
```

```
    Debug.Print "----------Section 2----------"
    Debug.Print "Offset: " & data.SecondOffset
    Debug.Print "Rotation X: " & data.SecondRotationX
    Debug.Print "Rotation Y: " & data.SecondRotationY
    Debug.Print "Color: " & data.SecondColor
    Debug.Print "Reverse direction: " & data.SecondReverseDirection
```

```
    Debug.Print "----------Section 3----------"
    Debug.Print "Offset: " & data.ThirdOffset
    Debug.Print "Rotation X: " & data.ThirdRotationX
    Debug.Print "Rotation Y: " & data.ThirdRotationY
    Debug.Print "Color: " & data.ThirdColor
    Debug.Print "Reverse direction: " & data.ThirdReverseDirection
    Set swMathTransform = data.GetDynamicCenterTransform(3)
    Debug.Print "Dynamic center transform:"
    transform = swMathTransform.ArrayData()
    If Not IsEmpty(transform) Then
        Debug.Print "  Rotate: " & Format(transform(0), "###0.0#####") & " " & Format(transform(1), "###0.0#####") & " " & Format(transform(2), "###0.0#####")
        Debug.Print "          " & Format(transform(3), "###0.0#####") & " " & Format(transform(4), "###0.0#####") & " " & Format(transform(5), "###0.0#####")
        Debug.Print "          " & Format(transform(6), "###0.0#####") & " " & Format(transform(7), "###0.0#####") & " " & Format(transform(8), "###0.0#####")
        Debug.Print "  Translate: " & Format(transform(9), "###0.0#####") & " " & Format(transform(10), "###0.0#####") & " " & Format(transform(11), "###0.0#####")
    End If
```

```
    Debug.Print "----------Section Cap---------"
    Debug.Print "Show section cap: " & data.ShowSectionCap
```

```
 End Sub
```
