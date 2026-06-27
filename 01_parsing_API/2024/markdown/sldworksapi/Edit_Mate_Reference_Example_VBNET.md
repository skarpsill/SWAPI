---
title: "Edit Mate Reference Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Mate_Reference_Example_VBNET.htm"
---

# Edit Mate Reference Example (VB.NET)

This example shows how to insert and edit a mate reference.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Adds a mate reference.
' 3. Edits the mate reference.
' 4. Expand MateReferences in the FeatureManager design tree
'    and click MyDefault<1>.
' 5. Examine the graphics area and Immediate window.
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
        Dim swFeature As Feature
        Dim swFeatureMgr As FeatureManager
        Dim swSelectionMgr As SelectionMgr
        Dim swPlane As Entity
        Dim swFace As Face2
        Dim swMateReference As MateReference
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Insert mate reference
        status = swModelDocExt.SelectByID2("Front", "PLANE", 0, 0, 0, True, 1, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swPlane = swSelectionMgr.GetSelectedObject6(1, -1)
        status = swModelDocExt.SelectByID2("", "FACE", 0.00835786916030656, 0.00429540237419701, 0, True, 2, Nothing, 0)
        swFeatureMgr = swModel.FeatureManager
        swFeature = swFeatureMgr.InsertMateReference2("Default", Nothing, 0, 1, False, Nothing, 0, 2, False, Nothing, 0, 0)
        swModel.ClearSelection2(True)

        'Edit mate reference
        status = swModelDocExt.SelectByID2("", "FACE", 0.0117890806857872, 0.00419179196288511, 0.00999999999999091, False, 0, Nothing, 0)
        swFace = swSelectionMgr.GetSelectedObject6(1, -1)
        status = swModelDocExt.SelectByID2("Default-<1>", "POSGROUP", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swMateReference = swFeature.GetSpecificFeature2
        swModel.ClearSelection2(True)
        status = swMateReference.Edit("MyDefault", swPlane, swMateReferenceType_e.swMateReferenceType_default, swMateReferenceAlignment_e.swMateReferenceAlignment_Any, swFace, swMateReferenceType_e.swMateReferenceType_default, swMateReferenceAlignment_e.swMateReferenceAlignment_Any, Nothing, swMateReferenceType_e.swMateReferenceType_default, swMateReferenceAlignment_e.swMateReferenceAlignment_Any)
        Debug.Print("Mate reference modified and replaced? " & status)

        swModel.EditRebuild3()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
