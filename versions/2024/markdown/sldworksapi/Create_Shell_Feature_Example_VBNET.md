---
title: "Create Shell Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Shell_Feature_Example_VBNET.htm"
---

# Create Shell Feature Example (VB.NET)

This example shows how to create a shell feature..

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified model document exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
  ' 1. Selects a face to remove from the model to create the shell.
 ' 2. Creates Shell1.
 ' 3. Inspect the Immediate window, graphics area, and
 '    FeatureManager design tree.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swSelData As SelectData
     Dim swFeat As Feature
     Dim swShell As ShellFeatureData
     Dim vFaceRemArr As Object
     Dim vFaceRem As Object
     Dim swFaceRem As Face2
     Dim vMultiFaceArr As Object
     Dim vMultiFace As Object
     Dim swMultiFace As Face2
     Dim swEnt As Entity
     Dim i As Integer
     Dim bRet As Boolean
     Dim longstatus As Integer, longwarnings As Integer

     Sub main()

         swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
         swApp.ActivateDoc2("block20", False, longstatus)
         swModel = swApp.ActiveDoc

         bRet = swModel.Extension.SelectByID2("", "FACE", -0.0150558029249623, 0.0396239999999466, -0.018063862472502, False, 1, Nothing, 0)
         swModel.InsertFeatureShell(0.00254, False)

         swSelMgr = swModel.SelectionManager
         swSelData = swSelMgr.CreateSelectData
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swShell = swFeat.GetDefinition

         ' Get shell data
         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  " & swFeat.Name)
         Debug.Print("    Direction: " & swShell.Direction)
         Debug.Print("    Thickness: " & swShell.Thickness * 1000.0# & " mm")
         Debug.Print("    Count of faces removed: " & swShell.FacesRemovedCount)
         Debug.Print("    Count of faces with alternative thicknesses: " & swShell.GetMultipleThicknessFacesCount)

         bRet = swShell.AccessSelections(swModel, Nothing)
         swModel.ClearSelection2(True)

         vFaceRemArr = swShell.FacesRemoved

         For Each vFaceRem In vFaceRemArr
             swFaceRem = vFaceRem
             swEnt = swFaceRem

             bRet = swEnt.Select4(True, swSelData)
         Next

         swModel.ClearSelection2(True)
         vMultiFaceArr = swShell.MultipleThicknessFaces

         For Each vMultiFace In vMultiFaceArr
             swMultiFace = vMultiFace
             swEnt = swMultiFace

             Debug.Print("    Alternative thickness in mm at face (" & i & "): " & swShell.GetMultipleThicknessAtIndex(i) * 1000.0#)
             i = i + 1

             bRet = swEnt.Select4(True, swSelData)
         Next

         swModel.ClearSelection2(True)
         swShell.ReleaseSelectionAccess()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
