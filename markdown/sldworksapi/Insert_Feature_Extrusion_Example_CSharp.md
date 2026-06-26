---
title: "Create Extrusion Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Feature_Extrusion_Example_CSharp.htm"
---

# Create Extrusion Feature Example (C#)

This example shows how to create an extrusion feature.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Verify that the specified part template exists.
 //
 // Postconditions:
 // 1. Creates a Boss-Extrude1 feature.
 // 2. Examine the FeatureManager design tree and graphics area.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace CreateExtrusionFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         Feature myFeature;
         ModelDoc2 Part;
         RefPlane myRefPlane;

         bool boolstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  true, 0,  null, 0);
             myRefPlane = (RefPlane)Part.FeatureManager.InsertRefPlane(8, 0.01, 0, 0, 0, 0);
             boolstatus = Part.Extension.SelectByID2("Front Plane",  "PLANE", 0, 0, 0,  true, 0,  null, 0);
             myRefPlane = (RefPlane)Part.FeatureManager.InsertRefPlane(8, 0.02, 0, 0, 0, 0);

             boolstatus = Part.Extension.SelectByID2("Plane2", "PLANE", 0, 0, 0, false, 0, null, 0);
             object vSkLines = null;
             vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0250462141853123, 0.0157487558892494, 0, 0.0275128867944718, -0.015559011842391, 0);

             Part.SketchManager.InsertSketch(true);

             // Sketch to extrude
             boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
             // Start condition reference
             boolstatus = Part.Extension.SelectByID2("Plane2", "PLANE", 0.00105020593408751, -0.00195369982668282, 0.0248175428318827,  true, 32,  null, 0);
             // End condition reference
             boolstatus = Part.Extension.SelectByID2("Plane1", "PLANE", 0.0068370744701368, -0.004419862088339, 0.018892268568016,  true, 1,  null, 0);

             // Boss extrusion start condition reference is Plane2, and the extrusion end is offset 3 mm from the end condition reference, Plane1
             myFeature = (Feature)Part.FeatureManager.FeatureExtrusion3(true, false, true, (int)swEndConditions_e.swEndCondOffsetFromSurface, 0, 0.003, 0.003, false, false, false,
             false, 0.0174532925199433, 0.0174532925199433,  false,  false,  false,  false, true, true, true,
             (int)swStartConditions_e.swStartSurface, 0, false);

         }

         public SldWorks swApp;

     }
 }
```
