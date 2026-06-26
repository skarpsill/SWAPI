---
title: "Create Tab and Slot Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Tab_And_Slot_Example_CSharp.htm"
---

# Create Tab and Slot Example (C#)

This example shows how to create a tab and slot feature.

```vb
  // ------------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\whatsnew\sheet metal\tab_and_slot.sldprt.
 //
 // Postconditions:
 // 1. Select Tab and Slot-Tab1 in the FeatureManager design tree;
 //     5 tabs/slots created
 // 2. Press F5 to continue.
 // 3. Select Tab and Slot-Tab1 in the FeatureManager design tree;
 //     1 tab/slot remains
 //
  // NOTE: Because the model is used elsewhere, do not save any changes to it.
  // ------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;

 namespace CreateTabAndSlot_CSharp
 {

     partial class SolidWorksMacro
     {

         private TabAndSlotFeatureData featdata;
         private TabAndSlotGroupData grp;
         private ModelDoc2 Part;
         private Edge swedge;
         private Face2 swface;
         private Feature feat;
         private TabAndSlotFeatureData newFeatData;
         private bool boolstatus;

         public void Main()
         {

             Part = (ModelDoc2)swApp.ActiveDoc;

             boolstatus = Part.Extension.SelectByRay(-0.0581596588411344, 0.0247654446213232, 0.000234517259855238, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.00157359077741066, 1, false, 0, 0);
             swedge = (Edge)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             Part.ClearSelection2(true);

             boolstatus = Part.Extension.SelectByRay(-0.0133680887414585, -0.00908584763345743, -0.00199999999999534, -0.821234743714012, -0.560561193384781, 0.106511239726198, 0.00157359077741066, 2, false, 0, 0);
             swface = (Face2)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             Part.ClearSelection2(true);

             featdata = (TabAndSlotFeatureData)Part.FeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmTabAndSlot);

             grp = (TabAndSlotGroupData)featdata.SelectionAddNewGroup();
             grp.Offset = true;
             grp.SelectionTabEdge = swedge;
             grp.SelectionSlotFace = swface;
             Part.FeatureManager.CreateFeature(featdata);

             System.Diagnostics.Debugger.Break();

             // Select Tab and Slot-Tab1 in the FeatureManager design tree; 5 tabs/slots created on the part
             // Press F5 to continue

             feat = (Feature)((SelectionMgr)(Part.SelectionManager)).GetSelectedObject6(1, -1);
             newFeatData = (TabAndSlotFeatureData)feat.GetDefinition();
             TabAndSlotGroupData[] var = null;
             newFeatData.AccessSelections(Part, null);
             var = (TabAndSlotGroupData[])newFeatData.SelectionGetGroups();
             var[0].Offset = false;
             var[0].SpacingType = 0;
             var[0].SpacingNumberOfInstances = 1;
             feat.ModifyDefinition(newFeatData, Part, null);

             // Select Tab and Slot-Tab1 in the FeatureManager design tree; only one tab and slot remain

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }

 }
```
