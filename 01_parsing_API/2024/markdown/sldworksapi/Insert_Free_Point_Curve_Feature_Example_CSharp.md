---
title: "Insert Free Point Curve Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Free_Point_Curve_Feature_Example_CSharp.htm"
---

# Insert Free Point Curve Feature Example (C#)

This example shows how to insert a free point curve feature.

```
//---------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part template exists.
// 2. Create c:\temp, if this folder does not exist.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Creates a new part document.
// 2. Inserts a free point curve feature.
// 3. Gets some free point curve feature data.
// 4. Saves the free point curve feature's points to a file.
// 5. Examine the graphics area, FeatureManager design tree,
//    Immediate window, and c:\temp.
//---------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace FreePointCurveFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            FreePointCurveFeatureData swFreePointCurveFeatureData = default(FreePointCurveFeatureData);
            bool status = false;
            int nbrPoints = 0;
            double[] pointArray = null;
            int i = 0;

            //Create new part document
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);

            //Insert free point curve feature
            swModel.InsertCurveFileBegin();
            status = swModel.InsertCurveFilePoint(0, 0, 0);
            status = swModel.InsertCurveFilePoint(0, 0, 0.0127);
            status = swModel.InsertCurveFilePoint(0, 0, 0.0254);
            status = swModel.InsertCurveFilePoint(0, 0, 0.0381);
            status = swModel.InsertCurveFilePoint(0, 0.0254, 0.0381);
            status = swModel.InsertCurveFilePoint(0, 0.0381, 0.0381);
            status = swModel.InsertCurveFileEnd();

            //Get free point curve feature
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            status = swModelDocExt.SelectByID2("Curve1", "REFERENCECURVES", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            //Get number of points in free point curve feature
            swFreePointCurveFeatureData = (FreePointCurveFeatureData)swFeature.GetDefinition();
            nbrPoints = swFreePointCurveFeatureData.GetPointCount();
            Debug.Print("Number of points in free point curve feature: " + nbrPoints);
            //Get the points in free point curve feature
            pointArray = (double[])swFreePointCurveFeatureData.PointArray;
            Debug.Print("Points in free point curve feature: ");
            for (i = 0; i <= nbrPoints - 1; i++)
            {
                Debug.Print("  " + pointArray[i]);
            }
            //Save the points in free point curve feature to file
            status = swFreePointCurveFeatureData.SavePointsToFile("c:\\temp\\MyFreePointCurveFeature.sldcrv");
            Debug.Print("Curve file created in specified folder: " + status);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
