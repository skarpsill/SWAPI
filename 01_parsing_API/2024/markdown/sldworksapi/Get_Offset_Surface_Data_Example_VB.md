---
title: "Get Offset Surface Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Offset_Surface_Data_Example_VB.htm"
---

# Get Offset Surface Data Example (VBA)

This example shows how to get data for an offset surface.

```vb
 '------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document that contains a component that
 '    has a surface offset feature.
 ' 2. Select the component's surface offset feature.
 ' 3. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '-----------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swSelData               As SldWorks.SelectData
     Dim swOffset                As SldWorks.SurfaceOffsetFeatureData
     Dim swFeat                  As SldWorks.Feature
     Dim swEnt                   As SldWorks.Entity
     Dim vFace                   As Variant
     Dim i                       As Long
     Dim bRet                    As Boolean
     Dim comp                    As SldWorks.Component2
     Dim swCompFace              As SldWorks.Component2

    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swSelData = swSelMgr.CreateSelectData
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swOffset = swFeat.GetDefinition
     Set comp = swSelMgr.GetSelectedObjectsComponent3(1, -1)

    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "CompFeature = " & comp.Name2
     Debug.Print "  " & swFeat.Name
     Debug.Print "    Distance       = " & swOffset.Distance * 1000# & " mm"
     Debug.Print "    Flip           = " & swOffset.Flip
     Debug.Print "    FacesCount     = " & swOffset.GetEntitiesCount
    bRet = swOffset.AccessSelections(swModel, comp)
    swModel.ClearSelection2 True
    vFace = swOffset.Entities
    For i = 0 To UBound(vFace)
         Set swEnt = vFace(i)
         Debug.Print "    Entity selected = " & swEnt.Select4(True, Nothing)
        Set swCompFace = swEnt.GetComponent
         Debug.Print "    Component face = " & swCompFace.Name2
    Next i
    swOffset.ReleaseSelectionAccess
End Sub
```
