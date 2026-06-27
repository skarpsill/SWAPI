---
title: "Get Mass Properties of Visible and Hidden Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_of_Visible_and_Hidden_Components_Example_CSharp.htm"
---

# Get Mass Properties of Visible and Hidden Components Example (C#)

This example shows how to get the mass properties for:

- visible and hidden components in an assembly.
- only the visible components in an assembly.

```vb
 //----------------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\routing-pipes\ball valve with flanges.sldasm.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets the mass properties of all components.
 // 2. Hides the slip on weld flange<1> component.
  // 3. Gets the mass properties of the visible components only.
 // 4. Examine the Immediate window.
 //
  // NOTE: Because this assembly is used elsewhere, do not save changes.
  //---------------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;

 namespace IncludeMassPropertiesOfHiddenBodiesModelDocExtCSharp.csproj
 {
     partial class SolidWorksMacro
     {
         public void Main()
         {
             ModelDoc2 swModel;
             ModelDocExtension swModelDocExt;
             int massStatus = 0;
             double[] massProperties;
             bool boolstatus;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;

             Debug.Print("-------------------------------");
             Debug.Print("Mass properties of visible and hidden components:");
             massProperties = (double[])swModelDocExt.GetMassProperties(1, ref massStatus);
             if ((massProperties != null))
             {
                 Debug.Print(" CenterOfMassX = " + massProperties[0]);
                 Debug.Print(" CenterOfMassY = " + massProperties[1]);
                 Debug.Print(" CenterOfMassZ = " + massProperties[2]);
                 Debug.Print(" Volume = " + massProperties[3]);
                 Debug.Print(" Area = " + massProperties[4]);
                 Debug.Print(" Mass = " + massProperties[5]);
                 Debug.Print(" MomXX = " + massProperties[6]);
                 Debug.Print(" MomYY = " + massProperties[7]);
                 Debug.Print(" MomZZ = " + massProperties[8]);
                 Debug.Print(" MomXY = " + massProperties[9]);
                 Debug.Print(" MomZX = " + massProperties[10]);
                 Debug.Print(" MomYZ = " + massProperties[11]);
             }

             Debug.Print("-------------------------------");

             // Now hide another component
             boolstatus = swModelDocExt.SelectByID2("slip on weld flange-1@ball valve with flanges", "COMPONENT", 0, 0, 0, false, 0, null, 0);
             swModel.HideComponent2();

             Debug.Print("Mass properties of visible components only:");
             swModelDocExt.IncludeMassPropertiesOfHiddenBodies = false;
             massProperties = (double[])swModelDocExt.GetMassProperties(1, ref massStatus);
             if ((massProperties != null))
             {
                 Debug.Print(" CenterOfMassX = " + massProperties[0]);
                 Debug.Print(" CenterOfMassY = " + massProperties[1]);
                 Debug.Print(" CenterOfMassZ = " + massProperties[2]);
                 Debug.Print(" Volume = " + massProperties[3]);
                 Debug.Print(" Area = " + massProperties[4]);
                 Debug.Print(" Mass = " + massProperties[5]);
                 Debug.Print(" MomXX = " + massProperties[6]);
                 Debug.Print(" MomYY = " + massProperties[7]);
                 Debug.Print(" MomZZ = " + massProperties[8]);
                 Debug.Print(" MomXY = " + massProperties[9]);
                 Debug.Print(" MomZX = " + massProperties[10]);
                 Debug.Print(" MomYZ = " + massProperties[11]);
             }
             Debug.Print("-------------------------------");

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;

     }
 }
```
