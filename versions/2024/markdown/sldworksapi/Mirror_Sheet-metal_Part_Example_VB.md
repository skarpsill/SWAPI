---
title: "Mirror Sheet-metal Part Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Mirror_Sheet-metal_Part_Example_VB.htm"
---

# Mirror Sheet-metal Part Example (VBA)

This example shows how to mirror a sheet-metal part.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the sheet-metal part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified sheet-metal part.
' 2. Creates a reference plane about which to mirror the
'    sheet-metal part.
' 3. Creates a new part document containing the mirrored
'    sheet-metal part, which includes the sheet-metal
'    information in the mirrored part.
' 4. Examine the graphics area and the Immediate window.
'
' NOTE: Because this part document is used elsewhere, do
' not save changes.
'---------------------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swSelMgr As SldWorks.SelectionMgr
Dim swPart As SldWorks.PartDoc
Dim swMirrorFeature As SldWorks.Feature
Dim swFeature As SldWorks.Feature
Dim swResultPart As SldWorks.ModelDoc2
Dim swMirrorFeatData As SldWorks.MirrorPartFeatureData
Dim swRefPlane As SldWorks.refPlane
Dim swPlane As SldWorks.Entity
Dim mirrorOptions As Long
Dim mirrorType As Long
Dim selType As swSelectType_e
Dim filename As String
Dim errors As Long
Dim status As Boolean
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.sldprt"
    Set swModel = swApp.OpenDoc6(filename, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    If swModel Is Nothing Then Exit Sub
    If swModel.GetType <> swDocPART Then Exit Sub
```

```
    Set swModelDocExt = swModel.Extension
    Set swFeatureMgr = swModel.FeatureManager
    status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swRefPlane = swFeatureMgr.InsertRefPlane(8, 0.09, 0, 0, 0, 0)
    status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    selType = swSelMgr.GetSelectedObjectType3(1, -1)
    If Not (selType = swSelDATUMPLANES) Then Exit Sub

    Set swPart = swModel
    mirrorOptions = swMirrorPartOptions_ImportSMInfo + swMirrorPartOptions_ImportIndProps + swMirrorPartOptions_ImportSolids + swMirrorPartOptions_ImportCutListProperties
    Set swMirrorFeature = swPart.MirrorPart2(False, mirrorOptions, swResultPart)
    If swMirrorFeature Is Nothing Then
        Debug.Print "No feature!"
    Else
        Debug.Print "Feature: " & swMirrorFeature.Name
   End If
```

```
    If swResultPart Is Nothing Then
        Debug.Print "No new part! "
    Else
        Debug.Print "Part document title: " & swResultPart.GetTitle
    End If
```

```
    Set swModel = swApp.ActiveDoc
    swMirrorFeature.Select2 False, -1
    Set swSelMgr = swModel.SelectionManager
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    Set swMirrorFeatData = swFeature.GetDefinition
```

```
    swMirrorFeatData.AccessSelections swModel, Nothing
```

```
    Debug.Print "  Path name = " & swMirrorFeatData.PathName
    Debug.Print "  Import:  "
    Debug.Print "     Solid bodies?  " & swMirrorFeatData.SolidBodies
    Debug.Print "     Cut-list properties? " & swMirrorFeatData.CutListProperties
    Debug.Print "     Sheet-metal information?  " & swMirrorFeatData.SheetMetalInformation
    Debug.Print "     Unlocked properties?  " & swMirrorFeatData.UnlockedProperties
```

```
    mirrorType = swMirrorFeatData.GetMirrorPlaneType
    Debug.Print "  Mirror plane type as defined in swMirrorPlaneType_e = " & mirrorType
    Set swRefPlane = swMirrorFeatData.GetMirrorPlane
    swMirrorFeatData.ReleaseSelectionAccess
    Set swPlane = swRefPlane
    swPlane.Select False
```

```
End Sub
```
