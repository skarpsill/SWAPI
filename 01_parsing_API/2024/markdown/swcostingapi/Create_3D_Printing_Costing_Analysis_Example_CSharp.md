---
title: "Create 3D Printing Costing Analysis Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Create_3D_Printing_Costing_Analysis_Example_CSharp.htm"
---

# Create 3D Printing Costing Analysis Example (C#)

This example shows how to create a 3D printing Costing analysis for a part.

```
//-----------------------------------------------
// Preconditions:
// 1. Specified part to open exists.
// 2. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
// 3. Open the Immediate window.
// 4. Run the macro.
//
// Postconditions:
// 1. Opens the specified part.
// 2. Gets the CostingManager.
// 3. Gets the Costing part.
// 4. Sets the Costing manufacturing method
//    to 3D printing and gets the Costing body.
// 5. Gets the common Costing analysis and
//    the 3D printing Costing analysis.
// 6. Gets the material classes from the Costing template
//    and sets the material class.
// 7. Gets the material names from the Costing template
//    and sets the material for the material class.
// 8. Sets and gets 3D printing Costing analysis
//    parameters.
// 9. Gets the total manufacturing cost.
//10. Examine the Immediate window to see the
//    results of steps 6 through 9.
//
// NOTE: Because the part is used elsewhere, do
// not save changes when closing it.
//-------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.sldcostingapi;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System;

namespace ThreeDPrintingCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel;
            ModelDocExtension swModelDocExt;
            CostManager swcCostMgr;
            CostPart swcCostPart;
            CostBody swcCostBody;
            CostAnalysis swcCostAnalysis;
            CostAnalysis3dPrinting swc3DPrintAnalysis;
            string fileName;
            int errors = 0;
            int warnings = 0;
            double totalCost;
            string templateName;
            int materialClassCount;
            string[] materialClasses;
            int materialCount;
            string[] materials;
            int i;

            //Open the specified part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\clamp1.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Get CostingManager
            swcCostMgr = (CostManager)swModelDocExt.GetCostingManager();
            if (swcCostMgr == null)
            {
                Debug.Print("CostingManager is nothing.");
                return;
            }

            //Get Costing part
            swcCostPart = (CostPart)swcCostMgr.CostingModel;
            if (swcCostPart == null)
            {
                Debug.Print("Costing part is nothing.");
                return;
            }

            //Set the Costing manufacturing method
            //to 3D printing and get the Costing body
            swcCostBody = (CostBody)swcCostPart.SetCostingMethod("", (int)swcMethodType_e.swcMethodType_3dPrinting);
            if (swcCostBody == null)
            {
                Debug.Print("Costing body is nothing.");
                return;
            }

            Debug.Print("3D printing Costing analysis");
            //Get the common Costing analysis
            swcCostAnalysis = (CostAnalysis)swcCostBody.GetCostAnalysis();
            if (swcCostAnalysis == null)
            {
                Debug.Print("Failed to activate Costing analysis.");
                return;
            }

            //Get the 3D printing Costing analysis
            swc3DPrintAnalysis = (CostAnalysis3dPrinting)swcCostAnalysis.GetSpecificAnalysis();
            if (swc3DPrintAnalysis == null)
            {
                Debug.Print("3D printing Costing analysis is nothing.");
                return;
            }

            //Get the material classes from the Costing template
            materialClassCount = swc3DPrintAnalysis.GetMaterialClassesCount();
            if (materialClassCount == 0)
            {
                Debug.Print("No material classes for this 3D printing Costing analysis.");
                return;
            }

            materialClasses = (string[])swc3DPrintAnalysis.GetMaterialClasses();
            Array.Resize(ref materialClasses, materialClassCount + 1);
            for (i = 0; i <= materialClassCount - 1; i++)
            {
                Debug.Print("  Valid material classes for this 3D printing Costing Analysis: ");
                Debug.Print("    " + materialClasses[i]);
            }

            //Set the material class
            swc3DPrintAnalysis.CurrentMaterialClass = materialClasses[0];
            Debug.Print("  Name of the material class for this 3D printing Costing analysis: " + materialClasses[0]);
            //Get the material names from the Costing template
            templateName = swcCostAnalysis.CostingTemplateName;
            Debug.Print("  Costing template path and file name: " + templateName);
            materialCount = swc3DPrintAnalysis.GetMaterialCount(materialClasses[0]);
            if (materialCount == 0)
            {
                Debug.Print("No materials for this 3D printing Costing Analysis.");
                return;
            }
            Debug.Print("  Number of materials: " + materialCount);
            materials = (string[])swc3DPrintAnalysis.GetMaterials(materialClasses[0]);
            Array.Resize(ref materials, materialCount + 1);
            for (i = 0; i <= materialCount - 1; i++)
            {
                Debug.Print("  Valid materials for this 3D printing Costing Analysis: ");
                Debug.Print("    " + materials[i]);
            }

            //Set the material
            swc3DPrintAnalysis.CurrentMaterial = materials[0];
            Debug.Print("  Name of material for " + materialClasses[0] + " for this 3D printing Costing analysis: " + materials[0]);

            //Set and get 3D printing Costing analysis parameters
            swc3DPrintAnalysis.OrientationPlane = (int)swcPlane_e.swcPlane_XZ;
            swc3DPrintAnalysis.PercentInfill = 80;
            swc3DPrintAnalysis.WallThickness = swc3DPrintAnalysis.WallThickness * 2;
            Debug.Print("  3D printing Costing analysis parameters:");
            Debug.Print("    Orientation plane: " + swc3DPrintAnalysis.OrientationPlane);
            Debug.Print("    Infill percentage: " + swc3DPrintAnalysis.PercentInfill + "%");
            Debug.Print("    Wall thickness: " + swc3DPrintAnalysis.WallThickness + " meters");
            Debug.Print("    Structural material cost: $" + swc3DPrintAnalysis.StructuralMaterialCost);
            //Reset the shop rate to the default
            swc3DPrintAnalysis.ResetShopRate();
            swc3DPrintAnalysis.ShopRateApplied = true;
            Debug.Print("    Default shop rate applied: " + swc3DPrintAnalysis.ShopRateApplied);
            Debug.Print("    Default shop rate: $" + swc3DPrintAnalysis.ShopRate);

            totalCost = swcCostAnalysis.GetTotalCostToManufacture();
            Debug.Print("Total 3D printing cost to manufacture: $" + totalCost);
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
