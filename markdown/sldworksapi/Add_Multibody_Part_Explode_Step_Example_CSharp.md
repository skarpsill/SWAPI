---
title: "Add Multibody Part Explode Step Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Multibody_Part_Explode_Step_Example_CSharp.htm"
---

# Add Multibody Part Explode Step Example (C#)

This example shows how to create an explode view of a multibody part.

```vb
 // -----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open public_documents\samples\tutorial\multibody\multi_Inter.sldprt.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Creates Exploded View1 in ConfigurationManager.
 // 2. Adds Chain1 to Exploded View1.
 // 3. Displays the Exploded View1 in its exploded state.
 // 4. Inspect the Immediate window, the ConfigurationManager,
 // and the graphics area.
 //
 // Note: Because the model is used elsewhere, do not save any changes.
 // ----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System.Diagnostics;

 namespace MultibodyPartExplode_CSharp
 {

       partial  class   SolidWorksMacro
      {
            public  void Main()
           {
               PartDoc swModel;

               Configuration config;

               string configName;

               ModelDoc2 swMdl;

               PartExplodeStep explStep;

               Body2 comp;

               object[] var;

               object[] varViews;

               object[] configVar;

               bool boolstatus;

               int i;

               int errCode;

              swModel = (PartDoc)swApp.ActiveDoc;

              swMdl = (ModelDoc2)swModel;

              configVar = (object[])swMdl.GetConfigurationNames();

              swModel.CreateExplodedView();

              varViews = (object[])swModel.GetExplodedViewNames((string)configVar[0]);

              configName = swModel.GetExplodedViewConfigurationName((string)varViews[0]);

              config = (Configuration)swMdl.GetConfigurationByName(configName);

              swModel.ShowExploded(true, (string)varViews[0]);

               // Select the bodies to move

              boolstatus = swMdl.Extension.SelectByID2("Extrude-Thin1",   "SOLIDBODY", 0, 0, 0,   true, 1,   null, 0);

               // Add an explode step without selecting an explode direction entity

               // Defaults to the Z-direction manipulator index

              explStep = (PartExplodeStep)config.AddPartExplodeStep("Exploded View1", 0.07, -1,  false,  true,  out errCode);

              swMdl.EditRebuild3();

               // Get bodies moved in the explode step

              var = (object[])explStep.GetBodies();

               Debug.Print("Explode view: " + varViews[0]);

               Debug.Print("Explode step: " + explStep.Name);

               Debug.Print("Explode distance (m): " + explStep.ExplodeDistance);

              Debug.Print("Reverse translation direction? " + explStep.ReverseTranslationDirection);

               Debug.Print("Automatically space components on drag? " + explStep.AutoSpaceBodiesOnDrag);

               Debug.Print("Bodies moved in the explode step:");

               for (i = 0; i <= var.GetUpperBound(0); i++)
              {
                  comp = (Body2)var[i];

                   Debug.Print("  " + comp.Name);
              }
           }

            ///  <summary>
            ///     ''' The SldWorks swApp variable is pre-assigned for you.
            ///     '''  </summary>
            public  SldWorks swApp;

      }
 }
```
