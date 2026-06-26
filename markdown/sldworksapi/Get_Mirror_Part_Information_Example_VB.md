---
title: "Get Mirror Part Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mirror_Part_Information_Example_VB.htm"
---

# Get Mirror Part Information Example (VBA)

This example shows how to get information about a mirror part.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part that contains a reference plane about which to mirror the part.
 ' 2. Select the reference plane in the FeatureManager design tree.
 '
 ' Postconditions:
 ' 1. Creates and mirrors a part about the selected reference plane.
 ' 2. Shows the reference plane in the graphics area.
 ' 3. Inspect the Immediate window for mirror part feature data.
 '---------------------------------------------------------------------------
 Option Explicit
 Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim selMgr As SldWorks.SelectionMgr
 Dim swPart As SldWorks.PartDoc
 Dim mirrorFeature As SldWorks.Feature
 Dim myFeature As SldWorks.Feature
 Dim resultPart As SldWorks.ModelDoc2
 Dim mirrorFeatData As SldWorks.MirrorPartFeatureData
 Dim refPlane As SldWorks.refPlane
 Dim facePlane As SldWorks.Face2
 Dim mirrorOptions  As Long
 Dim faceType As Long
 Dim selType As swSelectType_e
 Dim message As String
Sub main()

    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc

    If swModel Is Nothing Then Exit Sub
     If swModel.GetType <> swDocPART Then Exit Sub

    Set selMgr = swModel.SelectionManager

    If selMgr.GetSelectedObjectCount2(-1) = 0 Then Exit Sub

    selType = selMgr.GetSelectedObjectType3(1, -1)
     If Not (selType = swSelDATUMPLANES Or selType = swSelFACES) Then Exit Sub

    Set swPart = swModel

    mirrorOptions = swMirrorPartOptions_ImportSolids + _
                     swMirrorPartOptions_ImportCustomProperties + _
                     swMirrorPartOptions_ImportCutListProperties

    Set mirrorFeature = swPart.MirrorPart2(False, mirrorOptions, resultPart)

    If mirrorFeature Is Nothing Then
         message = "No Feature"
     Else
         message = "Feature: " & mirrorFeature.Name
     End If

    If resultPart Is Nothing Then
         Debug.Print "No new part. " & message
     Else
         Debug.Print resultPart.GetTitle & ". " & message
     End If

    Set swModel = swApp.ActiveDoc
     Set selMgr = swModel.SelectionManager
     mirrorFeature.Select2 False, -1

    Set myFeature = selMgr.GetSelectedObject6(1, -1)
     Set mirrorFeatData = myFeature.GetDefinition

    mirrorFeatData.AccessSelections swModel, Nothing

    Debug.Print "  Path name = " & mirrorFeatData.PathName
     Debug.Print "  Import surface bodies? = " & mirrorFeatData.SurfaceBodies
     Debug.Print "  Import solid bodies? = " & mirrorFeatData.SolidBodies
     Debug.Print "  Import custom properties? = " & mirrorFeatData.CustomProperties
     Debug.Print "  Import cut-list properties? = " & mirrorFeatData.CutListProperties

    faceType = mirrorFeatData.GetMirrorPlaneType
     Debug.Print "  Mirror plane type as defined in swMirrorPlaneType_e = " & faceType

    Dim plane As SldWorks.Entity
     If faceType = 1 Then
         Set refPlane = mirrorFeatData.GetMirrorPlane
         mirrorFeatData.ReleaseSelectionAccess
         Set plane = refPlane
         plane.Select False
     Else
         Set facePlane = mirrorFeatData.GetMirrorPlane
         mirrorFeatData.ReleaseSelectionAccess
         Set plane = facePlane
         plane.Select False
     End If

End Sub
```
