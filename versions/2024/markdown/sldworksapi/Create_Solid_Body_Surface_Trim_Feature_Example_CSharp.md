---
title: "Create Solid Body Surface Trim Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Solid_Body_Surface_Trim_Feature_Example_CSharp.htm"
---

# Create Solid Body Surface Trim Feature Example (C#)

This example shows how to create a solid body surface trim feature.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part.
// 2. Creates Surface-Trim1.
// 3. Expand and examine Solid Bodies(1) in the FeatureManager
//    design tree and examine the Immediate window.
//
// NOTE: Because the model is used elsewhere, do not save changes.
//----------------------------------------------------------------
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
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatureManager = default(FeatureManager);
            Feature swFeature = default(Feature);
            bool status = false;
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\SurfaceTrimFeature.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swFeatureManager = (FeatureManager)swModel.FeatureManager;

            // Select surface features
            status = swModelDocExt.SelectByID2("", "SURFACEBODY", -0.0446486526100784, 0.0218350174377093, 0.0123754341749418, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "SURFACEBODY", -0.00815686270678384, 0.0415839719953865, 0.0242402652081068, true, 0, null, 0);

            // Select trimming surfaces to create solid body surface trim feature
            status = swFeatureManager.PreTrimSurface(true, true, false, true);
            status = swModelDocExt.SelectByID2("", "SURFACEBODY", 0.0059504253577245, 0.0413800871671199, 0.0248740287174201, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "SURFACEBODY", -0.037205042299604, 0.0343527327176432, 0.0123446167727934, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "SURFACEBODY", -0.0104497983190015, -0.0472172176775487, 0.0233436625590571, true, 0, null, 0);
            Debug.Print("Solid body surface trim feature? " + swFeatureManager.SolidForTrim);
            swFeatureManager.SolidForTrim = true;
            Debug.Print("Solid body surface trim feature? " + swFeatureManager.SolidForTrim);
            swFeature = (Feature)swFeatureManager.PostTrimSurface(true);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
