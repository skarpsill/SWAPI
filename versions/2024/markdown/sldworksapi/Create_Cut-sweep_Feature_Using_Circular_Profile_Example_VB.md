---
title: "Create Cut-sweep Feature Using Circular Profile Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cut-sweep_Feature_Using_Circular_Profile_Example_VB.htm"
---

# Create Cut-sweep Feature Using Circular Profile Example (VBA)

This example shows how to create a cut-sweep feature using a circular profile.

```
'-----------------------------------------------
' Preconditions:
' 1. Verify that the part exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects an edge on the part.
' 3. Creates a cut-sweep feature using a circular
'    profile.
' 4. Accesses the cut-sweep feature.
' 5. Changes the diameter of the circular profile.
' 6. Examine the Immediate window, FeatureManager
'    design tree, and graphics area.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeature As SldWorks.Feature
Dim swFeatureManager As SldWorks.FeatureManager
Dim swSweepFeatureData As SldWorks.SweepFeatureData
Dim status As Boolean
Dim errors As Long
Dim warnings As Long

Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Select the edge for the cut-sweep feature
    status = swModelDocExt.SelectByID2("", "EDGE", -3.72983839416747E-02, 3.93904284381961E-02, 4.95042874504179E-02, True, 4, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
```

```
    'Create the cut-sweep feature using a circular profile
    Set swFeature = swFeatureManager.InsertCutSwept5(False, True, 0, False, False, 0, 0, False, 0, 0, 0, 0, True, True, 0, True, True, True, False, True, 0.0254, swSweepDirection_e.swSweepDirection1)
```

```
    'Roll back the cut-sweep feature to access and change the diameter of circular profile
    Set swSweepFeatureData = swFeature.GetDefinition
    status = swSweepFeatureData.AccessSelections(swModel, Nothing)
    Debug.Print "Using a circular profile? " & swSweepFeatureData.CircularProfile
    Debug.Print "Original size of circular profile = " & swSweepFeatureData.CircularProfileDiameter
    swSweepFeatureData.CircularProfileDiameter = 0.003
    Debug.Print "Modified size of circular profile = " & swSweepFeatureData.CircularProfileDiameter
    Debug.Print "Direction of cut-sweep = " & swSweepFeatureData.Direction
```

```
    'Roll forward the cut-sweep feature
    swFeature.ModifyDefinition swSweepFeatureData, swModel, Nothing
```

```
End Sub
```
