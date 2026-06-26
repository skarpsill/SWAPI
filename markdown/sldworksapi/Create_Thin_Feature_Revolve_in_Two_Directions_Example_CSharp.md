---
title: "Create Thin Feature Revolve in Two Directions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Thin_Feature_Revolve_in_Two_Directions_Example_CSharp.htm"
---

# Create Thin Feature Revolve in Two Directions Example (C#)

This example shows how to create a thin feature revolve in two directions.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\Multiple Planar_Faces2.sldprt.
 //
 // Postconditions:
 // 1. Creates a thin feature revolve in two directions.
 // 2. Examine the graphics area and FeatureManager design tree.
 //
 // NOTE: Because the model is used elsewhere, do not save changes
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 namespace ThinFeatureRevolve_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void main()
         {
             ModelDoc2 Part = default(ModelDoc2);
             bool boolstatus = false;

             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, true, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("Axis1", "AXIS", -0.03249248386774, -0.008890295497245, -0.005457395402805,  true, 16,  null, 0);
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.03948753408952, 0.1016773485926, -0.08343298757264,  true, 32,  null, 0);

             Feature myFeature = default(Feature);
             myFeature = Part.FeatureManager.FeatureRevolve2(false, true, true, false, false, true, 4, 5, 6.28318530718, 0,
             false, true, 0.01, 0.01, 0, 0.002, 0.01, true, true, true);

         }

         public SldWorks swApp;
     }
 }
```
