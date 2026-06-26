---
title: "Create Extrusion Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Feature_Extrusion_Example_VBNET.htm"
---

# Create Extrusion Feature Example (VB.NET)

This example shows how to create an extrusion feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Verify that the specified part template exists.
 '
 ' Postconditions:
 ' 1. Creates a Boss-Extrude1 feature.
 ' 2. Examine the FeatureManager design tree and graphics area.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim myFeature As Feature
     Dim Part As ModelDoc2
     Dim myRefPlane As RefPlane
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
         Part = swApp.ActiveDoc

         boolstatus = Part.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  True, 0,  Nothing, 0)
         myRefPlane = Part.FeatureManager.InsertRefPlane(8, 0.01, 0, 0, 0, 0)
         boolstatus = Part.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  True, 0,  Nothing, 0)
         myRefPlane = Part.FeatureManager.InsertRefPlane(8, 0.02, 0, 0, 0, 0)

         boolstatus = Part.Extension.SelectByID2("Plane2", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
         Dim vSkLines As Object
         vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0250462141853123, 0.0157487558892494, 0, 0.0275128867944718, -0.015559011842391, 0)

         Part.SketchManager.InsertSketch(True)

         ' Sketch to extrude
         boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
         ' Start condition reference
         boolstatus = Part.Extension.SelectByID2("Plane2", "PLANE", 0.00105020593408751, -0.00195369982668282, 0.0248175428318827,  True, 32,  Nothing, 0)
         ' End condition reference
         boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", 0.0068370744701368, -0.004419862088339, 0.018892268568016,  True, 1,  Nothing, 0)

         ' Boss extrusion start condition reference is Plane2, and the extrusion end is offset 3 mm from the end condition reference, Plane1
         myFeature = Part.FeatureManager.FeatureExtrusion3(True, False, True, swEndConditions_e.swEndCondOffsetFromSurface, 0, 0.003, 0.003,  False,  False,  False,  False, 0.0174532925199433, 0.0174532925199433,  False,  False,  False,  False, True, True, True, swStartConditions_e.swStartSurface, 0, False)

     End Sub

     Public swApp As SldWorks

 End  Class
```
