---
title: "Create Circular Pattern of Subassembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Circular_Pattern_of_Subassembly_Example_CSharp.htm"
---

# Create Circular Pattern of Subassembly Example (C#)

This example shows how to create a circular pattern of a subassembly.

```
//-------------------------------------------------------
// Preconditions: Verify that the assembly exists.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Selects an edge for Direction 1.
// 3. Selects a subassembly to pattern.
// 4. Creates a circular pattern.
// 5. Examine the FeatureManager design tree and
//    graphics area.
//
// NOTE: Because the assembly is used elsewhere, do not
// save changes.
//--------------------------------------------------------
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
            status = swModelDocExt.SelectByID2("", "EDGE", 0.22639417933982, -0.194822643434378, 0.102086175644843, false, 2, null, 0);
            status = swModelDocExt.SelectByID2("mount base-1@distance linkage", "COMPONENT", 0, 0, 0, true, 1, null, 0);
            swFeature = (Feature)swFeatureManager.FeatureCircularPattern5(3, 2.0943951023932, false, "NULL", false, true, false, false, false, false, 0, 0, "NULL", false);
            swModel.ClearSelection2(true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
