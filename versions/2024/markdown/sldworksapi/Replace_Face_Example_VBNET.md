---
title: "Create Replace Face Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Face_Example_VBNET.htm"
---

# Create Replace Face Feature Example (VB.NET)

This example shows how to create a Replace Face feature.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified model document exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified part.
  ' 2. Creates Plane1, Surface-Extrude1, and Replace Face1.
 ' 3. Inspect the FeatureManager design tree, the graphics area, and the
 '    Immediate window.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim selMgr As SelectionMgr
     Dim Part As ModelDoc2
     Dim feat As Feature
     Dim featData As ReplaceFaceFeatureData
     Dim boolstatus As Boolean
     Dim longstatus As Integer, longwarnings As Integer

     Sub main()

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", longstatus, longwarnings)
         swApp.ActivateDoc2("block20", False, longstatus)
         Part = swApp.ActiveDoc

         boolstatus = Part.Extension.SelectByID2("", "FACE", 0.00687152192142548, 0.0256655537640995, 0.049345602378537, True, 0, Nothing, 0)
         Dim myRefPlane As RefPlane
         myRefPlane = Part.FeatureManager.InsertRefPlane(264, 0.05842, 0, 0, 0, 0)
         Part.ClearSelection2(True)

         Dim pointArray As Object
         Dim points(0 To 14) As Double
         points(0) = -0.0700496017443584
         points(1) = 0.0582762055241233
         points(2) = 0
         points(3) = -0.0357558994484748
         points(4) = 0.0853945497913173
         points(5) = 0
         points(6) = -0.00588719099721402
         points(7) = 0.0671372129016845
         points(8) = 0
         points(9) = 0.0273002628375139
         points(10) = 0.0878577815467452
         points(11) = 0
         points(12) = 0.0737626982062238
         points(13) = 0.0582762055241233
         points(14) = 0
         pointArray = points
         Dim skSegment As SketchSegment
         skSegment = Part.SketchManager.CreateSpline((pointArray))
         Part.SketchManager.InsertSketch(True)
         boolstatus = Part.Extension.SelectByID2("Spline1@Sketch2", "EXTSKETCHSEGMENT", -0.0549544681183813, 0.0875052976097064, 0, False, 0, Nothing, 0)
         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
         Part.SelectionManager.EnableContourSelection = True
         boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCHCONTOUR", 0, 0, 0, True, 4, Nothing, 0)
         Part.FeatureExtruRefSurface2(True, False, False, 0, 0, 0.14478, 0.14478, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False)
         Part.SelectionManager.EnableContourSelection = False
         boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0585444908073214, 0.0396239999998329, -0.0518899759430838, True, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Surface-Extrude1", "SURFACEBODY", -0.0189730427370591, 0.0726880897401543, 0.115671174990496, True, 0, Nothing, 0)
         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Surface-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0585444908073214, 0.0396239999998329, -0.0518899759430838, True, 1, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Surface-Extrude1", "SURFACEBODY", -0.0189730427370591, 0.0726880897401543, 0.115671174990496, True, 2, Nothing, 0)
         Part.InsertFeatureReplaceFace()
         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0362064915135534, 0.0856902732399476, 0.127037337239983, False, 0, Nothing, 0)
         Part.FeatureManager.HideBodies()
         boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", -0.0693294107213475, 0.0872697709380442, -0.0300713252946179, False, 0, Nothing, 0)
         Part.BlankRefGeom()

         boolstatus = Part.Extension.SelectByID2("Replace Face1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         selMgr = Part.SelectionManager
         feat = selMgr.GetSelectedObject6(1, -1)
         featData = feat.GetDefinition

         featData.AccessSelections(Part, Nothing)

         Dim vFacesToReplace As Object
         vFacesToReplace = featData.FacesForReplacement
         Debug.Print(featData.GetFacesForReplacementCount & " face replaced in " & vFacesToReplace(0).GetFeature.Name)
         Debug.Print(featData.GetReplacementSurfacesCount & " replacement surface ")

         featData.ReleaseSelectionAccess()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
