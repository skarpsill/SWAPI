---
title: "Get Corner Points of a Reference Plane Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corner_Points_of_Reference_Plane_Example_CSharp.htm"
---

# Get Corner Points of a Reference Plane Example (C#)

This example shows how to obtain the four corner points of a reference plane.

```
//-----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Creates 3DSketch1 containing four corner points of the reference plane.
// 3. Gets the coordinates of each corner point.
// 4. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        bool boolstatus;
        Feature swFeature;
        RefPlane swRefPlane;
        ModelDocExtension swModelExt;
        SelectionMgr swSelMgr;
        Double[] vArrayData;
        Object[] cpObj;
        MathPoint[] vMathPoints = new MathPoint[4];
        int i;
        SketchManager sketchMgr;
        SketchPoint sketchPt;
        string filename;
        int errors;
        int warnings;
        public void Main()
        {
            filename = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\swutilities\\bracket_a.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(filename, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelExt = swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            sketchMgr = swModel.SketchManager;
            boolstatus = swModelExt.SelectByID2("Plane4", "PLANE", 0, 0, 0, false, 0, null, (int)swSelectOption_e.swSelectOptionDefault);
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swRefPlane = (RefPlane)swFeature.GetSpecificFeature2();
            cpObj = (Object[])swRefPlane.CornerPoints;
```

```
            //Four (4) MathPoint objects are always returned
            sketchMgr.Insert3DSketch(true);
            for (i = 0; i <= cpObj.GetUpperBound(0); i++)
            {
                vMathPoints[i] = (MathPoint)cpObj[i];
                vArrayData = (Double[])(vMathPoints[i].ArrayData);
                Debug.Print(" Point x = " + vArrayData[0]);
                Debug.Print(" Point y = " + vArrayData[1]);
                Debug.Print(" Point z = " + vArrayData[2]);
                Debug.Print("");
                sketchPt = sketchMgr.CreatePoint(vArrayData[0], vArrayData[1], vArrayData[2]);
            }
            sketchMgr.Insert3DSketch(true);
        }
        public SldWorks swApp;
    }
}
```
