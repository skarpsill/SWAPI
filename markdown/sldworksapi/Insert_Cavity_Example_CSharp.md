---
title: "Insert Cavity Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cavity_Example_CSharp.htm"
---

# Insert Cavity Example (C#)

This example shows how to insert a cavity in a mold base.

```
//------------------------------------------------------------------------------------
// Preconditions:
// 1. Create a new folder and copy public_documents\samples\tutorial\molds\telephone.sldprt
//    to that folder.
// 2. Click File > New > Part > OK to create a new part document.
//    a. Insert a sketch of a rectangle with a length of 240 mm and width of 350 mm.
//    b. Using the sketch, create a boss extrude feature with a depth of 160 mm.
//    c. Save the part as telephoneMoldBase.sldprt in the folder created in step 1.
// 3. Click File > New > Assembly > OK to create a new assembly document.
//    a. Click telephoneMoldBase in Part/Assembly to Insert in the PropertyManager page.
//    b. Click OK.
//    c. Click Insert Components on the Assembly toolbar, click Browse in
//       Part/Assembly to Insert, click telephone.sldprt located in the folder
//       created in step 1, and click Open.
//    d. Drop telephone.sldprt in the graphics area.
//    e. Click View > Display > Hidden Lines Visible.
//    f. In the FeatureManager design tree, click telephone<1> and click Move Component
//       in the Assembly toolbar.
//    g. Move telephone<1> into the center of telephoneMoldBase<1> and click OK.
//       TIP: Change the view orientation to Top and Front to help center telephone<1>.
//    h. Click File > Save All > Rebuild and save the document (recommended),
//       navigate to the folder created in step 1, type AssemInterim.sldasm in
//       File name, and click Save.
// 4. Click telephoneMoldBase<1> in the FeatureManager design tree.
// 5. Ctrl+click telephone<1> in the FeatureManager design tree.
//
// Postconditions:
// 1. Creates Cavity1 in telphoneMoldBase<1>.
// 2. Expand telephoneMoldBase<1> to verify step 1.
//-----------------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            SelectionMgr swSelMgr = default(SelectionMgr);
            AssemblyDoc swAssy = default(AssemblyDoc);
            Component2 swMoldBaseComp = default(Component2);
            Component2 swCoreComp1 = default(Component2);
            int nRetval = 0;
            int nInfo = 0;
            bool bRet = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;

            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swMoldBaseComp = (Component2)swSelMgr.GetSelectedObjectsComponent2(1);
            swCoreComp1 = (Component2)swSelMgr.GetSelectedObjectsComponent2(2);

            swModel.ClearSelection2(true);

            bRet = swMoldBaseComp.Select2(false, 0);
            nRetval = swAssy.EditPart2(true, true, ref nInfo);
            bRet = swCoreComp1.Select2(true, 0);
            swAssy.InsertCavity4(0.0, 0, 0.0, true, (int)swCavityScaleType_e.swAboutCentroid, 0);
            swAssy.EditAssembly();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
