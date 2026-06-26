---
title: "Create Solid Bodies Using Geometry and Topology Methods Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Solid_Bodies_using_Geometry_and_Topology_APIs_Example_CSharp.htm"
---

# Create Solid Bodies Using Geometry and Topology Methods Example (C#)

This example shows how to create a solid body using SOLIDWORKS geometry and topology methods.

```
//--------------------------------------------------
// Preconditions: Verify that the specified part
// document template exists.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Creates a part containing a single solid
//    body feature that is the union of a box and
//    a cone.
// 3. Examine the graphics area and FeatureManager
//    design tree.
//--------------------------------------------------
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
            Modeler swModeler = default(Modeler);
            Feature swFeat = default(Feature);
            double[] nConeParam = new double[9];
            object vConeArr = null;
            Body2 swConeBody = default(Body2);
            double[] nBoxParam = new double[9];
            object vBoxArr = null;
            Body2 swBoxBody = default(Body2);
            object[] vNewBodyArr = null;
            object vNewBody = null;
            PartDoc swNewPart = default(PartDoc);
            Body2 swNewBody = default(Body2);
            FaultEntity swFaultEnt = default(FaultEntity);
            int nRetVal = 0;
            int nCount = 0;

            // Form cone
            // Face center
            nConeParam[0] = 0.0;
            nConeParam[1] = 0.1;
            nConeParam[2] = 0.0;
            // Axis
            nConeParam[3] = 0.0;
            nConeParam[4] = 0.0;
            nConeParam[5] = 1.0;
            // Base radius
            nConeParam[6] = 0.2;
            // Top radius
            nConeParam[7] = 0.1;
            // Height
            nConeParam[8] = 0.3;
            vConeArr = nConeParam;

            // Form box
            // Face center
            nBoxParam[0] = 0.0;
            nBoxParam[1] = 0.1;
            nBoxParam[2] = 0.2;
            // Axis
            nBoxParam[3] = 0.0;
            nBoxParam[4] = 0.0;
            nBoxParam[5] = 1.0;
            // Width
            nBoxParam[6] = 0.3;
            // Length
            nBoxParam[7] = 0.25;
            //Height
            nBoxParam[8] = 0.4;
            vBoxArr = nBoxParam;

            swModeler = (Modeler)swApp.GetModeler();
            swConeBody = (Body2)swModeler.CreateBodyFromCone((vConeArr));
            swBoxBody = (Body2)swModeler.CreateBodyFromBox((vBoxArr));
            swFaultEnt = (FaultEntity)swConeBody.Check3;
            nCount = swFaultEnt.Count;
            if (nCount != 0)
            {
                Debug.Print("Faulty cone!");
                return;
            }
            swFaultEnt = (FaultEntity)swBoxBody.Check3;
            nCount = swFaultEnt.Count;
            if (nCount != 0)
            {
                Debug.Print("Faulty box!");
                return;
            }
            vNewBodyArr = (object[])swConeBody.Operations2((int)swBodyOperationType_e.SWBODYADD, swBoxBody, out nRetVal);

            swNewPart = (PartDoc)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2014\\templates\\Part.prtdot", 0, 0, 0);
            foreach (object vNewBody_loopVariable in vNewBodyArr)
            {
                vNewBody = vNewBody_loopVariable;
                swNewBody = (Body2)vNewBody;
                // Create solid body feature
                swFeat = (Feature)swNewPart.CreateFeatureFromBody3(swNewBody, false, (int)swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck + (int)swCreateFeatureBodyOpts_e.swCreateFeatureBodySimplify);
            }

            swModel = (ModelDoc2)swNewPart;
            swModel.ViewZoomtofit2();
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
