---
title: "Get Referenced Display State Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Referenced_Display_State_Example_CSharp.htm"
---

# Get Referenced Display State Example (C#)

This example shows how to get the active display state of a component.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open an assembly that contains two instances of the same
 //    component in different display states.
 // 2. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window for the display states.
 //----------------------------------------------------------------------------
```

```vb
using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 namespace ReferencedDisplayState_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             AssemblyDoc assem = default(AssemblyDoc);
             assem = (AssemblyDoc)swApp.ActiveDoc;

             ModelDoc2 model = default(ModelDoc2);
             model = (ModelDoc2)assem;

             Configuration assemConfig = default(Configuration);
             assemConfig = model.ConfigurationManager.ActiveConfiguration;

             Component2 root = default(Component2);
             root = assemConfig.GetRootComponent3(false);

             object[] comps = null;
             comps = (object[])root.GetChildren();

             object vComp = null;
             foreach (object vComp_loopVariable in comps)
             {
                 vComp = vComp_loopVariable;
                 Component2 comp = default(Component2);
                 comp = (Component2)vComp;

                 string refConfigName = null;
                 refConfigName = comp.ReferencedConfiguration;

                 ModelDoc2 compModel = default(ModelDoc2);
                 compModel = (ModelDoc2)comp.GetModelDoc2();

                 compModel.Visible =  true;

                 Configuration cmActiveConfig = default(Configuration);
                 cmActiveConfig = compModel.ConfigurationManager.ActiveConfiguration;

                 Debug.Print(comp.Name2);
                 Debug.Print("  " + cmActiveConfig.Name + " <" + comp.ReferencedDisplayState +  ">");

                 compModel.Visible =  false;
             }
         }

         public SldWorks swApp;
     }
 }
```
