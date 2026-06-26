---
title: "Insert Sheet Metal Base Flange Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sheet_Metal_Base_Flange_Example_VB.htm"
---

# Insert Sheet Metal Base Flange Example (VBA)

This example shows how to insert a sheet metal base flange.

```
'---------------------------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Creates two boss extrudes and converts them to sheet metal parts.
' 2. Inserts a sheet metal base flange that connects the two sheet metal parts.
' 3. Examine the graphics area and FeatureManager design tree.
'---------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As ModelDoc2
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    boolstatus = swApp.ResetUntitledCount(0, 0, 0)
    Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    swApp.ActivateDoc2 "Part1", False, longstatus
    Set Part = swApp.ActiveDoc
```

```
    Part.SketchManager.InsertSketch True
    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.07320616684915, 0.04378582530511, 0.008882453015985, False, 0, Nothing, 0)
    Part.ClearSelection2 True
    Dim vSkLines As Variant
    vSkLines = Part.SketchManager.CreateCornerRectangle(-0.09520523544121, 0.05740695090967, 0, -0.03844330645187, -0.0429584598942, 0)
    Part.ShowNamedView2 "*Trimetric", 8
    Part.ClearSelection2 True
    Dim myFeature As Object
    Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, True, 0, 0, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, True, True, True, 0, 0, False)
    boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0785775433435, 0.01894373057962, 0, True, 0, Nothing, 0)
    boolstatus = Part.FeatureManager.InsertConvertToSheetMetal(0.002, False, False, 0.004, 0.002, 0, 0.5)
    Part.ClearSelection2 True
```

```
    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Part.SketchManager.InsertSketch True
    Part.ClearSelection2 True
    vSkLines = Part.SketchManager.CreateCornerRectangle(-0.02256810687936, 0.06039039042219, 0, 0.02390260459754, -0.04039198125838, 0)
    Part.ClearSelection2 True
    Set myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, True, 0, 0, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, True, True, True, 0, 0, False)
    boolstatus = Part.Extension.SelectByID2("", "FACE", 9.118315510932E-04, 0.02609254832731, 0, True, 0, Nothing, 0)
        boolstatus = Part.FeatureManager.InsertConvertToSheetMetal(0.002, False, False, 0.004, 0.002, 0, 0.5)
    Part.ClearSelection2 True
```

```
    Part.SketchManager.InsertSketch True
    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Part.ClearSelection2 True
    vSkLines = Part.SketchManager.CreateCornerRectangle(-0.05411927414525, 0.01318437124604, 0, -0.007403979976402, -0.001979918613586, 0)
    Dim customBendAllowanceData As Object
    Set myFeature = Part.FeatureManager.InsertSheetMetalBaseFlange2(0.002, False, 0.004, 0.02, 0.01, False, 0, 0, 1, customBendAllowanceData, False, 2, 0.0001, 0.0001, 0.5, True, False, True, True)
    Part.ClearSelection2 True
```

```
End Sub
```
