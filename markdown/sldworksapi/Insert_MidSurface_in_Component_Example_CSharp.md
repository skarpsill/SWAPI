---
title: "Insert MidSurface in Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_MidSurface_in_Component_Example_CSharp.htm"
---

# Insert MidSurface in Component Example (C#)

This example shows how to insert a midsurface feature in a component.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Open an assembly that contains at least one component
//    that contains a solid body.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Inserts a midsurface feature in the component.
// 2. Gets the number of faces in the midsurface feature.
// 3. Examine the Immediate window.
// 4. Expand the component in the FeatureManager design tree
//    in which the midsurface feature was inserted to
//    verify step 1.
//----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        ModelDocExtension swExt;
        SelectionMgr swSelMgr;
        Component2 swComp;
        AssemblyDoc swAssem;
        FeatureManager featMgr;

        public void Main()
        {
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swExt = (ModelDocExtension)swModel.Extension;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            featMgr = (FeatureManager)swModel.FeatureManager;
            swAssem = (AssemblyDoc)swModel;
            object[] vComponents = null;
            vComponents = (object[])swAssem.GetComponents(true);
            swComp = (Component2)vComponents[0];
            object[] vBodies = null;
            vBodies = (object[])swComp.GetBodies2((int)swBodyType_e.swSolidBody);
            if ((vBodies != null))
            {
                Body2 pBody = default(Body2);
                pBody = (Body2)vBodies[0];
                MidSurface3 midSurf = default(MidSurface3);
                swModel = (ModelDoc2)swComp.GetModelDoc2();
                Debug.Print("Component in which to insert midsurface feature: " + swModel.GetPathName());
                midSurf = (MidSurface3)featMgr.InsertMidSurface(pBody, swModel, 0.5, true);
                Debug.Print("Face count: " + midSurf.GetFaceCount());
            }
            else
            {
                Debug.Print("Open a different assembly in which the specified body is a solid body.");
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
