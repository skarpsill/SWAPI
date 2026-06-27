---
title: "Insert Basic Dimension Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Basic_Dimension_Example_CSharp.htm"
---

# Insert Basic Dimension Example (C#)

This example shows how to insert a DimXpert distance-between dimension.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Ensure that the part to open exists.
 // 2. Reference the SOLIDWORKS DimXpert interop assembly:
  //    a. Right-click the project in Project Explorer.
 //    b. Click Add Reference.
 //    c. Click the Browse tab.
 //    d. Select install_dir\api\redist\swdimxpert.dll.
 //
 // Postconditions: Inspect the graphics view and the DimXpertManager pane.
 //
  // NOTE: Because the part is used elsewhere, do not save any changes.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swdimxpert;
 using System.Runtime.InteropServices;
 namespace InsertBasicDimension_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         Configuration swConfig;
         DimXpertManager swDimXPertMgr;
         DimXpertPart swDimXPertPart;
         DimXpertDimensionOption swDimXPertDimOpt;
         object[] dblDimXPertTextPos = new object[3];
         object[] varDimXPertTextPos;
         bool boolstatus;
         int status;
         int warnings;

         public void Main()
         {
             Part = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2017\\Simulation Examples\\actuator_casing.sldprt", 1, 0, "", ref status, ref warnings);
             swApp.ActivateDoc2("actuator_casing.sldprt", false, ref longstatus);
             Part = (ModelDoc2)swApp.ActiveDoc;

             Part.ShowNamedView2("*Isometric", 7);

             swConfig = Part.ConfigurationManager.ActiveConfiguration;
             swDimXPertMgr = Part.Extension.get_DimXpertManager(swConfig.Name, true);
             swDimXPertPart = (DimXpertPart)swDimXPertMgr.DimXpertPart;
             swDimXPertDimOpt = swDimXPertPart.GetDimOption();
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0832566935649766, 0.0141096473029049, 0.0143449005094567, false, 0, null, 0);
             boolstatus = Part.Extension.SelectByID2("", "FACE", 0.0751728497303361, 0.000895850622406916, 0.0190499999998792, true, 0, null, 0);
             dblDimXPertTextPos[0] = 0.083208;
             dblDimXPertTextPos[1] = 0.045464;
             dblDimXPertTextPos[2] = 0.019052;
             varDimXPertTextPos = dblDimXPertTextPos;
             swDimXPertDimOpt.TextPosition = varDimXPertTextPos;
             boolstatus = swDimXPertPart.InsertBasicDimension(swDimXPertDimOpt);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
