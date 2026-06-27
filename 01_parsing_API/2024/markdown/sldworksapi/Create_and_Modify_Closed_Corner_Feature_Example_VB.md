---
title: "Create and Modify Closed Corner Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Closed_Corner_Feature_Example_VB.htm"
---

# Create and Modify Closed Corner Feature Example (VBA)

This example shows how to create and modify a closed corner feature in a sheet metal part.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified sheet metal part document to
'    open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified sheet metal part document.
' 2. Selects two faces.
' 3. Inserts a closed corner feature.
' 4. Modifies properties of the closed corner feature.
' 5. Examine the graphics area and Immediate window.
'
' NOTE: Because this part document is used elsewhere,
' do not save changes.
'--------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeature As SldWorks.Feature
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swClosedCornerFeatureData As SldWorks.ClosedCornerFeatureData
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim faces As Variant
Dim swFace As SldWorks.Face2
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\sheetmetal\formtools\cover.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swSelectionMgr = swModel.SelectionManager
```

```
    'Select the faces for the closed corner feature
    status = swModelDocExt.SelectByID2("", "FACE", 1.10595835492404E-02, 2.80018934407167E-02, 4.97348782814129E-02, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 1.81424245698736E-02, 1.10595835492404E-02, 4.95671179450028E-02, True, 1073741824, Nothing, 0)
```

```
    'Insert the closed corner feature
    swModel.InsertSheetMetalClosedCorner
```

```
    'Select the closed corner feature
    status = swModelDocExt.SelectByID2("Closed Corner1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swClosedCornerFeatureData = swFeature.GetDefinition
```

```
    'Access closed corner feature
    status = swClosedCornerFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print ("Original properties: ")
        Debug.Print ("  Corner type: " & swClosedCornerFeatureData.CornerType)
        Debug.Print ("  Gap distance: " & swClosedCornerFeatureData.GapDistance)
        Debug.Print ("  Open bend region? " & swClosedCornerFeatureData.OpenBendRegion)
        Debug.Print ("  Overlap/underlap ratio: " & swClosedCornerFeatureData.OverlapUnderlapRatio)
        faces = swClosedCornerFeatureData.faces
        For i = 0 To UBound(faces)
            Set swFace = faces(i)
            Debug.Print ("  Area of face " & i & ": " & swFace.GetArea * 1000 & " mm")
        Next i
```

```
        Debug.Print ("Modified properties: ")
        swClosedCornerFeatureData.CornerType = swClosedCornerTypes_e.swClosedCornerTypeUnderlap
        swClosedCornerFeatureData.GapDistance = 0.005
        swClosedCornerFeatureData.OpenBendRegion = True
        swClosedCornerFeatureData.OverlapUnderlapRatio = 0.5
        Debug.Print ("  Corner type: " & swClosedCornerFeatureData.CornerType)
        Debug.Print ("  Gap distance: " & swClosedCornerFeatureData.GapDistance)
        Debug.Print ("  Open bend region? " & swClosedCornerFeatureData.OpenBendRegion)
        Debug.Print ("  Overlap/underlap ratio: " & swClosedCornerFeatureData.OverlapUnderlapRatio)
```

```
        status = swFeature.ModifyDefinition(swClosedCornerFeatureData, swModel, Nothing)
```

```
End Sub
```
