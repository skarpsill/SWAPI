---
title: "Insert Connection Point Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Connection_Point_Example_CSharp.htm"
---

# Insert Connection Point Example (C#)

This example shows how to create a connection point for a tube for routing.

```
//---------------------------------------------------
// Preconditions:
// 1. Load the SOLIDWORKS Routing Add-in (click
//    Tools > Add-Ins > SOLIDWORKS Routing).
// 2. Verify that the specified part document to open
//    exists.
//
// Postconditions:
// 1. Creates a connection point for a tube
//    using the selected edge.
// 2. Examine the graphics area and Immediate window.
//
// NOTE: Because this part document is used elsewhere,
// do not save changes.
//---------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace InsertConnectionPointFeatureManagerCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            FeatureManager swFeatMgr = default(FeatureManager);
            int errors = 0;
            int warnings = 0;
            bool status = false;

            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\routing-pipes\\fittings\\filter.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Select the edge for the connection point;
            // remember to specify a value of 1 for
            // the Mark parameter for a circular edge for
            // a tube's connection point
            status = swModelDocExt.SelectByID2("", "EDGE", 0.001425156111225, 0.1755840982619, -0.09117938337181, false, 1, null, 0);

            // Insert a connection point for a tube
            swFeatMgr = swModel.FeatureManager;
            Debug.Print("Connection point for tube created? " + swFeatMgr.InsertConnectionPoint((int)swConnectionPointType_e.swConnectionPoint_Tube, 0, true, 25.4 / 1000, 0.1, 0.2, 0.3, 0.4, "", 0,
            0, false, "Specification", ""));
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
