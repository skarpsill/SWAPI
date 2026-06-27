---
title: "Set Visible Bounding Box for Zoom to Fit Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_VB.htm"
---

# Set Visible Bounding Box for Zoom to Fit Example (VBA)

This example shows how to set the visible bounding box for Zoom to Fit.

```
'--------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document and zooms to fit
'    the assembly in the graphics area.
' 2. When Done! is printed to the Immediate window,
'    click Zoom to Fit > arm2 at the top of the
'    FeatureManager design tree.
' 3. Examine the graphics area and observe the new bounding box.
'
' NOTE: Because the assembly is used elsewhere, do not save
' changes.
'--------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swAssembly As SldWorks.AssemblyDoc
Dim swMathPoint1 As SldWorks.MathPoint
Dim swMathPoint2 As SldWorks.MathPoint
Dim swMathUtilty As SldWorks.MathUtility
Dim options As Long
Dim arr1() As Double
Dim arr2() As Double
Dim box() As Double
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\arm2.sldasm", 2, 0, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("arm2.SLDASM", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ViewZoomtofit2
    Set swAssembly = swModel
```

```
    swModel.ClearSelection2 True
```

```
    options = swBoundingBoxIncludeRefPlanes + swBoundingBoxIncludeSketches
    box = swAssembly.GetBox(options)
```

```
    'Change values
    box(0) = box(0) + box(0)
    box(1) = box(1) + box(1)
    box(2) = box(2) + box(2)
    box(3) = box(3) + box(3)
    box(4) = box(4) + box(4)
    box(5) = box(5) + box(5)
```

```
    'Apply the new values
    Dim ar1(2) As Double
    Dim ar2(2) As Double
```

```
    ar1(0) = box(0)
    ar1(1) = box(1)
    ar1(2) = box(2)
    ar2(0) = box(3)
    ar2(1) = box(4)
    ar2(2) = box(5)
```

```
    Set swMathUtilty = swApp.GetMathUtility
    Set swMathPoint1 = swMathUtilty.CreatePoint(ar1)
    Set swMathPoint2 = swMathUtilty.CreatePoint(ar2)
```

```
    'Set the bounding box
    swModelDocExt.SetVisibleBox swMathPoint1, swMathPoint2
```

```
    'Remove the bounding box
    'swModelDocExt.RemoveVisibleBox
```

```
    Debug.Print "Done!"
```

```
End Sub
```
