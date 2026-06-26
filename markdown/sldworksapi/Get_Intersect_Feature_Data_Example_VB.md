---
title: "Get Intersect Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Intersect_Feature_Data_Example_VB.htm"
---

# Get Intersect Feature Data Example (VBA)

This example shows how to create an intersect feature and get its data.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part that contains the following intersecting features:
 '    * Boss-Extrude1
 '    * Boss-Extrude2
 '    * Boss-Extrude3
 '    * Boss-Extrude4
 '    * Surface-Extrude1
 ' 2. Open an Immediate window.
 ' 3. Multi-select Surface-Extrude1, Boss-Extrude3, and  Boss-Extrude4 in the
 '    FeatureManager design tree and press F5.
 '
 ' Postconditions:
 ' 1. When the macro stops, hide Boss-Extrude3 and Boss-Extrude4 in the
 '    FeatureManager design tree.
 ' 2. Press F5.
 ' 3. When the macro stops, inspect the blue intersect regions.
 ' 4. Press F5.
 ' 5. Inspect the Immediate window.
 ' 6. Right-click Intersect1 in the FeatureManager design tree and click
 '    Roll Forward.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------

Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swFeat As SldWorks.Feature
 Dim swFeatMgr As SldWorks.FeatureManager
 Dim featData As SldWorks.IntersectFeatureData
 Dim intStatus As Long
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swFeatMgr = swModel.FeatureManager
    Dim vResultingBodies As Variant
    vResultingBodies = swFeatMgr.PreIntersect(False) 'Do not cap planar surface openings of intersect feature
     swModel.ClearSelection2 True

    Dim i As Integer
     Dim swBody As Body2

    Stop 'Hide Boss-Extrude4 and Boss-Extrude3 to expose the intersect regions

    Debug.Print ""
     'Color the intersect regions blue
     For i = 0 To UBound(vResultingBodies)
         Set swBody = vResultingBodies(i)
         Debug.Print "Intersect region " & i + 1 & " is a temporary body? " & swBody.IsTemporaryBody
         intStatus = swBody.Display3(swModel, 16711680, swTempBodySelectOptionNone)
         Debug.Print "Intersect region " & i + 1 & " is displayed (0 = yes)? " & intStatus
     Next
    Stop 'Observe the intersect regions

    Dim intToExclude As Variant
     Dim boolArr(3) As Boolean
     boolArr(0) = False
     boolArr(1) = True 'Exclude region, vResultingBodies(2), from the intersect feature
     boolArr(2) = False
     boolArr(3) = False
     intToExclude = boolArr
     Set swFeat = swFeatMgr.PostIntersect(intToExclude, True, False)

    Debug.Print "Feature name = " & swFeat.Name
     Set featData = swFeat.GetDefinition

    Debug.Print "Merge touching regions into one body? " & featData.Merge
     Debug.Print "Consume surfaces? " & featData.Consume
     Debug.Print "Cap planar openings on surfaces? " & featData.CapPlanar
    Debug.Print "Number of solids, surfaces, or planes used to create the intersect feature: " & featData.GetIntersectionsToolsCount
     Debug.Print "Number of intersect regions: " & featData.GetIntersectionsCount
End Sub
```
