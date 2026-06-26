---
title: "Get Selections for Reference Axis Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Selections_for_Reference_Axis_Feature_Example_CSharp.htm"
---

# Get Selections for Reference Axis Feature Example (C#)

This example shows how to get the selections for a reference axis feature.

```
//-------------------------------------------------
// Preconditions:
// 1. Verify that the document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified document.
// 2. Gets the Axis1 feature.
// 3. Gets the entities that define Axis1.
// 4. Gets the type and name of the entities that define
//    Axis1.
// 5. Examine the Immediate window.
//-------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace IRefAxisFeatureDataGetSelectionCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            PartDoc swPart = default(PartDoc);
            Feature swFeat = default(Feature);
            RefAxisFeatureData swRefAxisFeatureData = default(RefAxisFeatureData);
            Entity swEntity = default(Entity);
            int warnings = 0;
            int errors = 0;
            string fileName = null;
            object[] obj = null;
            object types = null;
            string aType = null;
            string name = null;
            int i = 0;
            int[] entTypes;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\button.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swPart = (PartDoc)swModel;

            swFeat = (Feature)swPart.FeatureByName("Axis1");
            swRefAxisFeatureData = (RefAxisFeatureData)swFeat.GetDefinition();
            swRefAxisFeatureData.AccessSelections(swModel, null);
            obj = (object[])swRefAxisFeatureData.GetSelections(out types);
            swRefAxisFeatureData.ReleaseSelectionAccess();

            entTypes = (int[])types;

            Debug.Print("Entity:");
            Debug.Print("");
            for (i = 0; i < obj.GetLength(0); i++)
            {
                swEntity = (Entity)obj[i];
                swFeat = (Feature)swEntity;
                swEntity.Select(false);
                name = swFeat.GetNameForSelection(out aType);
                Debug.Print("  Type: " + entTypes[i]);
                Debug.Print("  Name: " + name);
                Debug.Print("");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
