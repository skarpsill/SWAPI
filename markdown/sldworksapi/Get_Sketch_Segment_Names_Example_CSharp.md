---
title: "Get Sketch Segment Names Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Segment_Names_Example_CSharp.htm"
---

# Get Sketch Segment Names Example (C#)

This example shows how to get the names of selected sketch segments.

```
//----------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Inserts a sketch of a rectangle.
// 3. Selects two sketch segments and prints their names
//    to the Immediate window.
// 4. Examine the Immediate window.
//----------------------------------------------------
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
            SketchManager swSketchManager = default(SketchManager);
            object[] sketchLines = null;
            SketchSegment swSketchSegHoriz = default(SketchSegment);
            SketchSegment swSketchSegVert = default(SketchSegment);
            bool ret = false;

            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2016\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            ret = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, false);
            ret = swModelDocExt.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified, true);
            swSketchManager = (SketchManager)swModel.SketchManager;
            sketchLines = (object[])swSketchManager.CreateCornerRectangle(0, 0, 0, 0.110951010058045, -0.066328380491143, 0);
            ret = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0.00443505736694483, -0.012832795562811, 0.00637809258389225, false, 0, null, 0);
            ret = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0.095835993249203, -0.0306185999393385, -0.0297695225643872, true, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSketchSegHoriz = (SketchSegment)swSelMgr.GetSelectedObject6(1, -1);
            Debug.Print("Name of selected horizontal sketch segment = " + swSketchSegHoriz.GetName());
            swSketchSegVert = (SketchSegment)swSelMgr.GetSelectedObject6(2, -1);
            Debug.Print("Name of selected vertical sketch segment = " + swSketchSegVert.GetName());

            swSketchManager.InsertSketch(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
