---
title: "Suppress Component Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Suppress_Component_Feature_Example_CSharp.htm"
---

# Suppress Component Feature Example (C#)

This example shows how to suppress the selected component feature.

```
//------------------------------------------------
// Preconditions:
// 1. Open an assembly document.
// 2. Select a component feature in the FeatureManager
//    design tree.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Suppresses the selected component feature.
// 2. Prints the names of the assembly and the suppressed
//    component feature to the Immediate window.
// 3. Examine the Immediate window.
//
// NOTE: Editing a component requires that geometry on
// the component to be selected. However, not
// all features are associated with geometry.
// Therefore, it is necessary to select the component
// before attempting to edit the component.
//------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace SelectFeatureCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            AssemblyDoc swAssy = default(AssemblyDoc);
            ModelDoc2 swEditModel = default(ModelDoc2);
            PartDoc swEditPart = default(PartDoc);
            AssemblyDoc swEditAssy = default(AssemblyDoc);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Feature swFeat = default(Feature);
            Component2 swComp = default(Component2);
            string featName = null;
            int status = 0;
            int info = 0;
            bool retVal = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            Debug.Assert((swFeat != null));
            swComp = (Component2)swSelMgr.GetSelectedObjectsComponent2(1);
            Debug.Assert((swComp != null));

            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("    " + swFeat.Name + " <" + swFeat.GetTypeName() + ">");
            Debug.Print("");
            featName = swFeat.Name;
            retVal = swComp.Select2(false, 0);
            Debug.Assert(retVal);
            status = swAssy.EditPart2(true, false, ref info);
            Debug.Assert((int)swEditPartCommandStatus_e.swEditPartSuccessful == status);
            swEditModel = (ModelDoc2)swAssy.GetEditTarget();
            switch (swEditModel.GetType())
            {
                case (int)swDocumentTypes_e.swDocPART:
                    swEditPart = (PartDoc)swEditModel;
                    swFeat = (Feature)swEditPart.FeatureByName(featName);
                    Debug.Assert((swFeat != null));
                    retVal = swFeat.Select2(false, 0);
                    Debug.Assert(retVal);
                    break;
                case (int)swDocumentTypes_e.swDocASSEMBLY:
                    swEditAssy = (AssemblyDoc)swEditModel;
                    swFeat = (Feature)swEditAssy.FeatureByName(featName);
                    Debug.Assert((swFeat != null));
                    retVal = swFeat.Select2(false, 0);
                    Debug.Assert(retVal);
                    break;
                default:
                    Debug.Assert(false);
                    break;
            }
            // Suppress the selected feature
            retVal = swEditModel.EditSuppress2();
            Debug.Assert(retVal);
            swAssy.EditAssembly();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
