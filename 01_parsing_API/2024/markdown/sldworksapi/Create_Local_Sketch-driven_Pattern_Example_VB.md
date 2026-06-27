---
title: "Create Local Sketch-driven Pattern Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Local_Sketch-driven_Pattern_Example_VB.htm"
---

# Create Local Sketch-driven Pattern Example (VBA)

This example shows how to create a local sketch-driven pattern feature.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly document.
' 2. Creates a sketch for the local sketch-driven
'    pattern feature.
' 3. Selects an assembly component and the just-created
'    sketch for the local sketch-driven pattern feature.
' 4. Creates the local sketch-driven pattern feature.
' 5. Gets values and settings of the local sketch-driven
'    pattern feature.
' 6. Examine the Immediate window and graphics area.
'
' NOTE: Because this assembly is used elsewhere, do not save changes.
'------------------------------------------------------------------------------
```

```
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As ModelDoc2
Dim swSketchMgr As SldWorks.SketchManager
Dim swSketchPoint As SldWorks.SketchPoint
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatMgr As FeatureManager
Dim swFeat As Feature
Dim swLocalSketchPatternFeat As SldWorks.LocalSketchPatternFeatureData
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
```

```
    'Open assembly document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\assem1.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Create sketch
    Set swSketchMgr = swModel.SketchManager
    swSketchMgr.InsertSketch True
    Set swSketchPoint = swSketchMgr.CreatePoint(0.025, -0.05, 0#)
    Set swSketchPoint = swSketchMgr.CreatePoint(0.05, -0.075, 0#)
    Set swSketchPoint = swSketchMgr.CreatePoint(0.1, -0.05, 0#)
    swSketchMgr.InsertSketch True

    'Select a component and the just-created sketch
    'for the local sketch-driven pattern feature
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("TestPart1-1@assem1", "COMPONENT", 0, 0, 0, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 16, Nothing, 0)
```

```vb
    'Create local sketch-driven pattern feature
     Set swFeatMgr = swModel.FeatureManager
     Set swLocalSketchPatternFeat = swFeatMgr.CreateDefinition(swFmLocalSketchPattern)
     swLocalSketchPatternFeat.ReferencePoint = 1 'Bounding box center
     Set swFeat = swFeatMgr.CreateFeature(swLocalSketchPatternFeat)

     'Get local sketch-driven pattern feature data
     Set swLocalSketchPatternFeat = swFeat.GetDefinition
     Debug.Print "Local sketch-driven pattern properties: "
     Debug.Print "  Number of components: " & swLocalSketchPatternFeat.GetPatternComponentCount
     Debug.Print "  Number of items skipped: " & swLocalSketchPatternFeat.GetSkippedItemCount
     Debug.Print "  Type of reference point as defined in swLocalSketchPatternReferencePoint_e: " & swLocalSketchPatternFeat.ReferencePoint
```

```
End Sub
```
