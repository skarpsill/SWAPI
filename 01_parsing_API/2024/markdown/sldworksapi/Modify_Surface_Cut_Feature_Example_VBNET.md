---
title: "Modify Surface-cut Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Surface_Cut_Feature_Example_VBNET.htm"
---

# Modify Surface-cut Feature Example (VB.NET)

This example shows how to modify a surface-cut feature.

```vb
  '-------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the part to open exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Flips the direction of the surface-cut feature.
  ' 2. Examine the Immediate window.
 '
 ' NOTE: Because this part is used elsewhere, do not save changes.
  '-------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModel As ModelDoc
         Dim swModelDocExt As ModelDocExtension
         Dim swSelMgr As SelectionMgr
         Dim swFeature As Feature
         Dim swSurfCutFeature As SurfCutFeatureData
         Dim status As Boolean
         Dim errors As Integer, warnings As Integer
         Dim fileName As String

         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\SurfCut.sldprt"
         swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension

         ' Get the surface-cut feature
         status = swModelDocExt.SelectByID2("SurfaceCut1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         swSelMgr = swModel.SelectionManager
         swFeature = swSelMgr.GetSelectedObject6(1, -1)
         swSurfCutFeature = swFeature.GetDefinition
         status = swSurfCutFeature.AccessSelections(swModel, Nothing)

         ' Flip direction of surface cut
         swSurfCutFeature.Flip = True
         Debug.Print("Surface-cut feature flipped: " & status)

         ' Update definition of feature
         swFeature.ModifyDefinition(swSurfCutFeature, swModel, Nothing)

         ' Rebuild part
         swModel.EditRebuild3()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
