---
title: "Get Tooling Split Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Tooling_Split_Feature_Data_Example_VB.htm"
---

# Get Tooling Split Feature Data Example (VBA)

This example shows how to get tooling split feature data.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document that contains a Tooling Split1 feature.
 ' 2. Select Tooling Split1 in the FeatureManager design tree.
 ' 3. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '----------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swFeat As SldWorks.Feature
 Dim swToolingSplitFeatData As SldWorks.ToolingSplitFeatureData
 Dim bod As SldWorks.Body2
 Dim bRet As Boolean
 Dim i As Long
 Dim cavSurf As Variant
 Dim coreSurf As Variant
 Dim partSurf As Variant
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swToolingSplitFeatData = swFeat.GetDefinition

    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  " & swFeat.Name
     Debug.Print "    Draft angle: " & swToolingSplitFeatData.Angle
     Debug.Print "    Depth of block in direction 1: " & swToolingSplitFeatData.Depth(0)
     Debug.Print "    Depth of block in direction 2: " & swToolingSplitFeatData.Depth(1)
     Debug.Print "    Interlock surface? " & swToolingSplitFeatData.InterlockSurface

    bRet = swToolingSplitFeatData.AccessSelections(swModel, Nothing)

    Debug.Print "    Cavity surfaces:"
     Debug.Print "    Count: " & swToolingSplitFeatData.GetCavitySurfacesCount
     cavSurf = swToolingSplitFeatData.CavitySurfaces
     For i = 0 To swToolingSplitFeatData.GetCavitySurfacesCount - 1
         Set bod = cavSurf(i)
         Debug.Print "      " & bod.Name
     Next
     Debug.Print "    Core surfaces:"
     Debug.Print "    Count: " & swToolingSplitFeatData.GetCoreSurfacesCount
     coreSurf = swToolingSplitFeatData.CoreSurfaces
     For i = 0 To swToolingSplitFeatData.GetCoreSurfacesCount - 1
         Set bod = coreSurf(i)
         Debug.Print "      " & bod.Name
     Next
     Debug.Print "    Parting surfaces:"
     Debug.Print "    Count: " & swToolingSplitFeatData.GetPartingSurfacesCount
     partSurf = swToolingSplitFeatData.PartingSurfaces
     For i = 0 To swToolingSplitFeatData.GetPartingSurfacesCount - 1
         Set bod = partSurf(i)
         Debug.Print "      " & bod.Name
     Next

    swToolingSplitFeatData.ReleaseSelectionAccess

End Sub
```
