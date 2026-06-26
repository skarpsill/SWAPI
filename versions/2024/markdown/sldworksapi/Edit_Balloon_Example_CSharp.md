---
title: "Edit Balloon Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Edit_Balloon_Example_CSharp.htm"
---

# Edit Balloon Example (C#)

This example shows how to edit a balloon in a drawing document.

```vb
// --------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
 // 2. Click Insert > Annotations > Balloon.
 // 3. Click a model edge in either drawing view and add the balloon.
 // 4. Close the Balloon PropertyManager page.
 // 5. Select the balloon in the drawing.
 //
 // Postconditions: The properties of the selected balloon are modified.
 //
 // NOTE: Because this drawing document is used elsewhere, do not save any
 // changes when closing it.
 // --------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace EditBalloonProperties_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         ModelDoc2 swModel;
         ModelDocExtension swModelDocExt;
         SelectionMgr swSelMgr;
         Note swNote;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             // Get the selected balloon
             swNote = (Note)swSelMgr.GetSelectedObject6(1, -1);

             // Edit the selected balloon
             swNote = (Note)swModelDocExt.EditBalloonProperties2((int)swBalloonStyle_e.swBS_SplitCirc, (int)swBalloonFit_e.swBF_5Chars, (int)swBalloonTextContent_e.swBalloonTextCustom, "Upper", (int)swBalloonTextContent_e.swBalloonTextCustom, "Lower", 0, true, 1, "X",
             0.0355);

             Debug.Print("Balloon name:  " + swNote.GetName());
         }

         public SldWorks swApp;

     }
 }
```
