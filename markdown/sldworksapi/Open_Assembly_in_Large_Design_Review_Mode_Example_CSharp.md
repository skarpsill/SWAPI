---
title: "Open an Assembly in Large Design Review Mode Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm"
---

# Open an Assembly in Large Design Review Mode Example (C#)

This example shows how to open an assembly in Large Design Review mode.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly to open in Large Design Review mode exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Click OK in the Large Design Review dialog.
// 2. Opens the assembly.
// 3. Creates a section view.
// 4. Creates four snapshots in the DisplayManager:
//    * Home
//    * ASnap
//    * Snap2
//    * Snap3
// 5. Click OK in the Name Snapshot dialog.
// 6. Selects and fully resolves a component.
// 7. Inspect the Immediate window for snapshot information and inspect
//    the graphics area.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
// ---------------------------------------------------------------------------
using Microsoft.VisualBasic;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        AssemblyDoc Part;
        ModelDoc2 Model;
        SnapShot snap;
        object[] snaps;
        SnapShot snap1;
        SnapShot snap2;
        SnapShot snap3;
        int i;
        bool boolstatus;
        int longstatus;
        int longwarnings;

        public void Main()
        {
            string large_assembly_document;
            large_assembly_document = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\motor casing.sldasm";
            Part = (AssemblyDoc)swApp.OpenDoc6(large_assembly_document, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_ViewOnly, "", ref longstatus, ref longwarnings);
            Model = (ModelDoc2)Part;

            // Create section view
            SectionViewData sViewData = default(SectionViewData);
            sViewData = Model.ModelViewManager.CreateSectionViewData();
            sViewData.FirstPlane = null;
            sViewData.FirstReverseDirection = false;
            sViewData.FirstOffset = -0.00508;
            sViewData.FirstRotationX = 0;
            sViewData.FirstRotationY = 0;
            sViewData.FirstColor = 16711680;
            sViewData.ShowSectionCap = true;
            sViewData.KeepCapColor = true;

            ModelViewManager mvmgr = default(ModelViewManager);
            mvmgr = Model.ModelViewManager;
            boolstatus = mvmgr.CreateSectionView(sViewData);
            Model.ClearSelection2(true);
            Model.ShowNamedView2("*Front", 1);
            Model.ShowNamedView2("*Dimetric", 9);

            // Add a named snapshot
            snap1 = mvmgr.AddSnapShot("ASnap");
            // Open dialog box to name the next snapshot
            snap2 = mvmgr.AddSnapShot("?");
            // Add a snapshot with the next default name
            snap3 = mvmgr.AddSnapShot("");

            snap1.Comment = "<TS> This is a comment for ASnap.";

            snaps = (object[])mvmgr.GetSnapShots();

            for (i = 0; i <= snaps.GetUpperBound(0); i++)
            {
                snap = (SnapShot)snaps[i];
                snap.Activate();
                Debug.Print("Snapshot name: " + snap.Name);
                Debug.Print("      Comment: " + snap.Comment);
                Debug.Print("       ViewID: " + snap.ViewId);
            }

            // Selects a component
            boolstatus = Model.Extension.SelectByID2("motor casing-1@motor casing", "COMPONENT", 0, 0, 0, false, 0, null, 0);

            // Fully resolve only the selected components
            Part.SelectiveOpen(true, false);

        }

        public SldWorks swApp;

    }
}
```
