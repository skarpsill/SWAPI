---
title: "Check Edges for Faults Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Check_Edges_for_Faults_Example_CSharp.htm"
---

# Check Edges for Faults Example (C#)

This example shows how to check the edges in a part for faults.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Open a part document.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Checks the bodies and edges in the part.
// 2. Examine the Immediate window.
//-----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetEdgesCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            PartDoc swPart = default(PartDoc);
            object[] vBodyArr = null;
            object vBody = null;
            Body2 swBody = default(Body2);
            int nRetval1 = 0;
            int nRetval2 = 0;
            object[] vEdgeArr = null;
            object vEdge = null;
            Edge swEdge = default(Edge);
            FaultEntity swFaultEnt = default(FaultEntity);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swPart = (PartDoc)swModel;
            Debug.Print("File = " + swModel.GetPathName());
            vBodyArr = (object[])swPart.GetBodies2((int)swBodyType_e.swAllBodies, true);
            Debug.Assert((vBodyArr != null));
            foreach (object vBody_loopVariable in vBodyArr)
            {
                vBody = vBody_loopVariable;
                swBody = (Body2)vBody;
                Debug.Print("  Body[" + swBody.GetType() + "] --> " + swBody.GetSelectionId());
                nRetval1 = swBody.Check(); // Obsolete method
                nRetval2 = swBody.Check2(); // Obsolete method
                Debug.Print("    IBody2::Check (1 if valid; 0 if not) = " + nRetval1);
                Debug.Print("    IBody2::Check2(Number of faults) = " + nRetval2);
                vEdgeArr = (object[])swBody.GetEdges();
                if ((vEdgeArr != null))
                {
                    foreach (Object vEdge_loopVariable in vEdgeArr)
                    {
                        vEdge = vEdge_loopVariable;
                        swEdge = (Edge)vEdge;
                        swFaultEnt = swEdge.Check;
                        ProcessFaultEntity(swApp, swModel, swEdge, swFaultEnt);
                    }
                }
                else
                {
                    Debug.Print("      No edges in part.");
                }
            }

        }

        public string GetStringFromID(SldWorks swApp, ModelDoc2 swModel, byte[] vPIDarr)
        {
            string functionReturnValue = null;
            byte vPID;
            functionReturnValue = "";
            foreach (object vPID_loopVariable in vPIDarr)
            {
                vPID = (byte)vPID_loopVariable;
                functionReturnValue = functionReturnValue + vPID.ToString("###000");
            }
            return functionReturnValue;
        }

        public void ProcessFaultEntity(SldWorks swApp, ModelDoc2 swModel, Edge swEdge, FaultEntity swFaultEnt)
        {
            ModelDocExtension swModExt = default(ModelDocExtension);
            byte[] vPIDarr = null;
            int nCount = 0;
            Entity swEnt = default(Entity);
            bool bRet = false;
            int i = 0;

            nCount = swFaultEnt.Count;
            // For each edge, print:
            // * no fault found, if no fault found
            // * edge ID and error code, if fault found
            if (0 == nCount)
            {
                Debug.Print("      No fault in edge.");
                return;
            }

            swModExt = (ModelDocExtension)swModel.Extension;
            vPIDarr = (byte[])swModExt.GetPersistReference3(swEdge);
            Debug.Assert((vPIDarr != null));
            Debug.Print("    Edge ID = " + GetStringFromID(swApp, swModel, vPIDarr));
            for (i = 0; i <= nCount - 1; i++)
            {
                swEnt = (Entity)swFaultEnt.get_Entity(i);
                if ((swEnt != null))
                {
                    bRet = swEnt.Select4(true, null);
                    Debug.Assert(bRet);
                }
                Debug.Print("      Fault[" + i + "]                         = " + swFaultEnt.get_ErrorCode(i));
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
