---
title: "Rotate Model Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Model_Example_CSharp.htm"
---

# Rotate Model Example (C#)

This example shows how to rotate a model in the graphics area.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template exists.
// 2. Watch the graphics while the macro runs.
//
// Postconditions:
// 1. Creates a new part document.
// 2. Inserts and extrudes a rectangular sketch.
// 3. Rotates the sketch multiple times.
//---------------------------------------------------------------------------
using Microsoft.VisualBasic;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
namespace RotateModel_CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 Part;
        Feature myFeature;
        object vSkLines;
        bool boolstatus;

        public void Main()
        {
            Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            boolstatus = Part.Extension.SelectByID2("Top Plane", "PLANE", -0.0567254111166863, 	0.00753958008310182, 0.0248109468921342, false, 0, null, 0);
            Part.SketchManager.InsertSketch(true);
            vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0493169981371904, 0.0173783707721528, 0, 0.0558925978888158, -0.0455595125648331, 0);
            Part.ShowNamedView2("*Trimetric", 8);
            boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            myFeature = Part.FeatureManager.FeatureExtrusion2(true, false, false, 0, 0, 0.016256, 0.00254, false, false, false, false, 0.0174532925199433, 0.0174532925199433, false, false, false, false, true, true, true, 0, 0, false);
            ((SelectionMgr)(Part.SelectionManager)).EnableContourSelection = false;

            Part.ViewRotate();
            Part.ViewRotateminusx();
            Part.ViewRotateminusy();
            Part.ViewRotateminusz();
            Part.ViewRotateplusx();
            Part.ViewRotateplusy();
            Part.ViewRotateplusz();
            Part.ViewRotXMinusNinety();
            Part.ViewRotXPlusNinety();
            Part.ViewRotYMinusNinety();
            Part.ViewRotYPlusNinety();
        }

        public SldWorks swApp;
    }
}
```
