---
title: "Get Gusset Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Gusset_Feature_Data_Example_VBNET.htm"
---

# Get Gusset Feature Data Example (VB.NET)

This example shows how to get some data for a gusset feature.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects and gets the Gusset1 feature.
' 3. Gets some Gusset1 feature data.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swGussetFeatureData As GussetFeatureData
        Dim status As Boolean
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim oneFace As Face2 = Nothing
        Dim twoFace As Face2 = Nothing

        'Open part document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\weldment_box3.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Select and get Gusset1
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Gusset1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swGussetFeatureData = swFeature.GetDefinition

        'Access Gusset1 and get some feature data
        swGussetFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Profile type: " & swGussetFeatureData.ProfileType)
        Debug.Print("Thickness type: " & swGussetFeatureData.ThicknessType)
        Debug.Print("Thickness: " & swGussetFeatureData.Thickness)
        If swGussetFeatureData.OffsetUsed = True Then
            Debug.Print("Profile offset distance: " & swGussetFeatureData.ProfileOffsetDistance)
        Else
            Debug.Print("No profile offset used.")
        End If
        status = swGussetFeatureData.GetSupportingFaces(oneFace, twoFace)
        status = oneFace.IsSame(twoFace)
        Debug.Print("Is the first supporting face the same as the second supporting face: " & status)
        swGussetFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
