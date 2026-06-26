---
title: "Get Assembly Bounding Box Using Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Assembly_Bounding_Box_using_Components_Example_VB.htm"
---

# Get Assembly Bounding Box Using Components Example (VBA)

This example shows how to get a bounding box for an assembly.

```
'--------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Ensure that all components in the assembly are fully resolved.
' 3. Open the Immediate window.
' 4. Run the macro.
'
' Postconditions:
' 1. Adds a 3D sketch to the assembly showing the bounding box.
' 2. Examine the graphics area and Immediate window to verify.
'
' NOTES:
' * Because all assembly component bounding boxes are
'   approximated, the bounding box for the assembly
'   is also approximated.
' * Resulting bounding box is oriented with the assembly
'   coordinate system.
'----------------------------------------------
```

```
Option Explicit
```

```
Function GetMax(ByVal Val1 As Double, ByVal Val2 As Double, ByVal Val3 As Double) As Double
' Finds maximum of 3 values
    GetMax = Val1
    If Val2 > GetMax Then
        GetMax = Val2
    End If
    If Val3 > GetMax Then
        GetMax = Val3
    End If
End Function
```

```
Function GetMin(ByVal Val1 As Double, ByVal Val2 As Double, ByVal Val3 As Double) As Double
```

```
' Finds minimum of 3 values
    GetMin = Val1
    If Val2 < GetMin Then
        GetMin = Val2
    End If
    If Val3 < GetMin Then
        GetMin = Val3
    End If
End Function
```

```
Sub main()
```

```
    Const MaxDouble             As Double = 1.79769313486231E+308
    Const MinDouble             As Double = -1.79769313486231E+308
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swAssy                  As SldWorks.AssemblyDoc
    Dim swConfigurationMgr      As SldWorks.ConfigurationManager
    Dim swConfig                As SldWorks.Configuration
    Dim swRootComp              As SldWorks.Component2
    Dim vChild                  As Variant
    Dim swChildComp             As SldWorks.Component2
    Dim vBox                    As Variant
    Dim X_max                   As Double
    Dim X_min                   As Double
    Dim Y_max                   As Double
    Dim Y_min                   As Double
    Dim Z_max                   As Double
    Dim Z_min                   As Double
    Dim swSketchMgr             As SldWorks.SketchManager
    Dim swSketchPt(8)           As SldWorks.SketchPoint
    Dim swSketchSeg(12)         As SldWorks.SketchSegment
    Dim i                       As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swConfigurationMgr = swModel.ConfigurationManager
    Set swConfig = swConfigurationMgr.ActiveConfiguration
    Set swRootComp = swConfig.GetRootComponent3(True)
```

```
    ' Initialize values
    X_max = MinDouble
    X_min = MaxDouble
    Y_max = MinDouble
    Y_min = MaxDouble
    Z_max = MinDouble
    Z_min = MaxDouble
```

```
    vChild = swRootComp.GetChildren
    For i = 0 To UBound(vChild)
        Set swChildComp = vChild(i)
```

```
        If swChildComp.Visible = swComponentVisible Then
            vBox = swChildComp.GetBox(False, False)
            X_max = GetMax(vBox(0), vBox(3), X_max)
            X_min = GetMin(vBox(0), vBox(3), X_min)
            Y_max = GetMax(vBox(1), vBox(4), Y_max)
            Y_min = GetMin(vBox(1), vBox(4), Y_min)
            Z_max = GetMax(vBox(2), vBox(5), Z_max)
            Z_min = GetMin(vBox(2), vBox(5), Z_min)
        End If
    Next i
```

```
    Debug.Print "Assembly Bounding Box (" + swModel.GetPathName + ") = "
    Debug.Print "  (" + Str(X_min * 1000#) + "," + Str(Y_min * 1000#) + "," + Str(Z_min * 1000#) + ") mm"
    Debug.Print "  (" + Str(X_max * 1000#) + "," + Str(Y_max * 1000#) + "," + Str(Z_max * 1000#) + ") mm"
```

```
    Set swSketchMgr = swModel.SketchManager
```

```
    swSketchMgr.Insert3DSketch True
    swSketchMgr.AddToDB = True
```

```
    ' Draw points at each corner of bounding box
    Set swSketchPt(0) = swSketchMgr.CreatePoint(X_min, Y_min, Z_min)
    Set swSketchPt(1) = swSketchMgr.CreatePoint(X_min, Y_min, Z_max)
    Set swSketchPt(2) = swSketchMgr.CreatePoint(X_min, Y_max, Z_min)
    Set swSketchPt(3) = swSketchMgr.CreatePoint(X_min, Y_max, Z_max)
    Set swSketchPt(4) = swSketchMgr.CreatePoint(X_max, Y_min, Z_min)
    Set swSketchPt(5) = swSketchMgr.CreatePoint(X_max, Y_min, Z_max)
    Set swSketchPt(6) = swSketchMgr.CreatePoint(X_max, Y_max, Z_min)
    Set swSketchPt(7) = swSketchMgr.CreatePoint(X_max, Y_max, Z_max)
```

```
    ' Draw bounding box
    Set swSketchSeg(0) = swSketchMgr.CreateLine(X_min, Y_min, Z_min, X_max, Y_min, Z_min)
    Set swSketchSeg(1) = swSketchMgr.CreateLine(X_max, Y_min, Z_min, X_max, Y_min, Z_max)
    Set swSketchSeg(2) = swSketchMgr.CreateLine(X_max, Y_min, Z_max, X_min, Y_min, Z_max)
    Set swSketchSeg(3) = swSketchMgr.CreateLine(X_min, Y_min, Z_max, X_min, Y_min, Z_min)
    Set swSketchSeg(4) = swSketchMgr.CreateLine(X_min, Y_min, Z_min, X_min, Y_max, Z_min)
    Set swSketchSeg(5) = swSketchMgr.CreateLine(X_min, Y_min, Z_max, X_min, Y_max, Z_max)
    Set swSketchSeg(6) = swSketchMgr.CreateLine(X_max, Y_min, Z_min, X_max, Y_max, Z_min)
    Set swSketchSeg(7) = swSketchMgr.CreateLine(X_max, Y_min, Z_max, X_max, Y_max, Z_max)
    Set swSketchSeg(8) = swSketchMgr.CreateLine(X_min, Y_max, Z_min, X_max, Y_max, Z_min)
    Set swSketchSeg(9) = swSketchMgr.CreateLine(X_max, Y_max, Z_min, X_max, Y_max, Z_max)
    Set swSketchSeg(10) = swSketchMgr.CreateLine(X_max, Y_max, Z_max, X_min, Y_max, Z_max)
    Set swSketchSeg(11) = swSketchMgr.CreateLine(X_min, Y_max, Z_max, X_min, Y_max, Z_min)
```

```
    swSketchMgr.AddToDB = False
    swSketchMgr.Insert3DSketch True
```

```
End Sub
```
