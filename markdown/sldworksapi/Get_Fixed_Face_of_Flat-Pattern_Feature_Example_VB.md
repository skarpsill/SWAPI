---
title: "Get Fixed Face of Flat-Pattern Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Fixed_Face_of_Flat-Pattern_Feature_Example_VB.htm"
---

# Get Fixed Face of Flat-Pattern Feature Example (VBA)

This example shows how to get the fixed face of a Flat-Pattern feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a sheet metal part and select a Flat-Pattern feature.
 '
 ' Postconditions:
 ' 1. Inspect the graphics area to see that the fixed face
 '    of the Flat-Pattern feature is selected.
 ' 2. Press F5 to run the macro to completion.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFeat                  As SldWorks.Feature
     Dim swFlatPatt              As SldWorks.FlatPatternFeatureData
     Dim swFixedFace             As SldWorks.Face2
     Dim selectData              As SldWorks.selectData
     Dim bRet                    As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)

    Set swFlatPatt = swFeat.GetDefinition
     bRet = swFlatPatt.AccessSelections(swModel, Nothing)
    Set swFixedFace = swFlatPatt.FixedFace2
     bRet = swFixedFace.Select4(True, selectData)

     Stop
     ' Press F5
    swFlatPatt.ReleaseSelectionAccess
End Sub
```
