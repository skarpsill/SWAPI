---
title: "Get and Fill Gaps in Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Fill_Gaps_in_Body_Example_CSharp.htm"
---

# Get and Fill Gaps in Body Example (C#)

This example shows how to get and fill the gaps in a body.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Open a model document that contains at least one body
//    with one or more gaps.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Identifies the number of gaps in each
//    body and fills each gap with a fill-surface
//    feature.
// 2. Examine the Immediate window and the FeatureManager
//    design tree.
//---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace DiagnoseResultCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            PartDoc swPart = default(PartDoc);
            object[] vBodyArr = null;
            Body2 swBody = default(Body2);
            int i = 0;
            int length = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swPart = (PartDoc)swModel;
            Debug.Print("File = " + swModel.GetPathName());
            for (i = 0; i <= 5; i++)
            {
                vBodyArr = (object[])swPart.GetBodies2(i, false);
                if ((vBodyArr != null))
                {
                    length = vBodyArr.GetLength(0);
                    Debug.Print("  NumBody[" + i + "] = " + length.ToString());
                    foreach (Body2 vBody in vBodyArr)
                    {
                        swBody = vBody;
                        ProcessBody(swApp, swModel, swBody);
                    }
                }
            }

        }

        public void ProcessBody(SldWorks swApp, ModelDoc2 swModel, Body2 swBody)
        {
            int nRetval1 = 0;
            int nRetval2 = 0;
            DiagnoseResult swDiagnose = default(DiagnoseResult);
            object[] vCoEdgeArr = null;
            CoEdge swCoEdge = default(CoEdge);
            Edge swEdge = default(Edge);
            Entity swEnt = default(Entity);
            SelectionMgr swSelMgr = default(SelectionMgr);
            SelectData swSelData = default(SelectData);
            FeatureManager swFeatMgr = default(FeatureManager);
            Feature swFeat = default(Feature);
            FaultEntity swFaultEnt = default(FaultEntity);
            int nNumGap = 0;
            int i = 0;
            bool bRet = false;

            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swSelData = (SelectData)swSelMgr.CreateSelectData();
            swFeatMgr = (FeatureManager)swModel.FeatureManager;
            swDiagnose = (DiagnoseResult)swBody.Diagnose();
            swFaultEnt = swBody.Check3;
            nRetval1 = swFaultEnt.Count;
            swFaultEnt = swBody.Check3;
            nRetval2 = swFaultEnt.Count;
            swSelData.Mark = 257;
            nNumGap = swDiagnose.GetGapsCount();

            Debug.Print("    Body check1                        = " + nRetval1);
            Debug.Print("      Body check2 (Number of faults)   = " + nRetval2);
            Debug.Print("    Number of gaps                     = " + nNumGap);

            for (i = 1; i <= nNumGap; i++)
            {
                swModel.ClearSelection2(true);
                vCoEdgeArr = (object[])swDiagnose.GetCoEdgesAtGap(i - 1);
                foreach (CoEdge vCoEdge in vCoEdgeArr)
                {
                    swCoEdge = (CoEdge)vCoEdge;
                    swEdge = (Edge)swCoEdge.GetEdge();
                    swEnt = (Entity)swEdge;
                    bRet = swEnt.Select4(true, swSelData);
                }
                swFeat = (Feature)swFeatMgr.InsertFillSurface2(3, (int)swFeatureFillSurfaceOptions_e.swOptimizeSurface, swSelData, (int)swContactType_e.swContact, null, null);
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
