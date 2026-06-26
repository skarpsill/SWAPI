---
title: "Create Bidirectional Linear Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Bidirectional_Linear_Pattern_Example_CSharp.htm"
---

# Create Bidirectional Linear Pattern Example (C#)

This example shows how to create a bidirectional linear pattern.

```
//----------------------------------------------------
// Preconditions: Verify that the part exists.
//
// Postconditions:
// 1. Opens the part.
// 2. Selects the feature to pattern.
// 3. Selects the edges for Direction 1 and
//    Direction 2 for the bidirectional linear
//    pattern.
// 4. Creates a bidirectional linear pattern.
// 5. Examine the FeatureManager design tree and
//    graphics area.
//
// NOTE: Because the part is used elsewhere, do not save
// changes.
//------------------------------------------------------

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

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;

            //Select feature to pattern
            status = swModelDocExt.SelectByID2("CBORE for #6 Binding Head Machine Screw1", "BODYFEATURE", 0, 0, 0, false, 4, null, 0);

            //Select edges for Direction 1 and Direction 2
            status = swModelDocExt.SelectByID2("", "EDGE", -0.0341223962029176, 0.0300321434688158, 0.0460303188361877, true, 1, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0436465176948104, 0.0301916139486593, 0.0114344277122314, true, 2, null, 0);

            //Create linear pattern
            swFeature = (Feature)swFeatureManager.FeatureLinearPattern5(3, 0.01, 3, 0.01, false, false, "NULL", "NULL", true, false,
            false, false, false, false, true, true, false, false, 0, 0, false,
            false);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
