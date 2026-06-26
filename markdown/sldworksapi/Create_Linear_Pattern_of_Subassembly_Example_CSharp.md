---
title: "Create Linear Pattern of Subassembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Linear_Pattern_of_Subassembly_Example_CSharp.htm"
---

# Create Linear Pattern of Subassembly Example (C#)

This example shows how to create a linear pattern of a subassembly.

```
//--------------------------------------------------
// Preconditions: Verify that the assembly exists.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Selects an edge for Direction 1.
// 3. Selects a subassembly to pattern.
// 4. Creates a linear pattern.
// 5. Examine the FeatureManager design tree and
//    graphics area.
//
// NOTE: Because the assembly is used elsewhere, do
// not save changes.
//---------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\distance linkage.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            status = swModelDocExt.SelectByID2("", "EDGE", 0.222723097227572, -0.193386735236572, -0.10172211746567, false, 2, null, 0);
            status = swModelDocExt.SelectByID2("mount base-1@distance linkage", "COMPONENT", 0, 0, 0, true, 1, null, 0);
            swFeature = (Feature)swFeatureManager.FeatureLinearPattern5(4, 0.254, 1, 0.05, false, false, "NULL", "NULL", false, false,
            false, false, false, false, true, true, false, false, 0, 0, false,
            false);
            swModel.ClearSelection2(true);
            swModel.ViewZoomtofit2();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
