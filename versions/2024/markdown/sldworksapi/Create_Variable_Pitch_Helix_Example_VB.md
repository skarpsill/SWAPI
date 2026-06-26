---
title: "Create Variable-pitch Helix Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Variable_Pitch_Helix_Example_VB.htm"
---

# Create Variable-pitch Helix Example (VBA)

This example shows how to create a variable-pitch helix.

```
'--------------------------------------------------------------
' Preconditions: Verify that the specified part document
' template exists.
'
' Postconditions:
' 1. Creates a variable-pitch helix.
' 2. Examine the graphics area and FeatureManager design tree.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim errors As Long
Dim status As Boolean
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
```

```
' Create part document
Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
Set swModel = swApp.ActiveDoc
Set swSketchManager = swModel.SketchManager
Set swFeatureManager = swModel.FeatureManager
```

```
' Sketch a circle
Set swSketchSegment = swSketchManager.CreateCircle(0#, 0#, 0#, 0.045549, 0.013926, 0#)
```

```
' Create a variable-pitch helix using the sketched circle
status = swFeatureManager.InsertVariablePitchHelix(False, True, 1, 4.712388980385)
status = swFeatureManager.AddVariablePitchHelixFirstPitchAndDiameter(0.053, 0.05382625271268)
status = swFeatureManager.AddVariablePitchHelixSegment(0.0265, 0.05382625271268, 0.5)
status = swFeatureManager.AddVariablePitchHelixSegment(0.03975, 0.05382625271268, 0.75)
status = swFeatureManager.AddVariablePitchHelixSegment(0.046375, 0.05382625271268, 0.875)
status = swFeatureManager.AddVariablePitchHelixSegment(0.053, 0.05382625271268, 1)
Set swFeature = swFeatureManager.EndVariablePitchHelix()
```

```
End Sub
```
