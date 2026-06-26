---
title: "Mirror Sheet-metal Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Mirror_Sheet-metal_Part_Example_VBNET.htm"
---

# Mirror Sheet-metal Part Example (VB.NET)

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
' NOTE: Because this part document is used elsewhere, do not
' save changes.
'---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureMgr As FeatureManager
        Dim swSelMgr As SelectionMgr
        Dim swPart As PartDoc
        Dim swMirrorFeature As Feature
        Dim swFeature As Feature
        Dim swResultPart As ModelDoc2 = Nothing
        Dim swMirrorFeatData As MirrorPartFeatureData
        Dim swRefPlane As RefPlane
        Dim swPlane As Entity
        Dim mirrorOptions As Integer
        Dim mirrorType As Integer
        Dim selType As swSelectType_e
        Dim filename As String
        Dim errors As Integer
        Dim status As Boolean
        Dim warnings As Integer

        filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.sldprt"
        swModel = swApp.OpenDoc6(filename, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        If swModel Is Nothing Then Exit Sub
        If swModel.GetType <> swDocumentTypes_e.swDocPART Then Exit Sub

        swModelDocExt = swModel.Extension
        swFeatureMgr = swModel.FeatureManager
        status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swRefPlane = swFeatureMgr.InsertRefPlane(8, 0.09, 0, 0, 0, 0)
        status = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        selType = swSelMgr.GetSelectedObjectType3(1, -1)
        If Not (selType = swSelectType_e.swSelDATUMPLANES) Then Exit Sub

        swPart = swModel
        mirrorOptions = swMirrorPartOptions_e.swMirrorPartOptions_ImportSMInfo + swMirrorPartOptions_e.swMirrorPartOptions_ImportIndProps + swMirrorPartOptions_e.swMirrorPartOptions_ImportSolids + swMirrorPartOptions_e.swMirrorPartOptions_ImportCutListProperties
        swMirrorFeature = swPart.MirrorPart2(False, mirrorOptions, swResultPart)
        If swMirrorFeature Is Nothing Then
            Debug.Print("No feature!")
        Else
            Debug.Print("Feature: " & swMirrorFeature.Name)
        End If

        If swResultPart Is Nothing Then
            Debug.Print("No new part! ")
        Else
            Debug.Print("Part document title: " & swResultPart.GetTitle)
        End If

        swModel = swApp.ActiveDoc
        swMirrorFeature.Select2(False, -1)
        swSelMgr = swModel.SelectionManager
        swFeature = swSelMgr.GetSelectedObject6(1, -1)
        swMirrorFeatData = swFeature.GetDefinition

        swMirrorFeatData.AccessSelections(swModel, Nothing)

        Debug.Print("  Path name = " & swMirrorFeatData.PathName)
        Debug.Print("  Import:  ")
        Debug.Print("     Solid bodies?  " & swMirrorFeatData.SolidBodies)
        Debug.Print("     Cut-list properties? " & swMirrorFeatData.CutListProperties)
        Debug.Print("     Sheet-metal information? " & swMirrorFeatData.SheetMetalInformation)
        Debug.Print("     Unlocked properties?  " & swMirrorFeatData.UnlockedProperties)

        mirrorType = swMirrorFeatData.GetMirrorPlaneType
        Debug.Print("  Mirror plane type as defined in swMirrorPlaneType_e = " & mirrorType)
        swRefPlane = swMirrorFeatData.GetMirrorPlane
        swMirrorFeatData.ReleaseSelectionAccess()
        swPlane = swRefPlane
        swPlane.Select(False)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
