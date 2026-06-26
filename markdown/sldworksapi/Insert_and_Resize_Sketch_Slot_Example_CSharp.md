---
title: "Insert and Resize Sketch Slot Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Resize_Sketch_Slot_Example_CSharp.htm"
---

# Insert and Resize Sketch Slot Example (C#)

This example shows how to insert a sketch slot and resize it.

```
//--------------------------------------------------------
// Preconditions:
// 1. Open a new part document.
// 2. Open the Immediate window..
//
//Postconditions:
// 1. Creates a sketch and inserts a sketch slot.
// 2. Press F5 after examining the graphics area.
// 3. Resizes the slot.
// 4. Examine the graphics area and Immediate window.
//-------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        ModelDocExtension swExt;
        SelectionMgr swSelMgr;
        bool boolstatus;
        PartDoc swPart;
        SketchManager skManager;

        public void Main()
        {
            swModel = swApp.ActiveDoc as ModelDoc2;
            swExt = swModel.Extension;
            swSelMgr = swModel.SelectionManager as SelectionMgr;
            skManager = swModel.SketchManager;
            swPart = swModel as PartDoc;
            boolstatus = swExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);

            skManager.InsertSketch(true);
            SketchSlot swSketchSlot;
            swSketchSlot = skManager.CreateSketchSlot((int)swSketchSlotCreationType_e.swSketchSlotCreationType_line, (int)swSketchSlotLengthType_e.swSketchSlotLengthType_CenterCenter,
                0.05, -0.05, 0, 0, 0.05, 0, 0, 0, 0, 0, 1, false);
            swSketchSlotLengthType_e lengthType;
            lengthType = (swSketchSlotLengthType_e)swSketchSlot.LengthType;
            Debug.Print("Length: " + swSketchSlot.Length);
            Debug.Print("Length Type: " + lengthType.ToString());
            Debug.Print("Width: " + swSketchSlot.Width);

            System.Diagnostics.Debugger.Break();

            // Edit the original slot
            swSketchSlot.Width = swSketchSlot.Width * 2.0;
            Debug.Print("Modified width: " + swSketchSlot.Width);
            skManager.InsertSketch(true);
        }
        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
