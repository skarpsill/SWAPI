---
title: "Get Selections for Reference Axis Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selections_for_Reference_Axis_Feature_Example_VBNET.htm"
---

# Get Selections for Reference Axis Feature Example (VB.NET)

This example shows how to get the selections for a reference axis feature.

```
'-------------------------------------------------
' Preconditions:
' 1. Verify that the document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified document.
' 2. Gets the Axis1 feature.
' 3. Gets the entities that define Axis1.
' 4. Gets the type and name of the entities that define
'    Axis1.
' 5. Examine the Immediate window.
'-------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swPart As PartDoc
        Dim swFeat As Feature
        Dim swRefAxisFeatureData As RefAxisFeatureData
        Dim swEntity As Entity
        Dim warnings As Integer
        Dim errors As Integer
        Dim fileName As String
        Dim obj() As Object = Nothing
        Dim types() As Integer = Nothing
        Dim aType As String
        Dim name As String
        Dim i As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\button.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swPart = swModel

        swFeat = swPart.FeatureByName("Axis1")
        swRefAxisFeatureData = swFeat.GetDefinition
        swRefAxisFeatureData.AccessSelections(swModel, Nothing)
        obj = swRefAxisFeatureData.GetSelections(types)
        swRefAxisFeatureData.ReleaseSelectionAccess()

        Debug.Print("Entity:")
        Debug.Print("")
        For i = 0 To UBound(obj)
            swEntity = obj(i)
            swFeat = swEntity
            swEntity.Select(False)
            name = swFeat.GetNameForSelection(aType)
            Debug.Print("  Type: " & types(i))
            Debug.Print("  Name: " & name)
            Debug.Print("")
        Next i

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
