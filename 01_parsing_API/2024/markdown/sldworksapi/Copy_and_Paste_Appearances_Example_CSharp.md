---
title: "Copy and Paste Appearances Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_and_Paste_Appearances_Example_CSharp.htm"
---

# Copy and Paste Appearances Example (C#)

This example shows how to copy an appearance from one entity and apply it to other entities.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\introsw\vanity_assembly.sldasm.
 // 2. Press F5 repeatedly while observing the changes in the appearances of
 //    entities in the model.
 //
 // Postconditions: None
 //
 // Note: Because the model is used elsewhere, do not save changes when closing.
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
 namespace CopyAndPasteAppearances_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;

         bool boolstatus;

         public void Main()
         {
             Part = (ModelDoc2)swApp.ActiveDoc;

             object pEnt = null;
             SelectionMgr selMgr = default(SelectionMgr);
             selMgr = (SelectionMgr)Part.SelectionManager;

             Debug.Print("Selected a face, feature, body, component, or part and copied its appearance to the clipboard.");
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.196625056591301, -0.204766940654167, 0.863250195790926,  false, 0,  null, 0);
             pEnt = selMgr.GetSelectedObject6(1, -1);
             boolstatus = swApp.CopyAppearance(pEnt);

             Debug.Print("Selected a face to which was applied the copied appearance.");
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.273402696806954, 0.0150637315567224, 0.26416741603316,  false, 0,  null, 0);
             pEnt = selMgr.GetSelectedObject6(1, -1);
             boolstatus = swApp.PasteAppearance(pEnt, (int)swAppearanceTargetType_e.swAppearanceTargetFace);
             System.Diagnostics.Debugger.Break();

             Debug.Print("Selected a face to whose component was applied the copied appearance.");
             boolstatus = Part.Extension.SelectByID2("", "FACE", -2.59512148343788E-02, 0.178648261563922, 1.13882797742889,  false, 0,  null, 0);
             pEnt = selMgr.GetSelectedObject6(1, -1);
             boolstatus = swApp.PasteAppearance(pEnt, (int)swAppearanceTargetType_e.swAppearanceTargetComponent);
             System.Diagnostics.Debugger.Break();

             Debug.Print("Selected a face to whose feature was applied the copied appearance.");
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.00438233207216854, 0.239755098177056, 0.383214316118654,  false, 0,  null, 0);
             pEnt = selMgr.GetSelectedObject6(1, -1);
             boolstatus = swApp.PasteAppearance(pEnt, (int)swAppearanceTargetType_e.swAppearanceTargetFeature);
             System.Diagnostics.Debugger.Break();

             Debug.Print("Selected a face to whose part was applied the copied appearance.");
             boolstatus = Part.Extension.SelectByID2("", "FACE", -0.0112719408850239, 0.0695930730344685, 0.505696689751943,  false, 0,  null, 0);
             pEnt = selMgr.GetSelectedObject6(1, -1);
             boolstatus = swApp.PasteAppearance(pEnt, (int)swAppearanceTargetType_e.swAppearanceTargetPart);
             System.Diagnostics.Debugger.Break();

             Debug.Print("Selected a component to which was applied the copied appearance.");
             boolstatus = Part.Extension.SelectByID2("door-1@vanity_assembly", "COMPONENT", 0, 0, 0, false, 0, null, 0);
             pEnt = selMgr.GetSelectedObject6(1, -1);
             // The second parameter of SldWorks::PasteAppearance is ignored, if the selected object is not a face.
             boolstatus = swApp.PasteAppearance(pEnt, (int)swAppearanceTargetType_e.swAppearanceTargetAppearanceFilter);
             System.Diagnostics.Debugger.Break();

         }

         public SldWorks swApp;
     }

 }
```
