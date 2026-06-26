---
title: "Get Section View Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Section_View_Data_Example_CSharp.htm"
---

# Get Section View Data Example (C#)

This example shows how to get the data for a section view in a part.

```
//-------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\cosmosxpress\aw_rubber_duct.sldprt.
// 2. Create a section view with three sections:
//    a. Right-click Front in the FeatureManager design tree
//       and click Section View.
//    b. Set X Rotation to 45.00deg in Section 1.
//    c. Select Section 2, click Top, and
//       set X Rotation to 45.00deg.
//    d. Select Section 3, click Right, and
//       set X Rotation to 45.00deg.
//    e. Click Save twice.
// 3. Click View > Display > Section View twice.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Gets and prints data about each section in
//    the section view to the Immediate window.
// 2. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//-------------------------------------------------------------------------
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
            ModelViewManager swModelViewMgr = default(ModelViewManager);
            SectionViewData swSectionViewData = default(SectionViewData);
            SelectionMgr swSelMgr = default(SelectionMgr);
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            //Get section view
            swModelViewMgr = (ModelViewManager)swModel.ModelViewManager;
            swSectionViewData = (SectionViewData)swModelViewMgr.GetSectionViewData("");

            DisplayDebugInformation(swSectionViewData, swSelMgr);

            swModel.ClearSelection2(true);

        }
        //Select the planes and print each section's data
        public void DisplayDebugInformation(SectionViewData data, SelectionMgr selMgr)
        {
            Feature p1 = default(Feature);
            Feature p2 = default(Feature);
            Feature p3 = default(Feature);
            MathTransform swMathTransform = default(MathTransform);
            double[] transform = null;

            p1 = (Feature)data.FirstPlane;
            if ((p1 != null))
                p1.Select2(true, 1);
            p2 = (Feature)data.SecondPlane;
            if ((p2 != null))
                p2.Select2(true, 2);
            p3 = (Feature)data.ThirdPlane;
            if ((p3 != null))
                p3.Select2(true, 4);

            Debug.Print("----------Section 1----------");
            Debug.Print("Offset: " + data.FirstOffset);
            Debug.Print("Rotation X: " + data.FirstRotationX);
            Debug.Print("Rotation Y: " + data.FirstRotationY);
            Debug.Print("Color: " + data.FirstColor);
            Debug.Print("Reverse direction: " + data.FirstReverseDirection);
            Debug.Print("----------Section 2----------");
            Debug.Print("Offset: " + data.SecondOffset);
            Debug.Print("Rotation X: " + data.SecondRotationX);
            Debug.Print("Rotation Y: " + data.SecondRotationY);
            Debug.Print("Color: " + data.SecondColor);
            Debug.Print("Reverse direction: " + data.SecondReverseDirection);
            Debug.Print("----------Section 3----------");
            Debug.Print("Offset: " + data.ThirdOffset);
            Debug.Print("Rotation X: " + data.ThirdRotationX);
            Debug.Print("Rotation Y: " + data.ThirdRotationY);
            Debug.Print("Color: " + data.ThirdColor);
            Debug.Print("Reverse direction: " + data.ThirdReverseDirection);
            swMathTransform = (MathTransform)data.GetDynamicCenterTransform(3);
            Debug.Print("Dynamic center transform:");
            transform = (double[])swMathTransform.ArrayData;
            if ((transform != null))
            {
                Debug.Print("  Rotate: " + transform[0].ToString("###0.0#####") + " " + transform[1].ToString("###0.0#####") + " " + transform[2].ToString("###0.0#####"));
                Debug.Print("          " + transform[3].ToString("###0.0#####") + " " + transform[4].ToString("###0.0#####") + " " + transform[5].ToString("###0.0#####"));
                Debug.Print("          " + transform[6].ToString("###0.0#####") + " " + transform[7].ToString("###0.0#####") + " " + transform[8].ToString("###0.0#####"));
                Debug.Print("  Translate: " + transform[9].ToString("###0.0#####") + " " + transform[10].ToString("###0.0#####") + " " + transform[11].ToString("###0.0#####"));
            }
            Debug.Print("----------Section Cap---------");
            Debug.Print("Show section cap: " + data.ShowSectionCap);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
