---
title: "Create Shell Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Shell_Feature_Data_Example_VB.htm"
---

# Create Shell Feature Example (VBA)

This example shows how to create a shell feature.

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

Dim swApp                   As SldWorks.SldWorks
 Dim swModel                 As SldWorks.ModelDoc2
 Dim swSelMgr                As SldWorks.SelectionMgr
 Dim swSelData               As SldWorks.SelectData
 Dim swFeat                  As SldWorks.Feature
 Dim swShell                 As SldWorks.ShellFeatureData
 Dim vFaceRemArr             As Variant
 Dim vFaceRem                As Variant
 Dim swFaceRem               As SldWorks.Face2
 Dim vMultiFaceArr           As Variant
 Dim vMultiFace              As Variant
 Dim swMultiFace             As SldWorks.Face2
 Dim swEnt                   As SldWorks.Entity
 Dim i                       As Long
 Dim bRet                    As Boolean
 Dim longstatus As Long, longwarnings As Long
Option Explicit
Sub main()
    Set swApp = Application.SldWorks

    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "block20", False, longstatus
     Set swModel = swApp.ActiveDoc

    bRet = swModel.Extension.SelectByID2("", "FACE", -1.50558029249623E-02, 3.96239999999466E-02, -0.018063862472502, False, 1, Nothing, 0)
     swModel.InsertFeatureShell 0.00254, False

    Set swSelMgr = swModel.SelectionManager
     Set swSelData = swSelMgr.CreateSelectData
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swShell = swFeat.GetDefinition
    ' Get shell data
     Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  " & swFeat.Name
     Debug.Print "    Direction: " & swShell.Direction
     Debug.Print "    Thickness: " & swShell.Thickness * 1000# & " mm"
     Debug.Print "    Count of faces removed: " & swShell.FacesRemovedCount
     Debug.Print "    Count of faces with alternative thicknesses: " & swShell.GetMultipleThicknessFacesCount
    bRet = swShell.AccessSelections(swModel, Nothing)
     swModel.ClearSelection2 True
    vFaceRemArr = swShell.FacesRemoved
    For Each vFaceRem In vFaceRemArr
         Set swFaceRem = vFaceRem
         Set swEnt = swFaceRem
        bRet = swEnt.Select4(True, swSelData)
     Next
    swModel.ClearSelection2 True
     vMultiFaceArr = swShell.MultipleThicknessFaces
    For Each vMultiFace In vMultiFaceArr
         Set swMultiFace = vMultiFace
         Set swEnt = swMultiFace
        Debug.Print "    Alternative thickness in mm at face (" & i & "): " & swShell.GetMultipleThicknessAtIndex(i) * 1000#
         i = i + 1
        bRet = swEnt.Select4(True, swSelData)
     Next
    swModel.ClearSelection2 True
     swShell.ReleaseSelectionAccess

 End Sub
```
