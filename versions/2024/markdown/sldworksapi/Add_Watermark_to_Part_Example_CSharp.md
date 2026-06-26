---
title: "Add Watermark to Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Watermark_to_Part_Example_CSharp.htm"
---

# Add Watermark to Part Example (C#)

This example shows how to add and modify a watermark.

```
//--------------------------------------------------------
// Preconditions:
// 1. Open a part document.
// 2. Insert a note for a watermark.
//    a. Expand the Annotations folder in the FeatureManager
//       design tree.
//    b. Right click Notes Area and click Activate.
//    c. Click Insert > Annotations > Note.
//    d. Place the note on the model, type the note text,
//       and click OK in the Notes PropertyManager page.
//    e. Right-click the note and click Watermark.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Places the watermark behind the geometry and
//    sets its transparency level to 50%.
// 2. Examine the graphics area and the Immediate window.
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
            Note swNote = default(Note);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
```

```
	    swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swNote = (Note)swSelectionMgr.GetSelectedObject6(1, 0);
            Debug.Print("Is note a watermark? " + swNote.WatermarkNote);
            swNote.WatermarkBehindGeometry = true;
            Debug.Print("Is note behind geometry? " + swNote.WatermarkBehindGeometry);
            swNote.WatermarkTransparencyLevel = 0.50;
            Debug.Print("Note transparency level = " + swNote.WatermarkTransparencyLevel * 100 + "%");

            swModel.ClearSelection2(true);
            swModel.EditRebuild3();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
