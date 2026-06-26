---
title: "Get Rib Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Rib_Feature_Data_Example_VBNET.htm"
---

# Get Rib Feature Data Example (VB.NET)

This example shows how to get rib feature data.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Verify that the specified model document exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the part document.
 ' 2. Creates Shell1, Plane1, and Rib1.
 ' 3. Inspect the FeatureManager design tree, the graphics area, and the
 '    Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
  '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim myRefPlane As RefPlane
     Dim skSegment As SketchSegment
     Dim swSelMgr As SelectionMgr
     Dim swFeat As Feature
     Dim swRibFeat As RibFeatureData2
     Dim boolstatus As Boolean
     Dim longstatus As Integer, longwarnings As Integer

     Sub main()

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
         swApp.ActivateDoc2("block20", False, longstatus)
         Part = swApp.ActiveDoc

         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.00878816842651986, 0.0396239999998897, -0.0292468281514857, False, 1, Nothing, 0)
         Part.InsertFeatureShell(0.00254, False)

         boolstatus = Part.Extension.SelectByID2("", "FACE", 0.00264031138414111, 0.028407059059532, -0.0613970439424634, True, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.059937899786064, 0.0277866864457792, -0.00877977980189826, True, 1, Nothing, 0)

         myRefPlane = Part.FeatureManager.InsertRefPlane(128, 0, 128, 0, 0, 0)
         Part.ClearSelection2(True)

         boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", 0.00664896553058725, 0.109417877974863, 0.0524178648701081, False, 0, Nothing, 0)
         Part.SketchManager.InsertSketch(True)

         skSegment = Part.SketchManager.CreateLine(-0.085797, 0.021082, 0.0#, -0.03423, 0.035134, 0.0#)
         skSegment = Part.SketchManager.CreateLine(-0.03423, 0.035134, 0.0#, 0.007726, 0.025357, 0.0#)
         skSegment = Part.SketchManager.CreateLine(0.007726, 0.025357, 0.0#, 0.111514, 0.039624, 0.0#)
         Part.ClearSelection2(True)

         Part.SketchManager.InsertSketch(True)
         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
         Part.FeatureManager.InsertRib(True, False, 0.00254, 0, False, False, True, 0.0174532925199433, False, False)

         swSelMgr = Part.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swRibFeat = swFeat.GetDefinition

         Debug.Print("Rib feature type as defined in swRibType_e: " & swRibFeat.Type)
         Debug.Print("Thickness: " & swRibFeat.Thickness)
         Debug.Print("Extrusion direction as defined in swRibExtrusionDirection_e: " & swRibFeat.ExtrusionDirection)
         Debug.Print("Rib has a draft? " & swRibFeat.EnableDraft)
         If swRibFeat.EnableDraft Then
             Debug.Print("    Draft angle: " & swRibFeat.DraftAngle)
             Debug.Print("    Draft outward? " & swRibFeat.DraftOutward)
         End If
         Debug.Print("Add material to reverse side of the rib? " & swRibFeat.FlipSide)
         Debug.Print("Rib is extruded on two sides of the midplane? " & swRibFeat.IsTwoSided)
         If Not swRibFeat.IsTwoSided Then
             Debug.Print("Single-sided rib is extruded on the reverse side? " & swRibFeat.ReverseThicknessDir)
         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
