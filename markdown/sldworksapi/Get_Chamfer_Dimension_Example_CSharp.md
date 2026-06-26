---
title: "Get Chamfer Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Chamfer_Dimension_Example_CSharp.htm"
---

# Get Chamfer Dimension Example (C#)

This example shows how to the values of a chamfer dimension.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Open a drawing that contains a chamfered part.
// 2. Click Tools > Dimension > Chamfer.
// 3. Select a chamfered edge, select one of the lead-in edges, and click
//    the drawing to display and select the chamfer dimension.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Gets the chamfer dimensions.
// 2. Examine the Immediate window.
//---------------------------------------------------------------------------
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
            SelectionMgr swSelMgr = default(SelectionMgr);
            DisplayDimension swDisplayDimension = default(DisplayDimension);
            Dimension swDimension = default(Dimension);
            bool status = false;
            double length = 0;
            double angle = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;

            //Get chamfer dimensions
            swDisplayDimension = (DisplayDimension)swSelMgr.GetSelectedObject6(1, -1);
            swDimension = (Dimension)swDisplayDimension.GetDimension();
            status = swDimension.GetSystemChamferValues(ref length, ref angle);
            Debug.Print("Is selected dimension a chamfer dimension? " + status);
            //1 radian = 180º/p = 57.295779513º or approximately 57.3º
            Debug.Print("Angle = " + (angle * 57.3) + " degrees");
            Debug.Print("Length = " + length);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
