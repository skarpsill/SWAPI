---
title: "Cut Body and Keep All Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Cut_Body_and_Keep_All_Bodies_Example_VB.htm"
---

# Cut Body and Keep All Bodies Example (VBA)

This example shows how to cut a body and keep all bodies.

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Copy and paste this code in the main module.
'  2. Click Insert > Class module and copy and paste this code in the class module.
'  3. Verify that the specified part document template exists.
'  4. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a body.
' 3. Splits the body into two bodies.
' 4. Examine the graphics area and Immediate window.
'-----------------------------------------------------------------------------
```

#### 'Main module

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As Boolean
Dim Feature As SldWorks.Feature
Dim PartEvents As Class1
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open new part document
    Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\part.prtdot", 0, 0, 0)
```

```
    'Set up event
    Set PartEvents = New Class1
    Set PartEvents.swPartDoc = swApp.ActiveDoc
```

```
    'Create body
    Call CreateBodiesAndSketch
```

```
    boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    Set Feature = Part.FeatureManager.FeatureCut3(True, False, False, swEndCondThroughAll, swEndCondBlind, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, False, True, True, False, False, False, swStartSketchPlane, 0, False)
    If (Feature Is Nothing) Then
        Debug.Print "No feature created."
    End If
```

```
End Sub
```

```
Sub CreateBodiesAndSketch()
```

```
    'Create body
    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.06869486923422, 0.06291203863612, -0.006492164309718, False, 0, Nothing, 0)
    Part.ClearSelection2 True
    Part.SketchRectangle -0.0424567617866, 0.0388405707196, 0, 0.05638579404467, -0.03750124069479, 0, 1
    Part.ShowNamedView2 "*Trimetric", 8
    Part.ClearSelection2 True
    boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    Part.FeatureManager.FeatureExtrusion3 True, False, False, 0, 0, 0.12, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, False, False, False, 0, 0, False
    Part.ClearSelection2 True
```

```
    'Create sketch for cut feature
    boolstatus = Part.Extension.SelectByID2("", "FACE", -0.02909828822015, 0.03884057071963, 0.09843602253397, False, 0, Nothing, 0)
    Part.SketchManager.InsertSketch True
    Part.ClearSelection2 True
    Dim vSkLines As Variant
    vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0628943705795, -0.07743122635196, 0, 0.1160562766823, -0.04532565168643, 0)
    Part.ClearSelection2 True
    boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

End Sub
```

```
Back to top
```

#### 'Class module

```
Option Explicit
```

```
Public WithEvents swPartDoc   As SldWorks.PartDoc
```

```
Public Function swPartDoc_PromptBodiesToKeepNotify(ByVal swFeat As Object, ByRef bodies As Variant) As Long
    Debug.Print "PartDoc_PromptBodiesToKeepNotify fired."
    Dim theFeature As SldWorks.Feature
    If Not swFeat Is Nothing Then
        Set theFeature = swFeat
        Dim bodiesToKeep(0) As Object
        'Change BodyOption to Body1 or Body2 to show other options
        Dim BodyOption As String
        BodyOption = "AllBodies"
        Select Case BodyOption
            Case "AllBodies"
                theFeature.SetBodiesToKeep True, bodiesToKeep, swThisConfiguration, Nothing
            Case "Body1"
                Set bodiesToKeep(0) = bodies(0)
                theFeature.SetBodiesToKeep False, bodiesToKeep, swThisConfiguration, Nothing
            Case "Body2"
                Set bodiesToKeep(0) = bodies(1)
                theFeature.SetBodiesToKeep False, bodiesToKeep, swThisConfiguration, Nothing
        End Select
    End If
```

```
    swPartDoc_PromptBodiesToKeepNotify = 1
```

```
End Function
```

```
Back to top
```
