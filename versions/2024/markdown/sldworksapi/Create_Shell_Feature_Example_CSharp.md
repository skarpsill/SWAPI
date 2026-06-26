---
title: "Create Shell Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Shell_Feature_Example_CSharp.htm"
---

# Create Shell Feature Example (C#)

This example shows how to create a shell feature.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
  // 1. Verify that the specified model document exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
  // 1. Selects a face to remove from the model to create the shell.
 // 2. Creates Shell1.
  // 3. Inspect the Immediate window, graphics area, and
 //    FeatureManager design tree.
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

 namespace CreateShellFeature_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr swSelMgr;
         SelectData swSelData;
         Feature swFeat;
         ShellFeatureData swShell;
         object[] vFaceRemArr;
         object vFaceRem;
         Face2 swFaceRem;
         object[] vMultiFaceArr;
         object vMultiFace;
         Face2 swMultiFace;
         Entity swEnt;
         int i;
         bool bRet;
         int longstatus;
         int longwarnings;

         public void Main()
 {
 swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block20.sldprt", 1, 0, "", ref longstatus, ref longwarnings);
 swApp.ActivateDoc2("block20", false, ref longstatus);
 swModel = (ModelDoc2)swApp.ActiveDoc;

 bRet = swModel.Extension.SelectByID2("", "FACE", -0.0150558029249623, 0.0396239999999466, -0.018063862472502, false, 1, null, 0);
 swModel.InsertFeatureShell(0.00254, false);

 swSelMgr = (SelectionMgr)swModel.SelectionManager;
 swSelData = swSelMgr.CreateSelectData();
 swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
 swShell = (ShellFeatureData)swFeat.GetDefinition();

 // Get shell data
 Debug.Print("File = " + swModel.GetPathName());
 Debug.Print("  " + swFeat.Name);
 Debug.Print("    Direction: " + swShell.Direction);
 Debug.Print("    Thickness: " + swShell.Thickness * 1000.0 + " mm");
 Debug.Print("    Count of faces removed: " + swShell.FacesRemovedCount);
 Debug.Print("    Count of faces with alternative thicknesses: " + swShell.GetMultipleThicknessFacesCount());

 bRet = swShell.AccessSelections(swModel, null);
 swModel.ClearSelection2(true);

 vFaceRemArr = (object[])swShell.FacesRemoved;

 for (i =0; i< vFaceRemArr.GetLength(0); i++) {
 vFaceRem = vFaceRemArr[i];
 swFaceRem = (Face2)vFaceRem;
 swEnt = (Entity)swFaceRem;

 bRet = swEnt.Select4(true, swSelData);
 }

 swModel.ClearSelection2(true);
 vMultiFaceArr = (object[])swShell.MultipleThicknessFaces;

 foreach (object vMultiFace_loopVariable in vMultiFaceArr) {
 vMultiFace = vMultiFace_loopVariable;
 swMultiFace = (Face2)vMultiFace;
 swEnt = (Entity)swMultiFace;

 Debug.Print("    Alternative thickness in mm at face (" + i + "): " + swShell.GetMultipleThicknessAtIndex(i) * 1000.0);
 i = i + 1;

 bRet = swEnt.Select4(true, swSelData);
 }

 swModel.ClearSelection2(true);
 swShell.ReleaseSelectionAccess();

 }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
