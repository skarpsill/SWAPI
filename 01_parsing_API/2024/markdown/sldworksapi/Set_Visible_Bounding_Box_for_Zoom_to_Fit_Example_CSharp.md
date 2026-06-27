---
title: "Set Visible Bounding Box for Zoom to Fit Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_CSharp.htm"
---

# Set Visible Bounding Box for Zoom to Fit Example (C#)

This example shows how to set the visible bounding box for Zoom to Fit.

```
//--------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document to open
//    exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document and zooms to fit the
//    the assembly in the graphics area.
// 2. When Done! is printed to the Immediate window,
//    click Zoom to Fit > arm2 at the top of the
//    FeatureManager design tree.
// 3. Examine the graphics area and observe the new bounding box.
//
// NOTE: Because the assembly is used elsewhere, do not save
// changes.
//--------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            AssemblyDoc swAssembly = default(AssemblyDoc);
            MathPoint swMathPoint1 = default(MathPoint);
            MathPoint swMathPoint2 = default(MathPoint);
            MathUtility swMathUtilty = default(MathUtility);
            int options = 0;
            double[] arr1 = null;
            double[] arr2 = null;
            double[] box = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;

            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\arm2.sldasm", (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("arm2.SLDASM", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swModel.ViewZoomtofit2();
            swAssembly = (AssemblyDoc)swModel;
            swModel.ClearSelection2(true);
            options = (int)swBoundingBoxOptions_e.swBoundingBoxIncludeRefPlanes + (int)swBoundingBoxOptions_e.swBoundingBoxIncludeSketches;
            box = (double[])swAssembly.GetBox(options);

            //Change values
            box[0] = box[0] + box[0];
            box[1] = box[1] + box[1];
            box[2] = box[2] + box[2];
            box[3] = box[3] + box[3];
            box[4] = box[4] + box[4];
            box[5] = box[5] + box[5];

            //Apply the new values
            double[] ar1 = new double[3];
            double[] ar2 = new double[3];
            ar1[0] = box[0];
            ar1[1] = box[1];
            ar1[2] = box[2];
            ar2[0] = box[3];
            ar2[1] = box[4];
            ar2[2] = box[5];
            swMathUtilty = (MathUtility)swApp.GetMathUtility();
            swMathPoint1 = (MathPoint)swMathUtilty.CreatePoint(ar1);
            swMathPoint2 = (MathPoint)swMathUtilty.CreatePoint(ar2);

            //Set the bounding box
            swModelDocExt.SetVisibleBox(swMathPoint1, swMathPoint2);

            //Remove the bounding box
            //swModelDocExt.RemoveVisibleBox

            Debug.Print("Done!");

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
