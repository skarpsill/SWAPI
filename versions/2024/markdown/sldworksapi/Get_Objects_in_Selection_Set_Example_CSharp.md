---
title: "Get Objects in Selection Set Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Objects_in_Selection_Set_Example_CSharp.htm"
---

# Get Objects in Selection Set Example (C#)

This example shows how to get the objects in a selection set.

```
//----------------------------------------------------------------------
// Preconditions:
// 1. Verify that the assembly to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the assembly.
// 2. Creates two selection sets.
// 3. Traverses the nodes in the FeatureManager design tree. If the
//    name of the node is Selection-Set1(3), then:
//    a. Gets the type of feature for this node.
//    b. Gets the Selection Sets folder.
//    c. Gets the selection set by name.
//    d. Suspends the current selection list, starts a new selection list,
//       and adds the objects in the selection set to the new selection
//       list.
//    e. Gets the number of objects in the selection list and traverses
//       the selection list.
//       1. Gets the type of object in the selection list.
//       2. Casts the object to a component.
//       3. Gets the name of the component.
//    f. Reinstates the suspended selection list.
// 4. Examine the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//----------------------------------------------------------------------
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
            FeatureManager swFeatureMgr = default(FeatureManager);
            TreeControlItem rootNode = default(TreeControlItem);
            ModelDocExtension swModelDocExtension = default(ModelDocExtension);
            SelectionSet swSelectionSet1 = default(SelectionSet);
            SelectionSet swSelectionSet2 = default(SelectionSet);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\wrench.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            Debug.Print("File = " + swModel.GetPathName());
            swModelDocExtension = (ModelDocExtension)swModel.Extension;

            //Create a selection set
            status = swModelDocExtension.SelectByID2("arm1-1@wrench", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExtension.SelectByID2("arm2-1@wrench", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExtension.SelectByID2("clamp2-1@wrench", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            swSelectionSet1 = (SelectionSet)swModelDocExtension.SaveSelection(out errors);
            swModel.ClearSelection2(true);

            //Create another selection set
            status = swModelDocExtension.SelectByID2("centerlink-1@wrench", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExtension.SelectByID2("screw-1@wrench", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExtension.SelectByID2("screw-1@wrench", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swSelectionSet2 = (SelectionSet)swModelDocExtension.SaveSelection(out errors);
            swModel.ClearSelection2(true);

            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            rootNode = (TreeControlItem)swFeatureMgr.GetFeatureTreeRootItem();
            if ((rootNode != null))
            {
                traverse_node(rootNode, swFeatureMgr, swModel);
            }

        }

        private void traverse_node(TreeControlItem node, FeatureManager swFeatureMgr, ModelDoc2 swModel)
        {
            TreeControlItem childNode = default(TreeControlItem);
            Feature featureNode = default(Feature);
            int nodeObjectType = 0;
            object nodeObject = null;

            nodeObjectType = node.ObjectType;
            nodeObject = (object)node.Object;
            switch (nodeObjectType)
            {
                case (int)swTreeControlItemType_e.swFeatureManagerItem_Feature:
                    if ((nodeObject != null))
                    {
                        featureNode = (Feature)nodeObject;
                        if (featureNode.Name == "Selection-Set1(3)")
                        {
                            Feature swSelectionSetFeature = default(Feature);
                            SelectionSetFolder swSelectionSetFolderFeature = default(SelectionSetFolder);
                            SelectionSet swSelectionSet = default(SelectionSet);
                            Component2 swComponent = default(Component2);
                            SelectionMgr swSelectionMgr = default(SelectionMgr);
                            int nbrSelections = 0;
                            int i = 0;
                            object selObj = null;

                            swSelectionSetFeature = (Feature)node.Object;
                            Debug.Print("Feature name: " + swSelectionSetFeature.Name);
                            Debug.Print("  Feature type: " + swSelectionSetFeature.GetTypeName2());
                            swSelectionSetFolderFeature = (SelectionSetFolder)swFeatureMgr.GetSelectionSetFolder();
                            swSelectionSet = (SelectionSet)swSelectionSetFolderFeature.GetSelectionSetByName(swSelectionSetFeature.Name);
                            Debug.Print("Selection set name: " + swSelectionSet.GetName());

                            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
                            swSelectionMgr.SuspendSelectionList();

                            swSelectionSet.Select();

                            nbrSelections = swSelectionMgr.GetSelectedObjectCount2(-1);
                            Debug.Print("  Number of objects selected in this selection set: " + nbrSelections);
                            for (i = 1; i <= nbrSelections; i++)
                            {
                                //Get each object in the new selection list
                                selObj = (object)swSelectionMgr.GetSelectedObject6(i, -1);
                                Debug.Print("    Object[" + i + "] in the selection list is of swSelectType_e = " + swSelectionMgr.GetSelectedObjectType3(i, -1) + "");
                                //Cast the object
                                swComponent = (Component2)selObj;
                                Debug.Print("       Name of component: " + swComponent.Name2);
                            }
                            swSelectionMgr.ResumeSelectionList();
                        }
                    }
                    break;
                default:
                    break;
            }
            childNode = (TreeControlItem)node.GetFirstChild();
            while ((childNode != null))
            {
                traverse_node(childNode, swFeatureMgr, swModel);
                childNode = (TreeControlItem)childNode.GetNext();
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
