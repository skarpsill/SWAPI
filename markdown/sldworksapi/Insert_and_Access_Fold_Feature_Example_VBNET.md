---
title: "Insert and Access Fold Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Access_Fold_Feature_Example_VBNET.htm"
---

# Insert and Access Fold Feature Example (VB.NET)

This example shows how to insert and access a fold feature.

```
'---------------------------------------------------------------
' Postconditions:
' 1. Verify that the specified sheet metal part document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified sheet metal part document.
' 2. Creates an unfold feature.
' 3. Creates a fold feature.
' 4. Prints to the Immediate window some fold feature data.
' 5. Examine the FeatureManager design tree and the Immediate window.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'---------------------------------------------------------------
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
        Dim swSelectionMgr As SelectionMgr
        Dim swFoldsFeatureData As FoldsFeatureData
        Dim swFace As Face2
        Dim swBody As Body2
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim i As Integer
        Dim bendsArray() As Object

        'Open sheet metal part
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Insert unfold feature
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", 0.0135437392197275, 0.013831948116092, 0.0180159642212061, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 0.0139765211971223, 0.045779599797811, -0.018375967305019, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("EdgeBend4", "BODYFEATURE", 0.0145403568253926, 0.0461305825900808, -0.00849880301666417, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("EdgeBend5", "BODYFEATURE", 0.013808065447904, 0.0455785871991452, 0.0109703538056465, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("EdgeBend6", "BODYFEATURE", 0.0139037479688966, 0.0457015473971296, 0.0275647689667267, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("", "FACE", 0.0135437392197275, 0.013831948116092, 0.0180159642212061, False, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 0.0139765211971223, 0.045779599797811, -0.018375967305019, True, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("EdgeBend4", "BODYFEATURE", 0.0145403568253926, 0.0461305825900808, -0.00849880301666417, True, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("EdgeBend5", "BODYFEATURE", 0.013808065447904, 0.0455785871991452, 0.0109703538056465, True, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("EdgeBend6", "BODYFEATURE", 0.0139037479688966, 0.0457015473971296, 0.0275647689667267, True, 4, Nothing, 0)
        swModel.InsertSheetMetalUnfold()

        'Insert fold feature
        status = swModelDocExt.SelectByID2("", "FACE", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 0.0135437392197559, 0.0460611937937756, -0.019419982567797, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("Unfold1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", 0, 0, 0, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("EdgeBend3", "BODYFEATURE", 0.0135437392197559, 0.0460611937937756, -0.019419982567797, True, 4, Nothing, 0)
        swModel.InsertSheetMetalFold()

        'Access the fold feature
        status = swModelDocExt.SelectByID2("Fold1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swFoldsFeatureData = swFeature.GetDefinition
        status = swFoldsFeatureData.AccessSelections(swModel, Nothing)

        'Get name of fixed face body in the fold feature
        swFace = swFoldsFeatureData.FixedFace
        swBody = swFace.GetBody
        Debug.Print("Name of the body of the fixed face of the fold feature: " & swBody.Name)

        'Get the names bend features in the fold feature
        bendsArray = swFoldsFeatureData.Bends
        For i = 0 To UBound(bendsArray)
            swFeature = bendsArray(i)
            Debug.Print("Name of bend feature" & (i + 1) & " of the fold feature: " & swFeature.Name)
        Next i

        'Release selection access
        swFoldsFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
