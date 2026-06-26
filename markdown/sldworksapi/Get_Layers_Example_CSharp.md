---
title: "Get Layers Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Layers_Example_CSharp.htm"
---

# Get Layers Example (C#)

This example shows how to get the layers in a drawing document.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing document.
 // 2. Open an Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
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
 namespace GetLayers_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             LayerMgr swLayerMgr = default(LayerMgr);
             object[] vLayerArr = null;
             object vLayer = null;
             Layer swLayer = default(Layer);

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swLayerMgr = (LayerMgr)swModel.GetLayerManager();

             Debug.Print("File = " + swModel.GetPathName());
             Debug.Print("  Current Layer = " + swLayerMgr.GetCurrentLayer());
             Debug.Print("");

             vLayerArr = (object[])swLayerMgr.GetLayerList();
             foreach (object vLayer_loopVariable in vLayerArr)
             {
                 vLayer = vLayer_loopVariable;
                 swLayer = (Layer)swLayerMgr.GetLayer(vLayer.ToString());

                 Debug.Print("    Layer          = " + swLayer.Name);
                 Debug.Print("    Color          = " + swLayer.Color);
                 Debug.Print("    Description    = " + swLayer.Description);
                 Debug.Print("    ID             = " + swLayer.GetID());
                 Debug.Print("    Style          = " + swLayer.Style);
                 Debug.Print("    Visible        = " + swLayer.Visible);
                 Debug.Print("    Width          = " + swLayer.Width);
                 Debug.Print("    Printable      = " + swLayer.Printable);
             }

         }

         public SldWorks swApp;

     }
 }
```
