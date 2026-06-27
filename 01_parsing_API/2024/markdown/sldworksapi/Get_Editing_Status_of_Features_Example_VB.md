---
title: "Get Editing Status of Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Editing_Status_of_Features_Example_VB.htm"
---

# Get Editing Status of Features Example (VBA)

This example shows how to get the editing status of one or more features.

```
'------------------------------------------------------------------------
' Preconditions
' 1. Open public_documents\samples\tutorial\introtosw\pressure_plate.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. At Stop, examine the the Immediate window, graphics area, and
'    FeatureManager design tree.
' 2. Press F5.
' 3. Examine the Immediate window again.
'
' NOTE: Because this document is used elsewhere, do not save changes.
'-------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeatMgr As SldWorks.FeatureManager
Dim swSelMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim varFeat  As Variant
Dim editStatus As Long
Dim retVal As Boolean
Dim i As Long
Dim featName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swFeatMgr = swModel.FeatureManager
    Set swSelMgr = swModel.SelectionManager
    Set swModelDocExt = swModel.Extension
```

```
    ' Traverse through the FeatureManager design tree
    ' to get the editing status of all features
    ' Change the editing status of a sketch and feature
    ' during feature traversal
    varFeat = swFeatMgr.GetFeatures(True)
    editStatus = swFeature_NonEditable
    For i = LBound(varFeat) To UBound(varFeat)
        Dim swFeat As SldWorks.Feature
        Set swFeat = varFeat(i)
        featName = swFeat.Name
        Select Case (featName)
            Case "Sketch2"
                ' Select and edit a sketch
                retVal = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
                swModel.EditSketch
```

```
                Stop
                ' Examine the Immediate window, graphics area, and FeatureManager design tree
                ' All of the features beneath Extrude1 cannot be edited because
                ' Extrude2's Sketch2 is in edit mode
                ' Press F5
```

```
            Case "Extrude3"
                ' Close the open sketch
                swModel.InsertSketch2 True
            Case "Cut-Extrude2"
                ' Select and edit a feature
                retVal = swModelDocExt.SelectByID2("Cut-Extrude2", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
                swModel.FeatEdit
        End Select
```

```
        ' Get the editing status of the current feature
        editStatus = swFeat.GetEditStatus
        Select Case (editStatus)
            Case 0
                Debug.Print (swFeat.Name & " can be edited.")
            Case 1
                Debug.Print (swFeat.Name & " cannot currently be edited.")
            Case 2
                Debug.Print (swFeat.Name & " is already being edited.")
        End Select
```

```
        Set swFeat = Nothing
```

```
    Next i
```

```
    ' End feature editing
    swModel.InsertSketch2 True
```

```
End Sub
```
