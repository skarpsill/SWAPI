---
title: "Get Properties of Sketch Pattern Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Properties_of_Sketch-Pattern_Feature_Example_VBNET.htm"
---

# Get Properties of Sketch Pattern Feature Example (VB.NET)

This example shows how to get the properties of a sketch pattern feature.

```vb
  '----------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified document exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates Boss-Extrude2, Sketch3, and Sketch-Pattern1.
 ' 2. Inspect the Immediate window.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  '----------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim myFeature As Feature
     Dim swSketchPatt As SketchPatternFeatureData
     Dim vBasePt As Object
     Dim skPoint As Object
     Dim vSkLines As Object
     Dim swSketch As Sketch
     Dim swSketchFeat As Feature
     Dim swPatternTransform As MathTransform
     Dim boolstatus As Boolean
     Dim i As Integer
     Dim longstatus As Integer
     Dim longwarnings As Integer

     Sub main()

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
         swApp.ActivateDoc2("block20", False, longstatus)

         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0407921768468213, 0.0396239999998329, -0.0402814031592129, False, 0, Nothing, 0)
         boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
         boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
         vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0518589252521906, 0.0451811131877662, 0, -0.0357471289475484, 0.0286242963995278, 0)
         Part.SketchManager.InsertSketch(True)

         boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
         myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)

         Part.SketchManager.InsertSketch(True)
         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.00770328176440671, 0.0396239999998897, -0.00762437790422155, False, 0, Nothing, 0)
         skPoint = Part.SketchManager.CreatePoint(-0.00527, 0.051345, 0.0#)
         skPoint = Part.SketchManager.CreatePoint(-0.005854, 0.025783, 0.0#)
         skPoint = Part.SketchManager.CreatePoint(-0.005888, -0.000009, 0.0#)
         skPoint = Part.SketchManager.CreatePoint(0.019408, 0.051285, 0.0#)
         skPoint = Part.SketchManager.CreatePoint(0.019093, 0.024628, 0.0#)
         skPoint = Part.SketchManager.CreatePoint(0.019629, -0.000148, 0.0#)
         skPoint = Part.SketchManager.CreatePoint(0.043756, 0.051962, 0.0#)
         skPoint = Part.SketchManager.CreatePoint(0.043146, 0.025865, 0.0#)
         skPoint = Part.SketchManager.CreatePoint(0.043401, 0.000225, 0.0#)
         Part.ClearSelection2(True)
         Part.SketchManager.InsertSketch(True)

         boolstatus = Part.Extension.SelectByID2("Boss-Extrude2", "BODYFEATURE", -0.0477922378944982, 0.0421639999998433, 0.0233214950450815, False, 4, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Sketch3", "SKETCH", 0, 0, 0, True, 64, Nothing, 0)

         swSketchPatt = Part.FeatureManager.CreateDefinition(swFeatureNameID_e.swFmSketchPattern)
         swSketchPatt.GeometryPattern = False
         swSketchPatt.UseCentroid = True
         swSketchFeat = Part.FeatureManager.CreateFeature(swSketchPatt)
         swSketchPatt = swSketchFeat.GetDefinition

         swSketchPatt.AccessSelections(Part, Nothing)

         swSketch = swSketchPatt.Sketch
         i = swSketch.GetSketchPointsCount2

         swPatternTransform = swSketchPatt.GetTransform(i)

         vBasePt = swSketchPatt.GetBasePoint

         Debug.Print(swSketchFeat.Name)
         Debug.Print("  Create pattern using only geometry? " & swSketchPatt.GeometryPattern)
         Debug.Print("  Pattern seed coordinates in mm:  (" & vBasePt(0) * 1000.0# & ", " & vBasePt(1) * 1000.0# & ", " & vBasePt(2) * 1000.0# & ")")
         Debug.Print("  Body count: " & swSketchPatt.GetPatternBodyCount)
         Debug.Print("  Face count: " & swSketchPatt.GetPatternFaceCount)
         Debug.Print("  Feature count: " & swSketchPatt.GetPatternFeatureCount)
         Debug.Print("  Reference point type (-1 for centroid): " & swSketchPatt.GetReferencePointType)
         Debug.Print("  Use centroid as the reference point? " & swSketchPatt.UseCentroid)
         Debug.Print("  Propagate visual properties? " & swSketchPatt.PropagateVisualProperty)

         swSketchPatt.ReleaseSelectionAccess()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
