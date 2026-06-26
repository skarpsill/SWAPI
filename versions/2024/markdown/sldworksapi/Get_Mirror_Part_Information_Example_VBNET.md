---
title: "Get Mirror Part Information Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mirror_Part_Information_Example_VBNET.htm"
---

# Get Mirror Part Information Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim selMgr As SelectionMgr
     Dim swPart As PartDoc
     Dim mirrorFeature As Feature
     Dim myFeature As Feature
     Dim resultPart As ModelDoc2
     Dim mirrorFeatData As MirrorPartFeatureData
     Dim refPlane As RefPlane
     Dim facePlane As Face2
     Dim mirrorOptions As Integer
     Dim faceType As Integer
     Dim selType As swSelectType_e
     Dim message As String

     Sub main()

         swModel = swApp.ActiveDoc

         If swModel Is Nothing Then  Exit  Sub
         If swModel.GetType <> swDocumentTypes_e.swDocPART  Then  Exit  Sub

         selMgr = swModel.SelectionManager

         If selMgr.GetSelectedObjectCount2(-1) = 0  Then  Exit  Sub

         selType = selMgr.GetSelectedObjectType3(1, -1)
         If Not (selType = swSelectType_e.swSelDATUMPLANES Or selType = swSelectType_e.swSelFACES) Then Exit  Sub

         swPart = swModel

         mirrorOptions = swMirrorPartOptions_e.swMirrorPartOptions_ImportSolids + _
                         swMirrorPartOptions_e.swMirrorPartOptions_ImportCustomProperties + _
                         swMirrorPartOptions_e.swMirrorPartOptions_ImportCutListProperties

         mirrorFeature = swPart.MirrorPart2(False, mirrorOptions, resultPart)

         If mirrorFeature Is Nothing Then
             message =  "No Feature"
         Else
             message =  "Feature: " & mirrorFeature.Name
         End If

         If resultPart Is Nothing Then
             Debug.Print("No new part. " & message)
         Else
             Debug.Print(resultPart.GetTitle & ". " & message)
         End If

         swModel = swApp.ActiveDoc
         selMgr = swModel.SelectionManager
         mirrorFeature.Select2(False, -1)

         myFeature = selMgr.GetSelectedObject6(1, -1)
         mirrorFeatData = myFeature.GetDefinition

         mirrorFeatData.AccessSelections(swModel,  Nothing)

         Debug.Print("  Path name = " & mirrorFeatData.PathName)
         Debug.Print("  Import surface bodies? = " & mirrorFeatData.SurfaceBodies)
         Debug.Print("  Import solid bodies? = " & mirrorFeatData.SolidBodies)
         Debug.Print("  Import custom properties? = " & mirrorFeatData.CustomProperties)
         Debug.Print("  Import cut-list properties? = " & mirrorFeatData.CutListProperties)

         faceType = mirrorFeatData.GetMirrorPlaneType
         Debug.Print("  Mirror plane type as defined in swMirrorPlaneType_e = " & faceType)

         Dim plane As Entity
         If faceType = 1 Then
             refPlane = mirrorFeatData.GetMirrorPlane
             mirrorFeatData.ReleaseSelectionAccess()
             plane = refPlane
             plane.Select(False)
         Else
             facePlane = mirrorFeatData.GetMirrorPlane
             mirrorFeatData.ReleaseSelectionAccess()
             plane = facePlane
             plane.Select(False)
         End If

     End Sub

     Public swApp As SldWorks

 End  Class
```
