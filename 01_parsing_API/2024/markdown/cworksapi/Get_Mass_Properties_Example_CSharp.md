---
title: "Get Mass Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Mass_Properties_Example_CSharp.htm"
---

# Get Mass Properties Example (C#)

This example shows how to get the mass properties of a study.

```vb
  //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 //    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 // 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
  //    (in the IDE, click Project > Add Reference > .NET >
 //    SolidWorks.Interop.cosworks > OK).
 // 3. Ensure that the specified file exists.
 // 4. Open the Immediate window.
 //
 // Postconditions: Prints some mass properties of the Ready study to the
 // Immediate window.
 //
  // NOTE: Because the model is used elsewhere, do not save any changes.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.cosworks;
 using System.Runtime.InteropServices;
 namespace GetMassProperties_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 Part;
         CwAddincallback swAddin;
         CosmosWorks ssApp;
         CWModelDoc ssModelDoc;
         CWStudyManager ssStudyMgr;
         CWStudy ssStudy;
         CWMassPropertiesManager massPropMgr;
         string docName;
         int errors;
         int warnings;
         string studyName;
         int studyType;

         object[] comObj;
         object[] moiObj;
         object[] moiocsObj;
         object[] paiObj;
         object[] pmiObj;

         byte[] var1;
         byte[] var2;
         object pDisp1;
         object pDisp2;
         string selection1;

         string selection2;

         public void Main()
         {
             docName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Contact\quartereyebar.sldasm"
             swApp.OpenDoc6(docName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

             Part = (ModelDoc2)swApp.ActiveDoc;

             swAddin = (CwAddincallback)swApp.GetAddInObject("SldWorks.Simulation");
             ssApp = swAddin.CosmosWorks;
             ssModelDoc = ssApp.ActiveDoc;
             ssStudyMgr = ssModelDoc.StudyManager;

             ssStudy = ssStudyMgr.GetStudy(0);
             studyName = ssStudy.Name;
             Debug.Print("Study name: " + studyName);
             studyType = ssStudy.AnalysisType;
             Debug.Print("  Type as defined in swsAnalysisStudyType_e: " + studyType);

             massPropMgr = ssStudy.GetMassPropertiesManager();

             selection1 = "245,35,0,0,4,0,0,0,255,254,255,27,113,0,117,0,97,0,114,0,116,0,101,0,114,0,98,0,111,0,108,0,116,0,45,0,49,0,64,0,113,0,117,0,97,0,114,0,116,0,101,0,114,0,101,0,121,0,101,0,98,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0,1,0,0,0,101,0,0,0";

             StringtoArray(selection1, ref var1);
             pDisp1 = Part.Extension.GetObjectByPersistReference3((var1), out errors);

             selection2 = "245,35,0,0,4,0,0,0,255,254,255,29,113,0,117,0,97,0,114,0,116,0,101,0,114,0,101,0,121,0,101,0,98,0,97,0,114,0,45,0,49,0,64,0,113,0,117,0,97,0,114,0,116,0,101,0,114,0,101,0,121,0,101,0,98,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,9,0,0,0,3,0,0,0,103,0,0,0,102,0,0,0,101,0,0,0";

             StringtoArray(selection2, ref var2);
             pDisp2 = Part.Extension.GetObjectByPersistReference3((var2), out errors);

             object[] varArray = { pDisp1, pDisp2 };

            massPropMgr.SetCoordinateSystemToDefault();
             errors = massPropMgr.AddBodies((varArray));
             comObj = (object[])massPropMgr.GetCenterOfMass();
             moiObj = (object[])massPropMgr.GetMomentOfInertia();
             moiocsObj = (object[])massPropMgr.GetMomentOfInertiaAtOutputCoordinateSystem();
             paiObj = (object[])massPropMgr.GetPrincipalAxesOfInertia();
             pmiObj = (object[])massPropMgr.GetPrincipalMomentOfInertia();

             Debug.Print("  Mass properties:");
             Debug.Print("    Surface area (square meters): " + massPropMgr.Area);
             Debug.Print("    Mass (kilograms): " + massPropMgr.Mass);
             Debug.Print("    Volume (cubic meters): " + massPropMgr.Volume);
             Debug.Print("    Center of mass: ");
             Debug.Print("        x: " + comObj[0]);
             Debug.Print("        y: " + comObj[1]);
             Debug.Print("        z: " + comObj[2]);
             Debug.Print("    Moment of inertia (kilograms * meters squared): ");
             Debug.Print("        lxx: " + moiObj[0]);
             Debug.Print("        lxy: " + moiObj[1]);
             Debug.Print("        lxz: " + moiObj[2]);
             Debug.Print("        lyx: " + moiObj[3]);
             Debug.Print("        lyy: " + moiObj[4]);
             Debug.Print("        lyz: " + moiObj[5]);
             Debug.Print("        lzx: " + moiObj[6]);
             Debug.Print("        lzy: " + moiObj[7]);
             Debug.Print("        lzz: " + moiObj[8]);
             Debug.Print("    Moment of inertia with respect to output coordinate system (kilograms * square meters): ");
             Debug.Print("        lxx: " + moiocsObj[0]);
             Debug.Print("        lxy: " + moiocsObj[1]);
             Debug.Print( "       lxz: " + moiocsObj[2]);
             Debug.Print( "       lyx: " + moiocsObj[3]);
             Debug.Print( "       lyy: " + moiocsObj[4]);
             Debug.Print( "       lyz: " + moiocsObj[5]);
             Debug.Print( "       lzx: " + moiocsObj[6]);
             Debug.Print( "       lzy: " + moiocsObj[7]);
             Debug.Print( "       lzz: " + moiocsObj[8]);
             Debug.Print( "    Coefficients of the principal axes of inertia with respect to center of mass: ");
             Debug.Print( "       Axis1_x: " + paiObj[0]);
             Debug.Print( "       Axis1_y: " + paiObj[1]);
             Debug.Print( "       Axis1_z: " + paiObj[2]);
             Debug.Print( "       Axis2_x: " + paiObj[3]);
             Debug.Print( "       Axis2_y: " + paiObj[4]);
             Debug.Print( "       Axis2_z: " + paiObj[5]);
             Debug.Print( "       Axis3_x: " + paiObj[6]);
             Debug.Print( "       Axis3_y: " + paiObj[7]);
             Debug.Print( "       Axis3_z: " + paiObj[8]);
             Debug.Print( "    Principal moments of inertia with respect to center of mass: ");
             Debug.Print( "       Px: " + pmiObj[0]);
             Debug.Print( "       Py: " + pmiObj[1]);
             Debug.Print("        Pz: " + pmiObj[2]);

         }

         private void StringtoArray(string inputSTR, ref byte[] varEntity)
         {

             string[] PIDArray = null;
             byte[] PID = null;
             int i;

             // Parse string into an array
             PIDArray = inputSTR.Split(new char[] { ',' });

             //Convert string array to byte array
             int sizeArray = PIDArray.Length;

             PID = new byte[sizeArray];

             for (i = 0; i < PIDArray.Length; i++)
             {
                 PID[i] = Convert.ToByte(PIDArray[i]);
             }

             varEntity = PID;
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
