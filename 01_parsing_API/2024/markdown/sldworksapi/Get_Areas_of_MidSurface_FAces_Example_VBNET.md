---
title: "Get Areas of MidSurface Faces Example(VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Areas_of_MidSurface_FAces_Example_VBNET.htm"
---

# Get Areas of MidSurface Faces Example(VB.NET)

## Get Areas of MidSurface Faces Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swMidSurfaceFeature As MidSurface3
        Dim swFeature As Feature
        Dim swSelectionMgr As SelectionMgr
        Dim swFace As Face2
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String
        Dim count As Integer
        Dim faces() As Object
        Dim i As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", -0.0533080255641494, 0.0299999999999727, 0.0131069871973182, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0370905424398416, 0, 0.0289438729892595, True, 0, Nothing, 0)
        swFeatureManager = swModel.FeatureManager
        swFeatureManager.InsertMidSurface(Nothing, Nothing, 0.0#, False)
        status = swModelDocExt.SelectByID2("Surface-MidSurface1", "REFSURFACE", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swMidSurfaceFeature = swFeature.GetSpecificFeature2
        count = swMidSurfaceFeature.GetFaceCount
        Debug.Print("Number of faces for midsurface feature: " & count)
        faces = swMidSurfaceFeature.GetFaces
        For i = LBound(faces) To UBound(faces)
            swFace = faces(i)
            Debug.Print("Area of face " & i & " of midsurface feature: " & swFace.GetArea)
        Next i

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
