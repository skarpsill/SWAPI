---
title: "Create Projection Split Line Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Projection_Split_Line_Example_VBNET.htm"
---

# Create Projection Split Line Feature Example (VB.NET)

This example shows how to create a projection split line feature.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Verify that the specified document template exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
  ' 1. Creates a new model document with a feature extrusion, reference plane,
 '    and sketch of an ellipse.
 ' 2. Creates Split Line1 in the FeatureManager design tree.
 ' 3. Inspect the Immediate window.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim skSegment As SketchSegment
     Dim myRefPlane As RefPlane
     Dim swSelMgr As SelectionMgr
     Dim swSplitLine As SplitLineFeatureData
     Dim vSkLines As Object
     Dim myFeature As Feature
     Dim boolstatus As Boolean
     Dim longstatus As Integer

     Sub main()

         Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
         Part = swApp.ActiveDoc

         skSegment = Part.SketchManager.CreateEllipse(-0.0212512457655407, 0.0122505076014363, 0, 0.00277468345541365, 0.00705202391259263, 0, -0.0196159170237913, 0.0198085370103935, 0)
         Part.ClearSelection2(True)
         Part.SketchManager.InsertSketch(True)

         boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)

         myRefPlane = Part.FeatureManager.InsertRefPlane(8, 0.01778, 0, 0, 0, 0)
         Part.ClearSelection2(True)

         Part.SketchManager.InsertSketch(True)
         boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", -0.0407148636658249, 0.0247341229458697, 0.0194913387248102, False, 0, Nothing, 0)
         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
         boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)

         vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0625406077424486, 0.0297244912047745, 0, 0.0584903577919818, -0.018090206988802, 0)
         Part.ClearSelection2(True)
         Part.SketchManager.InsertSketch(True)
         Part.ClearSelection2(True)
         boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)

         myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.00254, 0.00254, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, 0, 0, False)
         Part.SelectionManager.EnableContourSelection = False

         boolstatus = Part.Extension.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", -0.0143044793836914, 0.00334438727079956, 0, True, 4, Nothing, 0)
         boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0181817275523031, 0.0132444059746035, 0.0177800000000161, True, 1, Nothing, 0)

         Part.InsertSplitLineProject(True, True)

         swSelMgr = Part.SelectionManager

         boolstatus = Part.Extension.SelectByID2("Split Line1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)

         myFeature = swSelMgr.GetSelectedObject6(1, -1)
         swSplitLine = myFeature.GetDefinition

         ' Get split line feature data
         boolstatus = swSplitLine.AccessSelections(Part, Nothing)

         Debug.Print(myFeature.Name)
         Debug.Print("    Split type as defined in swSplitLineFeatureType_e: " & swSplitLine.GetType)
         Debug.Print("    Single Direction? " & swSplitLine.SingleDirection)
         Debug.Print("    Reversed? " & swSplitLine.ReverseDirection)

         swSplitLine.ReleaseSelectionAccess()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
