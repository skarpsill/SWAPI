---
title: "Get and Set Center Mark Set Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Center_Marks_Set_Example_CSharp.htm"
---

# Get and Set Center Mark Set Example (C#)

This example shows how to get and set properties of a center mark set.

```
//------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\introtosw\pressure_plate.sldprt.
// 2. Click File > Make Drawing from Part > OK.
// 3. Drag Bottom from the View Palette to Sheet1 and click OK.
// 4. Click a center mark and press Delete.
// 5. Open the Immediate window.
//
// Postconditions:
// 1. Activates Drawing View1.
// 2. Selects a center mark in Drawing View1.
// 3. Gets and sets properties of the center mark set.
// 4. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//-----------------------------------------------------------------------
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
            DrawingDoc swDrawingDoc = default(DrawingDoc);
            CenterMark swCenterMark = default(CenterMark);
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            bool status = false;
            int nbrInGroup = 0;
            int i = 0;
            double[] cmCoordinates = new double[3];

            swDrawingDoc = (DrawingDoc)swApp.ActiveDoc;

            //Get drawing view
            swDrawingDoc.ActivateView("Drawing View1");
            swModel = (ModelDoc2)swDrawingDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Select a center mark
            status = swModelDocExt.SelectByID2("DetailItem217@Drawing View1", "CENTERMARKSYM", 0.650520142546246, 0.417728685527748, 0, false, 0, null, 0);

            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swCenterMark = (CenterMark)swSelectionMgr.GetSelectedObject6(1, -1);

            //Get and set properties of center mark set
            Debug.Print("Center mark set");
            Debug.Print(" Style (4 = swCenterMark_CircularGroup): " + swCenterMark.Style);
            Debug.Print(" Is grouped? " + swCenterMark.IsGrouped);
            nbrInGroup = swCenterMark.GroupCount;
            Debug.Print(" Number in set: " + (nbrInGroup - 1));
            Debug.Print(" Any detached? " + swCenterMark.HasDetachCenterMark());
            for (i = 0; i <= nbrInGroup - 1; i++)
            {
                Debug.Print("   Center mark: " + i);
                Debug.Print("      Detached: " + swCenterMark.IsDetached(i));
                cmCoordinates = (double[])swCenterMark.GetPosition(i);
                Debug.Print("      x, y, z coordinates: " + cmCoordinates[0] + ", " + cmCoordinates[1] + ", " + cmCoordinates[2]);
                Debug.Print("      Original extended length: " + swCenterMark.GetExtendedLength(i, (int)swCenterMarkHandle_e.swCenterMarkHandle_Right));
                status = swCenterMark.SetExtendedLength(i, (int)swCenterMarkHandle_e.swCenterMarkHandle_Right, 0.005);
                Debug.Print("      Modified extended length: " + swCenterMark.GetExtendedLength(i, (int)swCenterMarkHandle_e.swCenterMarkHandle_Right));
                Debug.Print("      Is deleted? " + swCenterMark.IsDeleted(i));
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
