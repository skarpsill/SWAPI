---
title: "Get Selections for Reference Axis Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selections_for_Reference_Axis_Feature_Example_VB.htm"
---

# Get Selections for Reference Axis Feature Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swPart As SldWorks.PartDoc
Dim swFeat As SldWorks.Feature
Dim swRefAxisFeatureData As SldWorks.RefAxisFeatureData
Dim swEntity As SldWorks.Entity
Dim warnings As Long
Dim errors As Long
Dim fileName As String
Dim obj As Variant
Dim types As Variant
Dim aType As String
Dim name As String
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\button.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swPart = swModel
```

```
    Set swFeat = swPart.FeatureByName("Axis1")
    Set swRefAxisFeatureData = swFeat.GetDefinition
    swRefAxisFeatureData.AccessSelections swModel, Nothing
    obj = swRefAxisFeatureData.GetSelections(types)
    swRefAxisFeatureData.ReleaseSelectionAccess
```

```
    Debug.Print "Entity:"
    Debug.Print ""
    For i = 0 To UBound(obj)
        Set swEntity = obj(i)
        Set swFeat = swEntity
        swEntity.Select False
        name = swFeat.GetNameForSelection(aType)
        Debug.Print "  Type: " & types(i)
        Debug.Print "  Name: " & name
        Debug.Print ""
    Next i
```

```
End Sub
```
