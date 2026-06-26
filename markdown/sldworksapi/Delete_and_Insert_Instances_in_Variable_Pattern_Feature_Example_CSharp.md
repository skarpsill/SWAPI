---
title: "Delete and Insert Instances in Variable Pattern Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_CSharp.htm"
---

# Delete and Insert Instances in Variable Pattern Feature Example (C#)

This example shows how to delete and insert instances in a variable pattern feature.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\api\bottle.sldprt.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Selects the variable pattern feature.
// 2. Rolls back and accesses the variable pattern feature.
//    a. Deletes the last instance of the variable pattern in the table.
//    b. Deletes a dimension in the table.
//    c. Gets the names of the controlling dimensions.
//    d. Inserts a new instance in the table.
//    e. Rolls forward the variable pattern feature.
//       NOTE: It can take several minutes for this step to complete.
// 3. Selects the variable pattern again.
//    a. Rolls back and accesses the variable pattern feature.
//    b. Sets new values for the new instance.
//    c. Rolls forward the variable pattern feature.
// 4. Examine the Immediate window and graphics area.
//
// NOTE: Because the part is used elsewhere, do not save change.
//---------------------------------------------------------------
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
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swFeature = default(Feature);
            DimPatternFeatureData swDimensionDrivenTablePatternFeat = default(DimPatternFeatureData);
            bool status = false;
            string DimensionName = null;
            string errorString = null;
            int i = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            status = swModelDocExt.SelectByID2("VarPattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swDimensionDrivenTablePatternFeat = (DimPatternFeatureData)swFeature.GetDefinition();

            //Roll back and access the variable pattern feature
            status = swDimensionDrivenTablePatternFeat.AccessSelections(swModel, null);

            //Delete the last instance of the variable pattern in the table
            status = swDimensionDrivenTablePatternFeat.DeleteInstanceAt(-1);
            Debug.Print("Last instance of variable pattern deleted from table? " + status);

            //Delete a dimension in the table
            DimensionName = "D3@Fillet1";
            status = swDimensionDrivenTablePatternFeat.DeleteDimension(DimensionName);
            Debug.Print("D3@Fillet1 dimension deleted from table? " + status);

            //Get the names of the controlling dimensions
            int nbr = 0;
            int dimNbr = 0;

            string controllingDimName = null;
            string[] controllingDimNames = null;
            nbr = swDimensionDrivenTablePatternFeat.GetInstanceCount();
            Debug.Print("Number of pattern instances: " + nbr);
            Debug.Print("  Controlling dimension names: ");
            dimNbr = swDimensionDrivenTablePatternFeat.GetControllingDimensionCount();
            controllingDimNames = new string[dimNbr + 1];
            for (i = 0; i < dimNbr; i++)
            {
                controllingDimNames[i] = swDimensionDrivenTablePatternFeat.GetControllingDimensionName(i);
                controllingDimName = controllingDimNames[i];
                Debug.Print("     " + controllingDimName);
            }

            //Insert instance in table
            status = swDimensionDrivenTablePatternFeat.AddInstanceAt(false, -1);
            Debug.Print("Instance added to table? " + status);
            nbr = swDimensionDrivenTablePatternFeat.GetInstanceCount();
            Debug.Print("Number of pattern instances: " + nbr);

            //Roll forward the variable pattern feature
            //NOTE: It can several minutes for this step to complete.
            swFeature.ModifyDefinition(swDimensionDrivenTablePatternFeat, swModel, null);

            //Select the variable pattern again
            status = swModelDocExt.SelectByID2("VarPattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swDimensionDrivenTablePatternFeat = (DimPatternFeatureData)swFeature.GetDefinition();

            //Roll back and access the variable pattern feature
            status = swDimensionDrivenTablePatternFeat.AccessSelections(swModel, null);

            //Set new values for the new instance
            errorString = swDimensionDrivenTablePatternFeat.SetInstanceDimensionValue(nbr, "D3@Sketch2@bottle.moPart_c", 0.15);
            if (string.IsNullOrEmpty(errorString))
            {
                Debug.Print("Set new value for new instance[" + nbr + "] D3@Sketch2 dimension? True");
            }
            else
            {
                Debug.Print("Set new value for new instance[" + nbr + "] D3@Sketch2 dimension? " + errorString);
            }
            errorString = swDimensionDrivenTablePatternFeat.SetInstanceDimensionValue(nbr, "D1@Fillet1@bottle.moPart_c", 0.01);
            if (string.IsNullOrEmpty(errorString))
            {
                Debug.Print("Set new value for new instance[" + nbr + "] D2Fillet2 dimension? True");
            }
            else
            {
                Debug.Print("Set new value for new instance[" + nbr + "] D2Fillet2 dimension? " + errorString);
            }

            //Roll forward the variable pattern feature
            swFeature.ModifyDefinition(swDimensionDrivenTablePatternFeat, swModel, null);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
