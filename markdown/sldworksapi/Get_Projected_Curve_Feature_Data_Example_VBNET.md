---
title: "Get Projected Curve Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Projected_Curve_Feature_Data_Example_VBNET.htm"
---

# Get Projected Curve Feature Data Example (VB.NET)

This example shows how to get data for a projected curve feature.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the part document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects a face and sketches a spline on that face.
' 3. Selects the sketch of the spline and a face.
' 4. Inserts a projected curve feature.
' 5. Gets some projected curve feature data and prints it
'    to the Immediate window.
' 6. Examine the Immediate window, FeatureManager design tree, and
'    the graphics area.
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
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swFeature As Feature
        Dim swSelectionManager As SelectionMgr
        Dim swProjectionCurveFeatureData As ProjectionCurveFeatureData
        Dim swSketch As Sketch
        Dim pointArray As Object
        Dim points(10) As Double
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        'Open part document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Sketch a spline on the selected face
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("", "FACE", -0.0499223104334874, 0.0396239999998897, 0.00738137362270663, False, 0, Nothing, 0)
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)
        points(0) = -0.0624778997860176
        points(1) = 0.00729572078180673
        points(2) = 0
        points(3) = -0.0364588790258153
        points(4) = 0.0324586288177215
        points(5) = 0
        points(6) = 0.0104252377344665
        points(7) = 0.0140473535914225
        points(8) = 0
        points(9) = 0.0646002912861796
        points(10) = 0.0100590221094308
        pointArray = points
        swSketchSegment = swSketchManager.CreateSpline2((pointArray), False)
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)

        'Insert projected curve
        status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0497146993259321, 0, -0.0256283866693252, True, 0, Nothing, 0)
        swFeature = swModel.InsertProjectedSketch2(1)

        'Get projected curve data
        status = swModelDocExt.SelectByID2("Curve1", "REFCURVE", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionManager = swModel.SelectionManager
        swFeature = swSelectionManager.GetSelectedObject6(1, -1)
        swProjectionCurveFeatureData = swFeature.GetDefinition
        swProjectionCurveFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Is reversed = " & swProjectionCurveFeatureData.Reverse)
        Debug.Print("Number of targeted faces = " & swProjectionCurveFeatureData.GetFaceArrayCount)
        swFeature = swProjectionCurveFeatureData.Sketch
        swSketch = swFeature.GetSpecificFeature2
        Debug.Print("Name of sketch = " & swFeature.Name)
        swProjectionCurveFeatureData.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
