---
title: "Get Dispatch Objects for Selection Set Items Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Dispatch_Objects_for_Selection_Set_Items_Example_CSharp.htm"
---

# Get Dispatch Objects for Selection Set Items Example (C#)

This example shows how to get the Dispatch objects for selection set items.

```
//-------------------------------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Selects two faces and creates a selection set.
// 3. Selects two edges and creates a selection set.
// 4. Traverses the FeatureManager design tree. If the feature is the
//    Selection Sets folder, then:
//    a. Gets its name.
//    b. Gets each selection set in the Selection Sets folder.
//       1. Gets the selection set items and their types.
//       2. Gets the Dispatch object for each selection set item.
//       3. Gets the name of the body for each selection set item.
// 5. Examine the Immediate window and FeatureManager design tree.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//-------------------------------------------------------------------
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
            SelectionSet swSelectionSet1 = default(SelectionSet);
            SelectionSet swSelectionSet2 = default(SelectionSet);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Create a selection set
            status = swModelDocExt.SelectByID2("", "FACE", -0.0232252739277783, -0.0248041260152831, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", -0.0258449612883283, -0.00628596853454155, -0.00749999999999318, true, 0, null, 0);
            swSelectionSet1 = (SelectionSet)swModelDocExt.SaveSelection(out errors);
            Debug.Print("  First selection set created (1 = succeeded; 0 = failed)? " + errors);
            swModel.ClearSelection2(true);

            //Create another selection set
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0297500073491506, -0.00696186204362448, -0.0073680822854385, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "EDGE", 0.0299025466658236, -0.0199243068692567, -0.0036983143110092, true, 0, null, 0);
            swSelectionSet2 = (SelectionSet)swModelDocExt.SaveSelection(out errors);
            Debug.Print("  Second selection set created (1 = succeeded; 0 = failed)? " + errors);
            swModel.ClearSelection2(true);

            //Traverse the model to get Selection Sets folder
            TraverseModelFeatures(swModel);

        }

        public void TraverseFeatureFeatures(Feature swFeat, ModelDoc2 swModel)
        {
            SelectionSetFolder swSelectionSetFolder = default(SelectionSetFolder);
            object[] selectionSetArray = null;
            object[] selectionSetItemArray = null;
            int[] selectionSetItemArrayTypes = null;
            SelectionSet swSelectionSet = default(SelectionSet);
            SelectionSetItem swSelectionSetItem = default(SelectionSetItem);
            Face2 swFace = default(Face2);
            Edge swEdge = default(Edge);
            Body2 swBody = default(Body2);
            int i = 0;
            int j = 0;
            int selectionSetItemArrayType = 0;

            while ((swFeat != null))
            {
                if (swFeat.Name == "Selection Sets")
                {
                    Debug.Print("    " + swFeat.Name + " [" + swFeat.GetTypeName() + "]");
                    //Get Selection Sets folder
                    swSelectionSetFolder = (SelectionSetFolder)swFeat.GetSpecificFeature2();
                    //Get selection sets in Selection Sets folder
                    selectionSetArray = (object[])swSelectionSetFolder.GetSelectionSets();
                    for (i = 0; i < selectionSetArray.GetLength(0); i++)
                    {
                        swSelectionSet = (SelectionSet)selectionSetArray[i];
                        Debug.Print("      Selection set[" + i + "] name: " + swSelectionSet.GetName());
                        //Get the items and their types in this selection set
                        selectionSetItemArray = (object[])swSelectionSet.GetSelectionSetItems();
                        selectionSetItemArrayTypes = (int[])swSelectionSet.GetSelectionSetItemTypes();
                        for (j = 0; j < selectionSetItemArray.GetLength(0); j++)
                        {
                            swSelectionSetItem = (SelectionSetItem)selectionSetItemArray[j];
                            selectionSetItemArrayType = (int)selectionSetItemArrayTypes[j];
                            switch (selectionSetItemArrayType)
                            {
                                case (int)swSelectType_e.swSelFACES:
                                    //Get the Dispatch object for the selection set item
                                    swFace = (Face2)swSelectionSetItem.GetCorrespondingItem();
                                    //Get the name of the body for the face
                                    swBody = (Body2)swFace.GetBody();
                                    Debug.Print("        Name of face[" + j + "]'s body: " + swBody.Name);
                                    break;
                                case (int)swSelectType_e.swSelEDGES:
                                    //Get the Dispatch object for the selection set item
                                    swEdge = (Edge)swSelectionSetItem.GetCorrespondingItem();
                                    //Get the name of the body for the edge
                                    swBody = (Body2)swEdge.GetBody();
                                    Debug.Print("        Name of edge[" + j + "]'s body: " + swBody.Name);
                                    break;
                            }
                        }
                    }
                }
                swFeat = (Feature)swFeat.GetNextFeature();
            }
        }

        public void TraverseModelFeatures(ModelDoc2 swModel)
        {
            Feature swFeat = default(Feature);
            swFeat = (Feature)swModel.FirstFeature();
            TraverseFeatureFeatures(swFeat, swModel);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
