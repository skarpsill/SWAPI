---
title: "Create Wrap Feature on Multiple Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Wrap_Feature_on_Multiple_Faces_Example_VB.htm"
---

# Create Wrap Feature on Multiple Faces Example (VBA)

This example shows how to create a wrap feature on multiple faces.

```
'---------------------------------------------------------------------------
' Preconditions: Verify that the part to open exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects the plane on which to sketch a circle.
' 3. Sketches the circle.
' 4. Selects the sketch of the circle and the faces on which to
'    wrap it.
' 5. Creates the wrap feature.
' 6. Examine the FeatureManager design tree and part.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\molds\telephone.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Select the plane on which to sketch the circle for the wrap feature
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Plane8", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
```

```
    'Sketch the circle
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
    Set swSketchSegment = swSketchManager.CreateCircle(-0.035, 0.011624, 0#, -0.031081, 0.018171, 0#)
    swModel.ClearSelection2 True
    swSketchManager.InsertSketch True
```

```
    'Select the sketch of the circle and the faces on which to wrap it
    'Because the type of wrap feature to create is Scribe, no pull direction entity is selected
    status = swModelDocExt.SelectByID2("Sketch30", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
    status = swModelDocExt.SelectByRay(-0.103709743982563, 4.66186411857746E-03, 4.65727951450701E-02, 1, 0, 0, 4.21383417784414E-04, 2, True, 1, 0)
    status = swModelDocExt.SelectByRay(-0.105251033879711, 1.3155840361718E-03, 3.60382097004597E-02, 1, 0, 0, 4.21383417784414E-04, 2, True, 1, 0)
    status = swModelDocExt.SelectByRay(-0.104507668954227, 2.55494702965538E-03, 2.57514968545461E-02, 1, 0, 0, 4.21383417784414E-04, 2, True, 1, 0)
    status = swModelDocExt.SelectByRay(-0.101403318635789, 1.81709207475484E-02, 2.55036242558494E-02, 1, 0, 0, 4.21383417784414E-04, 2, True, 1, 0)
    status = swModelDocExt.SelectByRay(-0.100395783628869, 2.05257104351672E-02, 3.56664008024147E-02, 1, 0, 0, 4.21383417784414E-04, 2, True, 1, 0)
    status = swModelDocExt.SelectByRay(-9.97494761213602E-02, 1.90384748429869E-02, 4.84318396352955E-02, 1, 0, 0, 4.21383417784414E-04, 2, True, 1, 0)
```

```
    'Create the wrap feature
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.InsertWrapFeature2(swWrapSketchType_e.swWrapSketchType_Scribe, 0.00254, False, swWrapMethods_e.swWrapMethods_SplineSurface, 5)
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
