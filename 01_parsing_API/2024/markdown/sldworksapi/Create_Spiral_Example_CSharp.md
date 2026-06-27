---
title: "Create Spiral Example"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Spiral_Example_CSharp.htm"
---

# Create Spiral Example

## Create Spiral Example (C#)

This example shows how to create a spiral.

```
//----------------------------------------------------------
// Preconditions: Specified part template exists.
//
// Postconditions:
// 1. Opens a new part.
// 2. Selects Front Plane on which to create a circle.
// 3. Creates a circle.
// 4. Creates a spiral using the circle.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace SpiralCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchManager swSketchMgr = default(SketchManager);
            SketchSegment swSketchSegment = default(SketchSegment);
            bool status = false;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2015\\templates\\Part.prtdot", 0, 0, 0);
            //Select Front Plane, create circle, and create
            //spiral using circle
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", -0.0517981810568133, 0.0505753331558577, 0.0012310671470727, false, 0, null, 0);
            swModel.ClearSelection2(true);
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSketchSegment = (SketchSegment)swSketchMgr.CreateCircle(0.0, 0.0, 0.0, 0.021866, 0.001156, 0.0);
            swModel.InsertHelix(false, true, false, false, (int)swHelixDefinedBy_e.swHelixDefinedBySpiral, 0, 0.04, 2, 0, 4.712388980385);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
