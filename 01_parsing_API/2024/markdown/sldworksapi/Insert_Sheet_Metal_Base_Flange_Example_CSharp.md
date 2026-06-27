---
title: "Insert Sheet Metal Base Flange Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sheet_Metal_Base_Flange_Example_CSharp.htm"
---

# Insert Sheet Metal Base Flange Example (C#)

This example shows how to insert a sheet metal base flange.

```
//---------------------------------------------------------------------------------
// Preconditions: Verify that the specified part template exists.
//
// Postconditions:
// 1. Creates two boss extrudes and converts them to sheet metal parts.
// 2. Inserts a sheet metal base flange that connects the two sheet metal parts.
// 3. Examine the graphics area and FeatureManager design tree.
//---------------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 Part;
        bool boolstatus;
        long longstatus;
        int status;

        public void Main()
        {
            longstatus = (long)swApp.ResetUntitledCount(0, 0, 0);
            Part = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\Part.prtdot", 0, 0, 0);
            swApp.ActivateDoc2("Part1", false, ref status);
            Part = (ModelDoc2)swApp.ActiveDoc;

            Part.SketchManager.InsertSketch(true);
            boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.07320616684915, 0.04378582530511, 0.008882453015985, false, 0, null, 0);
            Part.ClearSelection2(true);
            object vSkLines = null;
            vSkLines = Part.SketchManager.CreateCornerRectangle(-0.09520523544121, 0.05740695090967, 0, -0.03844330645187, -0.0429584598942, 0);
            Part.ShowNamedView2("*Trimetric", 8);
            Part.ClearSelection2(true);
            object myFeature = null;
            myFeature = Part.FeatureManager.FeatureExtrusion2(true, false, true, 0, 0, 0.01, 0.01, false, false, false, false, 0.01745329251994, 0.01745329251994, false, false, false, false, true, true, true, 0, 0, false);
            boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0785775433435, 0.01894373057962, 0, true, 0, null, 0);
            boolstatus = Part.FeatureManager.InsertConvertToSheetMetal(0.002, false, false, 0.004, 0.002, 0, 0.5);
            Part.ClearSelection2(true);

            boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            Part.SketchManager.InsertSketch(true);
            Part.ClearSelection2(true);
            vSkLines = Part.SketchManager.CreateCornerRectangle(-0.02256810687936, 0.06039039042219, 0, 0.02390260459754, -0.04039198125838, 0);
            Part.ClearSelection2(true);
            myFeature = Part.FeatureManager.FeatureExtrusion2(true, false, true, 0, 0, 0.01, 0.01, false, false, false, false, 0.01745329251994, 0.01745329251994, false, false, false, false, true, true, true, 0, 0, false);
            boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0009118315510932, 0.02609254832731, 0, true, 0, null, 0);
            boolstatus = Part.FeatureManager.InsertConvertToSheetMetal(0.002, false, false, 0.004, 0.002, 0, 0.5);
            Part.ClearSelection2(true);

            Part.SketchManager.InsertSketch(true);
            boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
            Part.ClearSelection2(true);
            vSkLines = Part.SketchManager.CreateCornerRectangle(-0.05411927414525, 0.01318437124604, 0, -0.007403979976402, -0.001979918613586, 0);
            CustomBendAllowance customBendAllowanceData = null;
            customBendAllowanceData = null;
            myFeature = Part.FeatureManager.InsertSheetMetalBaseFlange2(0.002, false, 0.004, 0.02, 0.01, false, 0, 0, 1, customBendAllowanceData, false, 2, 0.0001, 0.0001, 0.5, true, false, true, true);
            Part.ClearSelection2(true);
        }

        public SldWorks swApp;
    }
}
```
