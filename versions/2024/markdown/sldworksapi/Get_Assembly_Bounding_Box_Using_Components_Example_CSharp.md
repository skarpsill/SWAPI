---
title: "Get Assembly Bounding Box Using Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Assembly_Bounding_Box_Using_Components_Example_CSharp.htm"
---

# Get Assembly Bounding Box Using Components Example (C#)

This example shows how to get a bounding box for an assembly.

```
//--------------------------------------------
// Preconditions:
// 1. Open an assembly document.
// 2. Ensure that all components in the assembly are fully resolved.
// 3. Open the Immediate window.
// 4. Run the macro.
//
// Postconditions:
// 1. Adds a 3D sketch to the assembly showing the bounding box.
// 2. Examine the graphics area and Immediate window to verify.
//
// NOTES:
// * Because all assembly component bounding boxes are
//   approximated, the bounding box for the assembly
//   is also approximated.
// * Resulting bounding box is oriented with the assembly
//   coordinate system.
//----------------------------------------------
```

```
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.sldworks;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetBoxComponents2CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public double GetMax(double Val1, double Val2, double Val3)
        {
            double functionReturnValue = 0;
            // Finds maximum of 3 values
            functionReturnValue = Val1;
            if (Val2 > functionReturnValue)
            {
                functionReturnValue = Val2;
            }
            if (Val3 > functionReturnValue)
            {
                functionReturnValue = Val3;
            }
            return functionReturnValue;
        }
        public double GetMin(double Val1, double Val2, double Val3)
        {
            double functionReturnValue = 0;
            // Finds minimum of 3 values
            functionReturnValue = Val1;
            if (Val2 < functionReturnValue)
            {
                functionReturnValue = Val2;
            }
            if (Val3 < functionReturnValue)
            {
                functionReturnValue = Val3;
            }
            return functionReturnValue;
        }

        public void Main()
        {
            const double MaxDouble = 1.79769313486231E+308;
            const double MinDouble = -1.79769313486231E+308;
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssy = default(AssemblyDoc);
            Configuration swConfig = default(Configuration);
            ConfigurationManager swConfigurationMgr = default(ConfigurationManager);
            Component2 swRootComp = default(Component2);
            object[] vChild = null;
            Component2 swChildComp = default(Component2);
            object Box = null;
            double[] BoxArray = new double[6];
            double X_max = 0;
            double X_min = 0;
            double Y_max = 0;
            double Y_min = 0;
            double Z_max = 0;
            double Z_min = 0;
            SketchManager swSketchMgr = default(SketchManager);
            SketchPoint[] swSketchPt = new SketchPoint[9];
            SketchSegment[] swSketchSeg = new SketchSegment[13];
            int i = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;
            swConfigurationMgr = (ConfigurationManager)swModel.ConfigurationManager;
            swConfig = (Configuration)swConfigurationMgr.ActiveConfiguration;
            swRootComp = (Component2)swConfig.GetRootComponent3(true);

            // Initialize values
            X_max = MinDouble;
            X_min = MaxDouble;
            Y_max = MinDouble;
            Y_min = MaxDouble;
            Z_max = MinDouble;
            Z_min = MaxDouble;

            vChild = (object[])swRootComp.GetChildren();
            for (i = 0; i <= vChild.GetUpperBound(0); i++)
            {
                swChildComp = (Component2)vChild[i];
                if (swChildComp.Visible == (int)swComponentVisibilityState_e.swComponentVisible)
                {
                    Box = (object)swChildComp.GetBox(false, false);
                    BoxArray = (double[])Box;
                    X_max = GetMax(BoxArray[0], BoxArray[3], X_max);
                    X_min = GetMin(BoxArray[0], BoxArray[3], X_min);
                    Y_max = GetMax(BoxArray[1], BoxArray[4], Y_max);
                    Y_min = GetMin(BoxArray[1], BoxArray[4], Y_min);
                    Z_max = GetMax(BoxArray[2], BoxArray[5], Z_max);
                    Z_min = GetMin(BoxArray[2], BoxArray[5], Z_min);
                }
            }

            Debug.Print("Assembly Bounding Box (" + swModel.GetPathName() + ") = ");
            Debug.Print("  (" + (X_min * 1000.0) + "," + (Y_min * 1000.0) + "," + (Z_min * 1000.0) + ") mm");
            Debug.Print("  (" + (X_max * 1000.0) + "," + (Y_max * 1000.0) + "," + (Z_max * 1000.0) + ") mm");

            swSketchMgr = swModel.SketchManager;
```

```
            swSketchMgr.Insert3DSketch(true);
            swSketchMgr.AddToDB = true;

            // Draw points at each corner of bounding box
            swSketchPt[0] = swSketchMgr.CreatePoint(X_min, Y_min, Z_min);
            swSketchPt[1] = swSketchMgr.CreatePoint(X_min, Y_min, Z_max);
            swSketchPt[2] = swSketchMgr.CreatePoint(X_min, Y_max, Z_min);
            swSketchPt[3] = swSketchMgr.CreatePoint(X_min, Y_max, Z_max);
            swSketchPt[4] = swSketchMgr.CreatePoint(X_max, Y_min, Z_min);
            swSketchPt[5] = swSketchMgr.CreatePoint(X_max, Y_min, Z_max);
            swSketchPt[6] = swSketchMgr.CreatePoint(X_max, Y_max, Z_min);
            swSketchPt[7] = swSketchMgr.CreatePoint(X_max, Y_max, Z_max);

            // Draw bounding box
            swSketchSeg[0] = swSketchMgr.CreateLine(X_min, Y_min, Z_min, X_max, Y_min, Z_min);
            swSketchSeg[1] = swSketchMgr.CreateLine(X_max, Y_min, Z_min, X_max, Y_min, Z_max);
            swSketchSeg[2] = swSketchMgr.CreateLine(X_max, Y_min, Z_max, X_min, Y_min, Z_max);
            swSketchSeg[3] = swSketchMgr.CreateLine(X_min, Y_min, Z_max, X_min, Y_min, Z_min);
            swSketchSeg[4] = swSketchMgr.CreateLine(X_min, Y_min, Z_min, X_min, Y_max, Z_min);
            swSketchSeg[5] = swSketchMgr.CreateLine(X_min, Y_min, Z_max, X_min, Y_max, Z_max);
            swSketchSeg[6] = swSketchMgr.CreateLine(X_max, Y_min, Z_min, X_max, Y_max, Z_min);
            swSketchSeg[7] = swSketchMgr.CreateLine(X_max, Y_min, Z_max, X_max, Y_max, Z_max);
            swSketchSeg[8] = swSketchMgr.CreateLine(X_min, Y_max, Z_min, X_max, Y_max, Z_min);
            swSketchSeg[9] = swSketchMgr.CreateLine(X_max, Y_max, Z_min, X_max, Y_max, Z_max);
            swSketchSeg[10] = swSketchMgr.CreateLine(X_max, Y_max, Z_max, X_min, Y_max, Z_max);
            swSketchSeg[11] = swSketchMgr.CreateLine(X_min, Y_max, Z_max, X_min, Y_max, Z_min);

            swSketchMgr.AddToDB = false;
            swSketchMgr.Insert3DSketch(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
