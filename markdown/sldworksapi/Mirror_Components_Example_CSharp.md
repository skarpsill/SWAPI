---
title: "Mirror Components Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Mirror_Components_Example_CSharp.htm"
---

# Mirror Components Example (C#)

This example shows how to mirror components in an assembly.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\advdrawings\98food processor.sldasm.
 //
 // Postconditions:
 // 1. Inserts reference plane PLANE4.
 // 2. Creates feature MirrorComponent1 that mirrors six assembly
 //    components.
 // 3. Saves the mirror components to files with file name suffix _TestMirror to
 //    public_documents\samples\tutorial\advdrawings.
 // 4. Examine public_documents\samples\tutorial\advdrawings, the FeatureManager design
 //    tree, and the graphics area.
 //
 // NOTE: Because the assembly is used elsewhere, do not save changes.
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
 namespace MirrorComponents2_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             swModel = (ModelDoc2)swApp.ActiveDoc;

             bool boolstatus = false;
             boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.104250921669188, -0.000236987012272039, -0.0597199999999418,  true, 0,  null, 0);
             RefPlane myRefPlane = default(RefPlane);
             myRefPlane = (RefPlane)swModel.FeatureManager.InsertRefPlane(8, 0.01, 0, 0, 0, 0);

             AssemblyDoc swAssem = default(AssemblyDoc);
             swAssem = (AssemblyDoc)swModel;

             object compsToInstance = null;
             compsToInstance = null;

             object filenames = null;
             filenames = null;

             string location = null;
             location = "";

             swMirrorComponentNameModifier_e nameModifierType = default(swMirrorComponentNameModifier_e);
             nameModifierType =  swMirrorComponentNameModifier_e.swMirrorComponentName_Suffix;
             string nameModifier = null;
             nameModifier = "_TestMirror";

             Feature mirrorPlane = default(Feature);
             mirrorPlane = (Feature)swAssem.FeatureByName("PLANE4");

             Component2[] compsToMirror = new Component2[6];
             compsToMirror[0] = swAssem.GetComponentByName("gear- caddy-1");
             compsToMirror[1] = swAssem.GetComponentByName("middle-gear-1");
             compsToMirror[2] = swAssem.GetComponentByName("shaft gear-1");
             compsToMirror[3] = swAssem.GetComponentByName("middle-gear plate-1");
             compsToMirror[4] = swAssem.GetComponentByName("base plate-1");
             compsToMirror[5] = swAssem.GetComponentByName("shaft gear insert-1");

             object orientations = null;
             orientations = null;

             bool orientAboutCoM = false;
             orientAboutCoM = true;

             bool createDerivedConfigs = false;
             createDerivedConfigs = false;

             int importOptions = 0;
             importOptions = (int)swMirrorPartOptions_e.swMirrorPartOptions_ImportSolids;

             bool breakLinks = false;
             breakLinks = false;
             bool preserveZAxis = false;
             preserveZAxis = true;

             object vResult = null;
             vResult = swAssem.MirrorComponents3(mirrorPlane, compsToInstance, orientations, orientAboutCoM, (compsToMirror), createDerivedConfigs, filenames, (int)nameModifierType, nameModifier, location, importOptions, breakLinks, preserveZAxis,  true);

         }

         public SldWorks swApp;

     }
 }
```
