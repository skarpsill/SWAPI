---
title: "Deselect Marked Entity Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Deselect_Marked_Entity_Example_CSharp.htm"
---

# Deselect Marked Entity Example (C#)

This example shows how to deselect a previously selected and marked entity.

```
//---------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Selects the Base-Extrude feature.
// 2. Examine the graphics area and FeatureManager
//    design tree to verify.
// 3. At System.Diagnostics.Debugger.Break(), press F5
//    to continue.
// 4. Deselects the Base-Extrude feature.
// 5. Examine the Immediate window, graphics area, and
//    FeatureManager design tree to verify.
//--------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace DeSelect2ObjectCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {

            ModelDoc2 swModel = default(ModelDoc2);
            DocumentSpecification swDocSpecification = default(DocumentSpecification);
            SelectionMgr swSelMgr = default(SelectionMgr);
            ModelDocExtension swModelExt = default(ModelDocExtension);
            bool bRet = false;
            int lMark = 0;
            int lMarkedIdx = 0;
            int lNumMarkedSelections = 0;
            int lNumAllSelections = 0;

            // Open the document
            swDocSpecification = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\swutilities\\bracket_a.sldprt");
            swModel = (ModelDoc2)swApp.ActiveDoc;
            if (swModel == null)
            {
                swModel = (ModelDoc2)swApp.OpenDoc7(swDocSpecification);
            }

            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swModelExt = (ModelDocExtension)swModel.Extension;
            // Select the Base-Extrude feature and mark it with a value of 8
            bRet = swModelExt.SelectByID2("Base-Extrude", "BODYFEATURE", 0, 0, 0, false, 8, null, (int)swSelectOption_e.swSelectOptionDefault);

            System.Diagnostics.Debugger.Break();
            // Examine the graphics area to verify
            // that Base-Extrude is selected
            // Press F5 to continue

            // Look for a given mark value
            lMark = 8;
            // Get the number of marked selections
            lNumMarkedSelections = swSelMgr.GetSelectedObjectCount2(lMark);
            Debug.Print("Number of marked selections = " + lNumMarkedSelections);

            // Get the total number of selections
            lNumAllSelections = swSelMgr.GetSelectedObjectCount2(-1);
            Debug.Print("Number of selections        = " + lNumAllSelections);

            Debug.Print(" ");

            // Deselect the marked selection
            for (lMarkedIdx = 1; lMarkedIdx <= lNumAllSelections; lMarkedIdx++)
            {
                Debug.Print("Selected object #" + lMarkedIdx + " deselected? " + swSelMgr.DeSelect2(lMarkedIdx, lMark));
            }

            // Examine the graphics area to verify that Base-Extrude is deselected

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
