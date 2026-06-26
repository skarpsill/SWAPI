---
title: "Insert Join Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Join_Feature_Example_CSharp.htm"
---

# Insert Join Feature Example (C#)

This example shows how to insert a join feature.

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document to open exists.
// 2. Verify that c:\temp exists.
// 3. Verify that c:\temp\Part1^arm2.sldprt does not exist. If it does,
//    delete or drag it to a different folder.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Edits the assembly, selects a face, and inserts a new part.
// 3. Selects the components for the join feature and inserts a
//    join feature, which is a feature of Part1^arm2<1> in the
//    the FeatureManager design tree.
// 4. Accesses the join feature
// 5. Gets the number of joined components.
// 6. Iterates through the components, prints the name of
//    each component, and, if an Inplace mate, prints
//    its mate component names and Inplace mate types.
// 7. Examine the Immediate window, FeatureManager design tree, and
//    the graphics area.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//--------------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace JoinFeatureDataCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {

            AssemblyDoc swAssemblyDoc = default(AssemblyDoc);
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Face2 swFace = default(Face2);
            SketchManager swSketchManager = default(SketchManager);
            Feature swFeature = default(Feature);
            JoinFeatureData swJoinFeatureData = default(JoinFeatureData);
            object swSelObj = null;
            string fileName = null;
            bool status = false;
            int errors = 0;
            int warnings = 0;
            int info = 0;
            int state = 0;
            Component2 swComponent = null;
            object singleComponent = null;
            object[] components = null;
            object[] mates = null;
            object singleMate = null;
            Mate2 swMate = null;
            MateInPlace swMateInPlace = null;
            int numMateEntities = 0;
            int typeOfMate = 0;
            int i = 0;

            //Open assembly document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\arm2.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swAssemblyDoc = (AssemblyDoc)swModel;

            //Edit the assembly, select a face, and insert a new part
            swAssemblyDoc.EditPart2(true, false, ref info);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("", "FACE", 0.0102799485791252, 0.00285108269579837, -0.00454660000001184, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swFace = (Face2)swSelectionMgr.GetSelectedObject6(1, -1);
            swSelObj = (object)swFace;
            state = swAssemblyDoc.InsertNewPart2("C:\\temp\\Part1^arm2.sldprt", swSelObj);
            swSketchManager = (SketchManager)swModel.SketchManager;
            swSketchManager.InsertSketch(true);
            swModel.EditUndo2(1);

            //Select the components for the join feature and insert a join feature
            status = swModelDocExt.SelectByID2("secondGrip-1@arm2", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("pincap-1@arm2", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("pincap-4@arm2", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("pincap-5@arm2", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swModelDocExt.SelectByID2("pincap-6@arm2", "COMPONENT", 0, 0, 0, true, 0, null, 0);
            status = swAssemblyDoc.InsertJoin2(true, false);
            swModel.ClearSelection2(true);
            status = swModelDocExt.SelectByID2("Join1@Part1^arm2-1@arm2", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);

            //Access the join feature, which is a feature of Part1^arm2<1> in the
            //the FeatureManager design tree
            swFeature = (Feature)swSelectionMgr.GetSelectedObject6(1, -1);
            swJoinFeatureData = (JoinFeatureData)swFeature.GetDefinition();
            swJoinFeatureData.AccessSelections(swModel, null);

            //Get the number of joined components
            Debug.Print("Number of joined components: " + swJoinFeatureData.GetJoinedPartsCount());

            swFeature.ReleaseSelectionAccess();
```

```
           Debug.Print("");

           //Get components
           components = (object[])swAssemblyDoc.GetComponents(false);
           foreach (Object singleComponent in components)
           {
                swComponent = (Component2)singleComponent;
                //Print name of component
                Debug.Print("Name of component: " + swComponent.Name2);
                //Get mates
                mates = (Object[])swComponent.GetMates();
                if ((mates != null))
                {
                    foreach (Object singleMate in mates)
                    {
                        //Get mate type
                        if (singleMate is Mate2)
                        {
                            swMate = (Mate2)singleMate;
                            typeOfMate = swMate.Type;
                        }
                        //If Inplace mate, print mate component name and Inplace mate type
                        if (singleMate is MateInPlace)
                        {
                            swMateInPlace = (MateInPlace)singleMate;
                            numMateEntities = swMateInPlace.GetMateEntityCount();
                            for (i = 0; i <= numMateEntities - 1; i++)
                            {
                                Debug.Print(" Mate component name: " + swMateInPlace.get_MateComponentName(i));
                                Debug.Print(" Type of Inplace mate: " + swMateInPlace.get_MateEntityType(i));
                            }
                        }
                    }
                }
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
