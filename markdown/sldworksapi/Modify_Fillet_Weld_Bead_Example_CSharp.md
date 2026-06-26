---
title: "Modify Fillet Weld Bead Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Fillet_Weld_Bead_Example_CSharp.htm"
---

# Modify Fillet Weld Bead Example (C#)

This example shows how to modify a fillet weld bead..

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions:
  // 1. Inspect the Immediate window to see the properties of Fillet Bead1.
 // 2. Modifies some properties of Fillet Bead1.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
  //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetWeldBeadFeatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swModelDocExt;
         SelectionMgr swSelMgr;
         WeldmentBeadFeatureData swWeldBead;
         Feature swFeat;
         SelectData swSelData;
         Vertex v1;
         Vertex v2;
         object[] set1;
         object[] faceVar;
         object[] ve;
         object fVar1;
         object fVar2;
         object[] f1 = new object[1];
         object[] f2 = new object[2];
         object[] e = new object[1];
         double bdlen;
         double bdPitch;
         double bdsz;
         int bdTy;
         int i;
         bool boolstatus;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swSelData = swSelMgr.CreateSelectData();

             //Select Fillet Bead1 feature
             boolstatus = swModelDocExt.SelectByID2("Fillet Bead1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swWeldBead = (WeldmentBeadFeatureData)swFeat.GetDefinition();

             //Roll back to the feature just before Fillet Bead1
             boolstatus = swWeldBead.AccessSelections(swModel, null);

             //Get Fillet Bead1 properties
             Debug.Print("Fillet Bead1 properties:");
             bdlen = swWeldBead.get_BeadLength((int)swWeldBeadSide_e.swWeldBeadArrowSide);
             Debug.Print("  Weld bead length: " + bdlen);

             bdPitch = swWeldBead.get_BeadPitch((int)swWeldBeadSide_e.swWeldBeadArrowSide);
             Debug.Print("  Weld bead pitch: " + bdPitch);

             bdsz = swWeldBead.get_BeadSize((int)swWeldBeadSide_e.swWeldBeadArrowSide);
             Debug.Print("  Weld bead size: " + bdsz);

             bdTy = swWeldBead.get_BeadType((int)swWeldBeadSide_e.swWeldBeadArrowSide);
             Debug.Print("  Weld bead type as defined in swWeldBeadType_e: " + bdTy);

             Debug.Print("  Propagate the weld bead along the tangent? " + swWeldBead.TangentPropagation);
             Debug.Print("  Apply weld bead to both sides of intersecting faces? " + swWeldBead.UseOtherSide);

             //Get Fillet Bead1 faces
             swWeldBead.GetFaces((int)swWeldBeadSide_e.swWeldBeadArrowSide, out fVar1, out fVar2);
             faceVar = (object[])fVar2;
             set1 = (object[])fVar1;

             for (i = faceVar.GetLowerBound(0); i <= faceVar.GetUpperBound(0); i++)
             {
                 ((Entity)faceVar[i]).Select4(true, swSelData);
             }

             for (i = set1.GetLowerBound(0); i <= set1.GetUpperBound(0); i++)
             {
                 ((Entity)set1[i]).Select4(true, swSelData);
             }

             //Get Fillet Bead1 virtual edges
             ve = (object[])swWeldBead.GetVirtualEdges(false, (int)swWeldBeadSide_e.swWeldBeadArrowSide);

             for (i = ve.GetLowerBound(0); i <= ve.GetUpperBound(0); i++)
             {
                 boolstatus = ((Entity)ve[i]).Select4(true, swSelData);
                 v1 = (Vertex)((Edge)ve[i]).GetStartVertex();
                 v2 = (Vertex)((Edge)ve[i]).GetEndVertex();
             }

             swModel.ClearSelection2(true);

             //Set new properties of Fillet Bead1
             swWeldBead.set_BeadLength((int)swWeldBeadSide_e.swWeldBeadArrowSide, bdlen * 0.5);
             swWeldBead.set_BeadPitch((int)swWeldBeadSide_e.swWeldBeadArrowSide, bdPitch * 0.5);
             swWeldBead.set_BeadSize((int)swWeldBeadSide_e.swWeldBeadArrowSide, bdsz * 0.5);
             swWeldBead.set_BeadType((int)swWeldBeadSide_e.swWeldBeadArrowSide, bdTy);

             //Modify Fillet Bead1
             boolstatus = swFeat.ModifyDefinition(swWeldBead, swModel, null);

         }

         public SldWorks swApp;

     }

 }
```
