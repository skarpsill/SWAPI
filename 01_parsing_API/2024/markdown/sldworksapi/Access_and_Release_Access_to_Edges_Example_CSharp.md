---
title: "Access Edges on Rip Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Access_and_Release_Access_to_Edges_Example_CSharp.htm"
---

# Access Edges on Rip Feature Example (C#)

This example shows how to access edges on a rip feature.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified model document exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified part.
 // 2. Creates Shell1 and Rip1 features.
  // 3. Inspect the FeatureManager design tree, the graphics area, and
 //    the Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save changes.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace InsertRipFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             RipFeatureData swRip = default(RipFeatureData);
             object[] vEdge = null;
             Edge swEdge = default(Edge);
             Entity swEnt = default(Entity);
             int i = 0;
             int lRipDirection = 0;
             bool bRet = false;
             int longstatus = 0;
             int longwarnings = 0;

             lRipDirection = 64;

             swModel = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\box.sldprt", 1, 0, "", ref longstatus, ref longwarnings);
             swApp.ActivateDoc2("box", false, ref longstatus);
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             bRet = swModel.Extension.SelectByID2("", "FACE", -0.0566885410894997, 0.0299999999999159, 0.0200993374069753, false, 1, null, 0);
             swModel.InsertFeatureShell(0.01, false);

             bRet = swModel.Extension.SelectByID2("", "EDGE", 0.0441585455038194, 0.0151990980971277, 0.0459121462268968, true, lRipDirection, null, 0);
             swModel.InsertRip(0.0001);

             bRet = swModel.Extension.SelectByID2("Rip1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);

             // Get rip feature data
             swRip = (RipFeatureData)swFeat.GetDefinition();

             Debug.Print("Gap: " + swRip.Gap * 1000.0 + " mm");

             bRet = swRip.AccessSelections(swModel, null);

             Debug.Print("Number of edges: " + swRip.GetEdgesCount());

             swModel.ClearSelection2(true);

             vEdge = (object[])swRip.Edges;

             for (i = 0; i <= vEdge.GetUpperBound(0); i++)
             {
                 swEdge = (Edge)vEdge[i];
                 swEnt = (Entity)swEdge;

                 Debug.Print("Direction of rip for edge (0=current, 1=other, 2=both): " + swRip.GetDirection(swEdge));

                 bRet = swEnt.Select4(true, null);
             }

             swRip.ReleaseSelectionAccess();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
