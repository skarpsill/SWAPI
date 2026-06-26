---
title: "Detect Interferences Using a Transform Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Detect_Interferences_Using_a_Transform_Example_CSharp.htm"
---

# Detect Interferences Using a Transform Example (C#)

This example shows how to specify a transform to detect interferences.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\api\InterferenceAssem.sldasm.
 // 2. Uncomment one of the userOpt assignments.
 //
 // Postconditions:
 // 1. When the macro stops, observe the position of the components in the
 //    graphics area.
 // 2. Press F5 to continue.
 // 3. Inspect the Immediate Window for interfering components.
 //
 // NOTE: Because the model is used elsewhere,
 // do not save changes when closing it.
 // ---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace IntDet_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swDoc;
         AssemblyDoc swADoc;
         SelectionMgr swSM;
         InterferenceDetectionMgr swIDM;
         Component2[] swComp;
         Component2 comp;
         Object[] varComp;
         int numOfComp;
         MathTransform[] swCompTrans;
         Object[] varCompTrans;
         bool isInterfering;
         object outcomp;
         Object[] outIntComp;
         double gposX;
         double gposY;
         int I;

         // Uncomment one of the following lines to transform the components
         //int userOpt = 0; //make components coincident
         int userOpt = 1; //make components intersecting

         public void Main()
         {
             swDoc = (ModelDoc2)swApp.ActiveDoc;
             swADoc = (AssemblyDoc)swDoc;
             swSM = (SelectionMgr)swDoc.SelectionManager;
             SetPosAsPerOption();
             SelectAllComponent();
             isInterfering = false;
             numOfComp = swSM.GetSelectedObjectCount();

             if ((numOfComp > 0))
             {
                 getSelectedComp();
                 PrintComponentName(varComp);
                 CreateSameTransMatAsCompCount();
                 ChangePosOfCompAsPerOption();

                 varCompTrans = swCompTrans;

                 swIDM = swADoc.InterferenceDetectionManager;
                 swIDM.TreatCoincidenceAsInterference =  true;
                 isInterfering = swIDM.GetComponentsTransformInterference((varComp), (varCompTrans), out (outcomp));

                 outIntComp = (object[])outcomp;

                 // Observe transformation of objects for interference detection
                 System.Diagnostics.Debugger.Break();

                 swIDM.Done(); // Interference detection finished

                 PrintInterferenceInfo();
                 varComp = null;
             }
             else
             {
                 System.Windows.Forms.MessageBox.Show("Select components");
             }

         }
         public void SetPosAsPerOption()
         {
             if (userOpt == 0)
             {
                 gposX = 100.0 / 1000.0;
                 gposY = -50.0 / 1000.0;
             }
             else
             {
                 gposX = 70.0 / 1000.0;
                 gposY = -50.0 / 1000.0;
             }
         }
         public void SelectAllComponent()
         {
             bool boolstatus = false;
             boolstatus = swDoc.Extension.SelectByID2("SquarePad_Red-1@InterferenceAssem", "COMPONENT", 0, 0, 0, false, 0, null, 0);
             boolstatus = swDoc.Extension.SelectByID2("SquarePad_Green-1@InterferenceAssem", "COMPONENT", 0, 0, 0, true, 0, null, 0);
             boolstatus = swDoc.Extension.SelectByID2("SquarePad_Blue-1@InterferenceAssem", "COMPONENT", 0, 0, 0, true, 0, null, 0);
             boolstatus = swDoc.Extension.SelectByID2("SquarePad_Orange-1@InterferenceAssem", "COMPONENT", 0, 0, 0, true, 0, null, 0);
             boolstatus = swDoc.Extension.SelectByID2("SquarePad_SkyBlue-1@InterferenceAssem", "COMPONENT", 0, 0, 0, true, 0, null, 0);
             boolstatus = swDoc.Extension.SelectByID2("SquarePad_Yellow-1@InterferenceAssem", "COMPONENT", 0, 0, 0, true, 0, null, 0);
             boolstatus = swDoc.Extension.SelectByID2("SquarePad_Pink-1@InterferenceAssem", "COMPONENT", 0, 0, 0, true, 0, null, 0);
         }
         public void PrintInterferenceInfo()
         {
             if ((isInterfering))
             {
                 Debug.Print("Interfering components:");
                 Debug.Print("");
                 for (I = 0; I <= outIntComp.GetUpperBound(0); I++)
                 {
                     Component2 swOutComp = default(Component2);
                     swOutComp = (Component2)outIntComp[I];
                     Debug.Print(swOutComp.Name2);
                     swOutComp.Select4(true, null, false);
                     swOutComp = null;
                 }
             }
             else
             {
                 Debug.Print("No interference");
             }
         }
         public void getSelectedComp()
         {
             swComp = new Component2[numOfComp];
             for (I = 1; I <= numOfComp; I++)
             {
                 swComp[I-1] = (Component2)swSM.GetSelectedObject6(I, -1);
             }
             varComp = swComp;
         }
         public void PrintComponentName(Object[] varComp)
         {
             if (!((varComp == null)))
             {
                 if (userOpt == 0)
                 {
                     Debug.Print("Detect interferences between coincident components:");
                     Debug.Print("");
                 }
                 else
                 {
                     Debug.Print("Detect interferences between intersecting components:");
                     Debug.Print("");
                 }

                 for (I = 0; I <= varComp.GetUpperBound(0); I++)
                 {
                     comp = default(Component2);
                     comp = (Component2)varComp[I];

                     Debug.Print("Component name : " + comp.Name2);
                     comp = null;
                 }
             }
             Debug.Print("");
         }
         public void CreateSameTransMatAsCompCount()
         {
             swCompTrans = new MathTransform[numOfComp];
             if (!((varComp == null)))
             {
                 for (I = 0; I <= varComp.GetUpperBound(0); I++)
                 {
                     Component2 comp = default(Component2);
                     comp = (Component2)varComp[I];
                     swCompTrans[I] = comp.Transform2;
                     comp = null;
                 }
             }
         }
         public void ChangePosOfCompAsPerOption()
         {
             ChangeRefPosOfComp(gposX, gposY);
         }

         public void ChangeRefPosOfComp(double posX, double posY)
         {
             if (!((varComp == null)))
             {
                 for (I = 0; I <= varComp.GetUpperBound(0); I++)
                 {
                     if ((I > 0))
                     {
                         double[] varData = null;
                         varData = (double[])swCompTrans[I].ArrayData;
                         varData[9] = posX * I;
                         varData[10] = posY * I;
                         swCompTrans[I].ArrayData = varData;
                     }
                 }
             }
         }

         public SldWorks swApp;

     }
 }
```
