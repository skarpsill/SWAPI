---
title: "Set Custom Stock Body in Machined Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Set_Custom_Stock_Body_in_Machined_Part_Example_CSharp.htm"
---

# Set Custom Stock Body in Machined Part Example (C#)

This example shows how to set a custom stock body in a machined part.

```
//-----------------------------------------------
// Preconditions:
// 1. Verify that the specified:
//    * part documents to open and reference exist.
//    * Costing template exists by clicking
//      Tools > Options > System Options > File Locations
//      and select Costing templates in Show folders for
//      in SOLIDWORKS. Click Cancel to close the dialog.
// 2. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
// 3. Open the Immediate window.
// 4. Run the macro.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Creates common and machining Costing analyses, which can
//    take one or more minutes to complete.
// 3. Sets and gets custom stock body Costing information and
//    updates the estimated total cost to manufacture the part,
//    which can take one or more minutes to complete.
// 4. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not
// save any changes when closing it.
//------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.sldcostingapi;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CustomStock.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            CostManager swCosting = default(CostManager);
            CostPart swCostingPart = default(CostPart);
            CostBody swCostingBody = default(CostBody);
            object swCostingModel = null;
            CostAnalysis swCostingAnalysis = default(CostAnalysis);
            CostAnalysisMachining swCostingMachining = default(CostAnalysisMachining);
            string fileName;
            int errors = 0;
            int warnings = 0;
            int nbrCostingBodies = 0;
            object[] costingBodies = null;
            string costingBodyName = null;
            int i = 0;
            bool isBody = false;

            //Open the specified part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\clamp1.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Get CostingManager
            swCosting = (CostManager)swModelDocExt.GetCostingManager();
            swCosting.WaitForUIUpdate();

            // Get Costing part
            swCostingModel = (object)swCosting.CostingModel;
            swCostingPart = (CostPart)swCostingModel;

            // Create common Costing analysis
            swCostingAnalysis = (CostAnalysis)swCostingPart.CreateCostAnalysis("c:\\Program Files\\SolidWorks Corp\\SolidWorks\\lang\\english\\costing templates\\multibodytemplate_default(englishstandard).sldctc");

            // Get common Costing analysis data
            Debug.Print("Common Costing analysis data:");
            Debug.Print("    Template name:  " + swCostingAnalysis.CostingTemplateName);
            Debug.Print("    Currency code: " + swCostingAnalysis.CurrencyCode);
            Debug.Print("    Currency name: " + swCostingAnalysis.CurrencyName);
            Debug.Print("    Currency separator: " + swCostingAnalysis.CurrencySeparator);
            Debug.Print("    Total manufacturing cost: " + swCostingAnalysis.GetManufacturingCost());
            Debug.Print("    Material costs: " + swCostingAnalysis.GetMaterialCost());
            Debug.Print("    Setup cost: " + swCostingAnalysis.GetSetupCost());
            Debug.Print("    Total cost to charge: " + swCostingAnalysis.GetTotalCostToCharge());
            Debug.Print("    Total cost to manufacture: " + swCostingAnalysis.GetTotalCostToManufacture());
            Debug.Print("    Lot size: " + swCostingAnalysis.LotSize);
            Debug.Print("    Total quantity: " + swCostingAnalysis.TotalQuantity);
            Debug.Print("");

            // Get Costing bodies
            nbrCostingBodies = swCostingPart.GetBodyCount();
            if ((nbrCostingBodies > 0))
            {
                Debug.Print("Costing bodies:");
                Debug.Print("    Number of Costing bodies: " + nbrCostingBodies);
                costingBodies = (object[])swCostingPart.GetBodies();
                for (i = 0; i <= (nbrCostingBodies - 1); i++)
                {
                    swCostingBody = (CostBody)costingBodies[i];
                    costingBodyName = swCostingBody.GetName();
                    Debug.Print("    Name of Costing body: " + costingBodyName);
                    // Make sure body is machining body
                    if ((swCostingBody.GetBodyType() == (int)swcBodyType_e.swcBodyType_Machined))
                    {
                        isBody = true;
                        // Determine analysis status of Costing body
                        switch ((int)swCostingBody.BodyStatus)
                        {
                            case (int)swcBodyStatus_e.swcBodyStatus_NotAnalysed:
                                // Create Costing analysis
                                swCostingAnalysis = (CostAnalysis)swCostingBody.CreateCostAnalysis("c:\\Program Files\\SolidWorks Corp\\SolidWorks\\lang\\english\\costing templates\\machiningtemplate_default(englishstandard).sldcts");
                                Debug.Print("    Creating machining Costing analysis for: " + swCostingBody.GetName());
                                break;
                            case (int)swcBodyStatus_e.swcBodyStatus_Analysed:
                                // Get Costing analysis
                                swCostingAnalysis = (CostAnalysis)swCostingBody.GetCostAnalysis();
                                Debug.Print("    Getting machining Costing analysis for: " + swCostingBody.GetName());
                                break;
                            case (int)swcBodyStatus_e.swcBodyStatus_Excluded:
                                // Body excluded from Costing analysis
                                Debug.Print("    Excluded from machining Costing analysis: " + swCostingBody.GetName());
                                break;
                            case (int)swcBodyStatus_e.swcBodyStatus_AssignedCustomCost:
                                // Body has an assigned custom cost
                                Debug.Print("    Custom cost assigned: " + swCostingBody.GetName());
                                break;
                        }

                        Debug.Print("");

                    }
                }
            }

            if (!isBody)
            {
                Debug.Print("");
                Debug.Print("No bodies in part! Exiting macro.");
                return;
            }

            // Get machining Costing analysis data
            swCostingMachining = (CostAnalysisMachining)swCostingAnalysis.GetSpecificAnalysis();
            Debug.Print("Machining Costing analysis: ");
            Debug.Print("    Current material: " + swCostingMachining.CurrentMaterial);
            Debug.Print("    Current material class: " + swCostingMachining.CurrentMaterialClass);
            Debug.Print("    Current plate thickness: " + swCostingMachining.CurrentPlateThickness);

            Debug.Print("");

            // Set and get custom stock body Costing information
            swCostingMachining.CurrentStockType = (int)swcStockType_e.swcStockType_Custom;
            Debug.Print("Custom stock body Costing information:");
            swCostingMachining.CustomStockBodyName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\clamp2.sldprt";
            Debug.Print("    Body: " + swCostingMachining.CustomStockBodyName);
            swCostingMachining.CustomStockCostInfoType = (int)swcCustomStockCostInfoType_e.swcCustomStockCostType_CustomCost;
            Debug.Print("    Information type: " + swCostingMachining.CustomStockCostInfoType);
            swCostingMachining.CustomStockCustomCost = 3.53;
            Debug.Print("    Cost: " + swCostingMachining.CustomStockCustomCost);
            swCostingMachining.CustomStockImportType = (int)swcCustomStockImportType_e.swcCustomStockImportType_ReferencePart;
            Debug.Print("    Import type: " + swCostingMachining.CustomStockImportType);
            Debug.Print ("");

            // Updated estimated total cost to manufacture the part
            Debug.Print("Updated estimated total cost to manufacture: " + swCostingAnalysis.GetTotalCostToManufacture());

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
