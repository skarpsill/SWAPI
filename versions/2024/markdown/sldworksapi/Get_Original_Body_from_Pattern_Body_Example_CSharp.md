---
title: "Get Original Body from Pattern Body (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Original_Body_from_Pattern_Body_Example_CSharp.htm"
---

# Get Original Body from Pattern Body (C#)

This example shows how to get the original body from a pattern body.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part document that contains a pattern of solid bodies.
 // 2. Select a pattern body from the Solid Bodies folder.
 //
 // Postconditions:
 // 1. The original body from which the pattern was generated is hidden from view.
 // 2. Click F5 to display the original body.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System.Windows.Forms;

 namespace GetOriginalBodyFromPattern_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swDoc;
         SelectionMgr swSm;
         int selType;
         Body2 swBody;
         Body2 swOriBody;

         MathTransform swMathTrans;

         public void Main()
         {
             swDoc = (ModelDoc2)swApp.ActiveDoc;
             swSm = (SelectionMgr)swDoc.SelectionManager;

             selType = swSm.GetSelectedObjectType3(1, -1);
             swBody = (Body2)swSm.GetSelectedObject6(1, -1);
             Debug.Print("Number of edges in pattern body: " + swBody.GetEdgeCount());

             if ((swBody == null))
             {
                 MessageBox.Show("Select body from 'Solid Bodies' folder");
             }
             else
             {
                 swDoc.ClearSelection();
                 swOriBody = swBody.GetOriginalPatternedBody(out swMathTrans);

                 if ((swOriBody != null))
                 {
                     swOriBody.HideBody(true);

                     System.Diagnostics.Debugger.Break();

                     swOriBody.HideBody(false);
                     swOriBody = null;
                 }
                 swBody = null;
             }

         }

         public SldWorks swApp;

     }
 }
```
