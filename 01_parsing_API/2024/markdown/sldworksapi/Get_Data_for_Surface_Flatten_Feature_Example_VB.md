---
title: "Get Data for Surface-flatten Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Data_for_Surface_Flatten_Feature_Example_VB.htm"
---

# Get Data for Surface-flatten Feature Example (VBA)

This example shows how to insert a surface-flatten feature and get its data.

```
'-------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Inserts a surface-flatten feature.
' 3. Gets surface-flatten feature data.
' 4. Examine the graphics area and FeatureManager design
'    tree.
'
' NOTE: Because this part is used elsewhere, do not save
' changes.
'--------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swSurfaceFlattenFeatureData As SldWorks.SurfaceFlattenFeatureData
Dim swEdge As SldWorks.Edge
Dim status As Boolean
Dim warnings As Long
Dim errors As Long
Dim fileName As String
Dim edges As Variant
Dim nbrTearEdges As Long
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\Hemisphere.SLDPRT"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    ' Select face, point, and curves for surface-flatten feature
    status = swModelDocExt.SelectByID2("", "FACE", 5.46207138008786E-03, -3.73996629648742E-02, 1.30049636270216E-02, False, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "VERTEX", 0, -4.00014251170795E-02, -5.4185036618795E-04, True, 16, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 0.011047389592717, -6.23453597697887E-06, 3.82739927527045E-02, True, 8, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 1.08290857690036E-02, -2.62767618508641E-02, 2.80128973987478E-02, True, 8, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 9.07918330954303E-03, 2.86363967873063E-02, 2.62553195430037E-02, True, 8, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 1.57595492108076E-02, 2.40950142317162E-02, -2.72880335909787E-02, True, 8, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 1.43808110794609E-02, -2.81074423709366E-02, -2.40578702886196E-02, True, 8, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 0.01886657492451, 2.48139106812095E-05, -0.035004838468241, True, 8, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 1.40143161426676E-02, -3.74399859522778E-02, 1.23652313243445E-04, True, 8, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 1.64192327552536E-02, 3.63245554251959E-02, -9.58561062339106E-05, True, 8, Nothing, 0)
```

```
    ' Create surface-flatten feature
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.InsertFlattenSurface2(8, True)
```

```
    ' Get surface-flatten feature data
    Set swSurfaceFlattenFeatureData = swFeature.GetDefinition
    swSurfaceFlattenFeatureData.AccessSelections swModel, Nothing
    Debug.Print "Feature = " & swFeature.Name
    Debug.Print "   Accuracy of flattened triangle mesh =  " & swSurfaceFlattenFeatureData.AccuracyFactor
    Debug.Print "   Keep internal control curves? " & swSurfaceFlattenFeatureData.KeepInternalControlCurves
    If swSurfaceFlattenFeatureData.ShouldMakeTears = True Then
        Debug.Print "   Tear edges: "
        edges = swSurfaceFlattenFeatureData.TearEdges
        nbrTearEdges = UBound(edges) + 1
        Debug.Print "      Number of tear edges: " & nbrTearEdges
        For i = 0 To UBound(edges)
            Set swEdge = edges(i)
            Dim swSelMgr As SldWorks.SelectionMgr
            Set swSelMgr = swModel.SelectionManager
            status = swSelMgr.AddSelectionListObject(swEdge, Nothing)
            Debug.Print "            Type of object (51 = swSelREFEDGES): " & swSelMgr.GetSelectedObjectType3(1, -1)
        Next i
    End If
    swSurfaceFlattenFeatureData.ReleaseSelectionAccess
```

```
End Sub
```
