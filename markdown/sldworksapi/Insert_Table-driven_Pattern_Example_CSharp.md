---
title: "Insert Table-driven Pattern Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Table-driven_Pattern_Example_CSharp.htm"
---

# Insert Table-driven Pattern Example (C#)

This example shows how to insert a table-driven pattern.

```
//--------------------------------------------------------------------
// Preconditions:
// 1. Verify that c:\temp exists.
// 2. Open public_documents\samples\tutorial\api\tablepattern.sldprt.
// 3. Edit TPattern1.
// 4. Click Save As, browse to c:\temp, type TestTable.sldptab in File name,
//    click Save, and click OK.
// 5. Edit c:\temp\TestTable.sldptab and change:
//    a. 0.01m to 0.04m.
//    b. -0.03m to -0.025m.
// 6. Save c:\temp\TestTable.sldptab.
// 7. Delete TPattern1.
//
// Postconditions:
// 1. Creates TPattern1.
// 2. Examine the FeatureManager design tree and the graphics
//    area.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//-------------------------------------------------------------------

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
            FeatureManager swFeatureMgr = default(FeatureManager);
            Feature swPatternFeature = default(Feature);
            object swPatternPoints = null;
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            status = swModelDocExt.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, true, 16, null, 0);
            status = swModelDocExt.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0, 0, 0, true, 4, null, 0);
            swPatternFeature = (Feature)swFeatureMgr.InsertTableDrivenPattern2("c:\\temp\\TestTable.sldptab", (swPatternPoints), true, false, true);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
