---
title: "Get Areas of MidSurface Faces Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Areas_of_MidSurface_Faces_Example_VB.htm"
---

# Get Areas of MidSurface Faces Example (VBA)

This example shows how to get the areas of mid-surface faces.

```
'-----------------------------------------------------------
' Postconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects two faces and inserts a midsurface feature.
' 3. Gets the number of faces in the midsurface feature.
' 4. Gets the areas of the faces in the midsurface feature.
' 5. Examine the Immediate window, FeatureManager design
'    tree, and graphics area.
'
' NOTE: Because the part used elsewhere, do not save changes.
'------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swMidSurfaceFeature As SldWorks.MidSurface3
Dim swFeature As SldWorks.Feature
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFace As SldWorks.Face2
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim count As Long
Dim faces As Variant
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", -5.33080255641494E-02, 2.99999999999727E-02, 1.31069871973182E-02, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -3.70905424398416E-02, 0, 2.89438729892595E-02, True, 0, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
    swFeatureManager.InsertMidSurface Nothing, Nothing, 0#, False
    status = swModelDocExt.SelectByID2("Surface-MidSurface1", "REFSURFACE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swMidSurfaceFeature = swFeature.GetSpecificFeature2
    count = swMidSurfaceFeature.GetFaceCount
    Debug.Print "Number of faces for midsurface feature: " & count
    faces = swMidSurfaceFeature.GetFaces
    For i = LBound(faces) To UBound(faces)
        Set swFace = faces(i)
        Debug.Print "Area of face " & i & " of midsurface feature: " & swFace.GetArea
    Next i
```

```
End Sub
```
