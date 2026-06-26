---
title: "Insert GTol Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_GTol_Example_CSharp.htm"
---

# Insert GTol Example (C#)

This example shows how to insert a GTol with a bent leader.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the drawing exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the drawing.
// 2. Inserts a GTol.
// 3. Sets and gets the length of the bent leader.
// 4. Gets whether to display the projected tolerance zone and its height
//    in the GTol.
// 5. Examine the Immediate window and GTol.
//
// NOTE: Because the drawing is used elsewhere, do not save changes.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public void Main()
        {
            DrawingDoc swDrawing = default(DrawingDoc);
            ModelDoc2 swModel = default(ModelDoc2);
            Gtol swGtol = default(Gtol);
            Annotation swAnno = default(Annotation);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            int frameNbr = 0;
            int tolNbr = 0;
            bool display = false;
            string height = "";

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";
            swDrawing = (DrawingDoc)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swApp.ActivateDoc3("foodprocessor - Sheet1", false, (int)swRebuildOnActivation_e.swRebuildActiveDoc, ref errors);
            swModel = (ModelDoc2)swDrawing;

            swGtol = (Gtol)swModel.InsertGtol();
            if ((swGtol != null))
            {
                swGtol.SetFrameSymbols2(1, "<IGTOL-POSI>", false, "", false, "", "", "", "");
                swGtol.SetFrameValues2(1, "0.2", "", "B-A-C<MOD-MMC>", "B<MOD-MMC>-C<MOD-LMC>", "C<MOD-MMC>-A");
                swGtol.SetPTZHeight2(1, 1, true, "50");
                swGtol.SetBetweenTwoPoints(false, "", "");
                swAnno = (Annotation)swGtol.GetAnnotation();
                if ((swAnno != null))
                {
                    status = swAnno.SetPosition(0.319315975204224, 0.12666668401487, 0);
                    errors = swAnno.SetLeader3((int)swLeaderStyle_e.swBENT, (int)swLeaderSide_e.swLS_LEFT, true, false, false, false);
                    swAnno.BentLeaderLength = 0.05;
                    Debug.Print("Bent leader length: " + swAnno.BentLeaderLength);
                }
            }

            frameNbr = 1;
            tolNbr = 1;
            height = "";
            status = swGtol.GetPTZHeight2(frameNbr, tolNbr, out display, out height);
            Debug.Print("Projected tolerance zone: ");
            Debug.Print("  Display: " + display);
            Debug.Print("  Height: " + height);

            swModel.WindowRedraw();

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
