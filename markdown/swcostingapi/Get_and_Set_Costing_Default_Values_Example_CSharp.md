---
title: "Get and Set Costing Default Values Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Get_and_Set_Costing_Default_Values_Example_CSharp.htm"
---

# Get and Set Costing Default Values Example (C#)

This example shows how to get and set Costing default values.

```
//-----------------------------------------------
// Preconditions:
// 1. Specified sheet metal part to open exists.
// 3. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
// 4. Open the Immediate window.
// 5. Open the Notepad text editor.
// 6. Run the macro.
//
// Postconditions:
// 1. Opens the specified sheet metal part.
// 2. Prints to the Immediate window the current
//    Costing default values.
// 3. Copy and paste the contents of the
//    Immediate window into Notepad.
// 4. Press F5 to continue.
// 5. Sets some new Costing default values.
// 6. Pops up a message box.
// 7. After reading the instructions in the message box,
//    click OK to close the message box, and perform the
//    instructions.
//
// NOTE: Running this macro changes the specified Costing
// default values in your computer's registry.
//------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.sldcostingapi;
using System.Runtime.InteropServices;
using System.Diagnostics;
using System.Windows.Forms;

namespace DefaultsSheetMetalCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            CostManager swcCostingMgr = default(CostManager);
            CostPart swcCostingPart = default(CostPart);
            CostBody swcCostingBody = default(CostBody);
            CostingDefaults swcCostingDefaults = default(CostingDefaults);
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            //Open the specified part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\costing\\sheet_metal_part.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Get CostingManager
            swcCostingMgr = (CostManager)swModelDocExt.GetCostingManager();
            if (swcCostingMgr == null)
            {
                Debug.Print("CostingManager is nothing.");
                return;
            }

            //Get Costing part
            swcCostingPart = (CostPart)swcCostingMgr.CostingModel;
            if (swcCostingPart == null)
            {
                Debug.Print("Costing part is nothing.");
                return;
            }

            //Set the Costing manufacturing method
            //to sheet metal and get the Costing body
            swcCostingBody = (CostBody)swcCostingPart.SetCostingMethod("", (int)swcMethodType_e.swcMethodType_Sheetmetal);
            if (swcCostingBody == null)
            {
                Debug.Print("Costing body is nothing.");
                return;
            }

            //Get Costing defaults object
            swcCostingDefaults = (CostingDefaults)swcCostingMgr.CostingDefaults;
            if (swcCostingDefaults == null)
            {
                Debug.Print("Costing defaults is nothing.");
                return;
            }

            //Get Costing defaults registry values
            Debug.Print("Costing costing defaults values:");
            Debug.Print("    Template name:  " + swcCostingDefaults.GetTemplateName((int)swcCostingType_e.swcCostingType_SheetMetal));
            Debug.Print("    Manufacturing method: " + swcCostingDefaults.GetManufacturingMethod((int)swcBodyType_e.swcBodyType_SheetMetal));
            Debug.Print("    Material class: " + swcCostingDefaults.GetMaterialClass((int)swcMethodType_e.swcMethodType_Sheetmetal));
            Debug.Print("    Material name: " + swcCostingDefaults.GetMaterialName((int)swcMethodType_e.swcMethodType_Sheetmetal));
            Debug.Print("    Lot size for single-body mode: " + swcCostingDefaults.LotSizeForSingleBody);
            Debug.Print("    Sheet metal blank size type: " + swcCostingDefaults.SheetmetalBlankSizeType);
            Debug.Print("    Total number of parts for single body: " + swcCostingDefaults.TotalNumberOfPartsForSingleBody);
            Debug.Print("");

            System.Diagnostics.Debugger.Break();

            //Examine the Immediate window
            //Copy and paste the contents of the
            //Immediate window into Notepad if
            //running the macro for the first time
            //Press F5 to continue

            //Set some new Costing default registry values
            swcCostingDefaults.SetMaterialClass((int)swcMethodType_e.swcMethodType_Sheetmetal, "Titanium Alloys");
            swcCostingDefaults.SetMaterialName((int)swcMethodType_e.swcMethodType_Sheetmetal, "Commercially Pure Grade 2 Textured (SS)");
            swcCostingDefaults.LotSizeForSingleBody = 125;
            swcCostingDefaults.TotalNumberOfPartsForSingleBody = 125;

            //Pop up message box
            MessageBox.Show("1. Save and exit the macro." + System.Environment.NewLine + "2. Close the part without saving any changes." + System.Environment.NewLine + "3. Exit SOLIDWORKS." + System.Environment.NewLine + "4. Start up SOLIDWORKS and run the macro again." + System.Environment.NewLine + "5. Examine the Immediate window and Notepad to verify that new default values were set in the registry, where applicable.");

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
