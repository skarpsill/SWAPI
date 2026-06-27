---
title: "Split FeatureManager Design Tree and Position Splitter Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_CSharp.htm"
---

# Split FeatureManager Design Tree and Position Splitter Example (C#)

This example shows how:

- to split a FeatureManager design tree.
- add a tab to one of the FeatureManager design trees.
- change the location of the split panel bar (splitter).

```vb
 //----------------------------------------------------------
 // Preconditions:
 // 1. In the IDE, reference your ActiveX control file
 //    (click Project > Add Reference > Browse and browse
 //    to the folder where the ActiveX control resides and click
 //    the ActiveX control file > OK).
 // 2. Verify that the specified part document and bitmap exist.
 // 3. Replace activex_control_component_declaration and
 //    activex_control_CLSID_or_ProgID with your ActiveX control's
 //    information.
 //
 // Postconditions:
 // 1. Opens the part document and splits the FeatureManager
 //    design tree; the splitter is below the FeatureManager
 //    design tree to which the tab was added. Drag the splitter
 //    to verify.
 // 2. Close the part document.
 // 3. Set test to 1.
 // 4. Rerun the macro.
 // 5. Opens the part document and splits the FeatureManager
 //    design tree; the splitter is above the FeatureManager
 //    design tree to which the tab was added. Drag the
 //    splitter to verify.
 //
 // NOTE: Because the part document is used elsewhere,
 // do not save changes.
 //----------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;

 namespace FeatureManagerSplitterPositionModelDoc2CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             const string iconSmall = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\data\\user macro icons\\button.bmp";

             ModelDoc2 swModel = default(ModelDoc2);
             ModelViewManager swModViewMgr =  default(ModelViewManager);
             FeatMgrView swFeatMgrTabTop =  default(FeatMgrView);
             FeatMgrView swFeatMgrTabBtm =  default(FeatMgrView);
             activex_control_component_declaration ctrlTop =  default(activex_control_component_declaration);
             activex_control_component_declaration ctrlBtm =  default(activex_control_component_declaration);
             string fileName = null;
             int errors = 0;
             int warnings = 0;
             int activePane = 0;
             int test = 0;

             fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\fillets\\knob.sldprt";
             swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swModViewMgr = (ModelViewManager)swModel.ModelViewManager;

             if (test == 0)
             {
                 // FeatureManager design tree is split, and the splitter is
                 // below the FeatureManager design tree to which the
                 // tab was added
                 swFeatMgrTabTop = (FeatMgrView)swModViewMgr.CreateFeatureMgrControl2(iconSmall,  "activex_control_CLSID_or_ProgID", "", "Top tab ToolTip", (int)swFeatMgrPane_e.swFeatMgrPaneTop);
                 ctrlTop = (activex_control_component_declaration)swFeatMgrTabTop.GetControl();
                 swModel.FeatureManagerSplitterPosition = 0.0;
                 activePane = swFeatMgrTabTop.ActivateView();
             }
             else
             {
                 // FeatureManager design tree is split, and the splitter is
                 // above the FeatureManager design tree to which the
                 // tab was added
                 swFeatMgrTabBtm = (FeatMgrView)swModViewMgr.CreateFeatureMgrControl2(iconSmall,  "activex_control_CLSID_or_ProgID", "", "Bottom tab ToolTip", (int)swFeatMgrPane_e.swFeatMgrPaneBottom);
                 ctrlBtm = (activex_control_component_declaration)swFeatMgrTabBtm.GetControl();
                 swModel.FeatureManagerSplitterPosition = 1.0;
                 activePane = swFeatMgrTabBtm.ActivateView();
             }
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
