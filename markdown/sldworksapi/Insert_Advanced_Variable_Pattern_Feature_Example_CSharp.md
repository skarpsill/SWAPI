---
title: "Insert Variable Pattern Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm"
---

# Insert Variable Pattern Feature Example (C#)

This example shows how to insert a variable pattern feature.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part to open exists.
// 2. Verify that c:\temp exists.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Inserts a variable pattern feature.
// 2. Exports the table to a Microsoft Excel file.
// 3. Examine the graphics area, Immediate window, and c:\temp.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------------------------
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
            DimPatternFeatureData swDimensionDrivenTablePatternFeat = default(DimPatternFeatureData);
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            int nbr = 0;
            int dimNbr = 0;
            int i = 0;
            int j = 0;
            string[] controllingDimNames = null;
            string controllingDimName = null;
            string instanceName = null;
            string[] instanceNames = null;
            string patternName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\api\\cstick.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Select feature to pattern
            status = swModelDocExt.SelectByID2("Sweep1", "BODYFEATURE", 0, 0, 0, false, 4, null, 0);

            //Select reference geometry to drive seed feature
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, true, 1048576, null, 0);

            //Populate table
            swFeatureManager = (FeatureManager)swModel.FeatureManager;
            status = swFeatureManager.InsertVaryInstanceOverride("D1@Sketch2@cstick.SLDPRT", 256, 1, 0, 1, 0, 0.085);
            status = swFeatureManager.InsertVaryInstanceOverride("D3@Sketch2@cstick.SLDPRT", 256, 1, 0, 1, 0, 0.04);
            status = swFeatureManager.InsertVaryInstanceOverride("D4@Sketch2@cstick.SLDPRT", 256, 1, 0, 1, 0, 0.03);
            status = swFeatureManager.InsertVaryInstanceOverride("D1@Sketch2@cstick.SLDPRT", 256, 1, 0, 2, 0, 0.105);
            status = swFeatureManager.InsertVaryInstanceOverride("D3@Sketch2@cstick.SLDPRT", 256, 1, 0, 2, 0, 0.06);
            status = swFeatureManager.InsertVaryInstanceOverride("D4@Sketch2@cstick.SLDPRT", 256, 1, 0, 2, 0, 0.05);
```

```
            //Insert the variable pattern feature
            //and access its feature data
            swDimensionDrivenTablePatternFeat = (DimPatternFeatureData)swFeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmDimPattern);
            swFeature = (Feature)swFeatureManager.CreateFeature(swDimensionDrivenTablePatternFeat);
            swDimensionDrivenTablePatternFeat = (DimPatternFeatureData)swFeature.GetDefinition();
            status = swDimensionDrivenTablePatternFeat.AccessSelections(swModel, null);

            nbr = swDimensionDrivenTablePatternFeat.GetInstanceCount();
            Debug.Print("Number of pattern instances: " + nbr);
```

```
            dimNbr = swDimensionDrivenTablePatternFeat.GetControllingDimensionCount();
            Debug.Print("Number of controlling dimensions: " + dimNbr);
            Debug.Print("  Controlling dimension names: ");
            controllingDimNames = new string[dimNbr + 1];
            for (i = 0; i < dimNbr; i++)
            {
                controllingDimNames[i] = swDimensionDrivenTablePatternFeat.GetControllingDimensionName(i);
                controllingDimName = controllingDimNames[i];
                Debug.Print("     " + controllingDimName);
            }

            Debug.Print("Names of pattern instances:");
            instanceNames = new string[nbr];
            j = 0;
            for (i = 1; i <= nbr; i++)
            {
                instanceName = swDimensionDrivenTablePatternFeat.GetInstanceNameByIndex(i);
                Debug.Print("  " + instanceName);
                instanceNames[j] = instanceName;
                j = j + 1;
            }

            Debug.Print("Table row indices of pattern instances:");
            for (i = 0; i <= nbr - 1; i++)
            {
                Debug.Print("  " + swDimensionDrivenTablePatternFeat.GetTableRowIndex(instanceNames[i]) + ": " + instanceNames[i]);
            }

            Debug.Print("Pattern dimension names: ");
            for (i = 0; i < nbr; i++)
            {
                for (j = 1; j < dimNbr; i++)
                {
                   patternName = swDimensionDrivenTablePatternFeat.GetInstanceDimensionName(instanceNames[i], controllingDimNames[j]);
                   Debug.Print("  " + patternName + ": " + instanceNames[i] + ": Controlling dimension name: " + swDimensionDrivenTablePatternFeat.GetControllingDimensionName(j));
                }
            }

            Debug.Print("Pattern instance suppression state:");
            for (i = 0; i <= nbr - 1; i++)
            {
                Debug.Print("  " + swDimensionDrivenTablePatternFeat.GetInstanceSuppressStateByIndex(swDimensionDrivenTablePatternFeat.GetTableRowIndex(instanceNames[i])) + ": " + instanceNames[i]);
            }
```

```
            //Export table to Microsoft Excel file
            errors = swDimensionDrivenTablePatternFeat.ExportToExcel("c:\\temp\\cstickVarPattern.xls", true);
            Debug.Print ("Table exported to Microsoft Excel file (0 = Succeeded)? " + errors);

            swDimensionDrivenTablePatternFeat.ReleaseSelectionAccess();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
