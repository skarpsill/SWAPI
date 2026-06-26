---
title: "Get Hole Series Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Hole_Series_Information_Example_VB.htm"
---

# Get Hole Series Information Example (VBA)

This example shows how to get information about a hole series.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly that contains a hole series feature.
 ' 2. Configure holes and fasteners in the SOLIDWORKS Toolbox.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swDoc As SldWorks.ModelDoc2
 Dim SelMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean
 Dim swFeat As SldWorks.Feature
 Dim swFeatData As SldWorks.HoleSeriesFeatureData2
 Dim swFace As SldWorks.Face2
 Dim swEnt As SldWorks.Entity

Sub main()
    Set swApp = Application.SldWorks
     Set swDoc = swApp.ActiveDoc
     Set SelMgr = swDoc.SelectionManager
     Set swFeat = swDoc.FirstFeature
    Do While Not swFeat Is Nothing
         Debug.Print swFeat.GetTypeName  & ", " & swFeat.Name
           If swFeat.GetTypeName = "HoleSeries" Then
                Set swFeatData = swFeat.GetDefinition
                Debug.Print "Design standard:", swFeatData.Standard
               Dim i As Long
               For i = 0 To swFeatData.GetComponentsCount - 1
                 Debug.Print "Component " & i
                 Debug.Print "  Type:", swFeatData.Type(i)
                 Debug.Print "  Size:", swFeatData.Size(i)
                Next
               Debug.Print "FastenerMaterial:", swFeatData.Material
               ' Bolt and nut information causes an error
                ' if SOLIDWORKS Toolbox is not configured
                Debug.Print "BoltHeadDiameter:", swFeatData.BoltHeadDiameter
                Debug.Print "BoltDiameter:", swFeatData.BoltDiameter
                Debug.Print "NutDiameter:", swFeatData.NutDiameter
                Debug.Print "FastenerPreload:", swFeatData.Preload
                Debug.Print "FastenerDefaultUnits:", swFeatData.FastenerDefaultUnits
                Debug.Print "FastenerTopHoleType:", swFeatData.FastenerTopHoleType
                Debug.Print "FastenerBottomHoleType:", swFeatData.FastenerBottomHoleType
                Debug.Print "FastenerHoleCount:", swFeatData.FastenerHoleCount
                ' End face
                 swFeatData.AccessSelections swDoc, Nothing
                 Set swFace = swFeatData.EndFace
                 Set swEnt = swFace
                If Not swEnt Is Nothing Then
                     boolstatus = swEnt.Select4(False, Nothing)
                     Debug.Print " Face selection = " & boolstatus
                 End If
                ' Sketch points
                 Dim ncount As Long
                 ncount = swFeatData.GetSketchPointsCount
                 Debug.Print " Sketch Point Count = " & ncount
                Dim vPtArr As Variant
                 vPtArr = swFeatData.GetSketchPoints
                Dim swSketchPoint As SldWorks.SketchPoint
                For i = 0 To i = ncount - 1
                    Set swSketchPoint = vPtArr(i)
                    swSketchPoint.Select4 False, Nothing
                 Next
               ' Components
                ncount = swFeatData.GetComponentsCount
                Debug.Print "ComponentsCount Count = " & ncount
                vPtArr = swFeatData.GetComponents
                Dim swComp As Object
               For i = 0 To i = ncount - 1
                  Set swComp = vPtArr(i)
                     If Not swComp Is Nothing Then
                         Debug.Print "  " & swComp.Name2 & " --> " & swComp.GetPathName
                     Else
                        Debug.Print "  Could not get component."
                  End If
                 Next
                swFeatData.ReleaseSelectionAccess
            End If
        Set swFeat = swFeat.GetNextFeature
    Loop

End Sub
```
