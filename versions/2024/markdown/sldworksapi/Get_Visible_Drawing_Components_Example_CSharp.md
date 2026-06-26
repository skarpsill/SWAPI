---
title: "Insert Chain Dimensions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Visible_Drawing_Components_Example_CSharp.htm"
---

# Insert Chain Dimensions Example (C#)

This example shows how to insert chain dimensions in a drawing.

```vb
  //=========================================================================
 // Preconditions:
 // 1. Open install_dir\samples\tutorial\advdrawings\foodprocessor.slddrw.
 // 2. Select the Sheet2 tab at the bottom.
 // 3. Open the Immediate window.
 //
 // Postconditions:
 // 1. Observe the chained dimensions in Drawing View3.
 // 2. Inspect the display dimension values in the Immediate window.
  //
  // NOTE: Because the sample is used elsewhere, do not save changes.
  //=========================================================================

 using System;
 using System.Diagnostics;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows;
 using System.Windows.Forms;

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace InsertChainDimensions_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
            public  void Main()
           {

               ModelDocExtension modDocExt;
               ModelDoc2 Part;
               SelectionMgr selectMgr;
               object[] dimArray =   new   object[4];
               object dimObject;
               object[] entityArray =   new   object[4];
               object varArray;
               DisplayDimension myDisplayDim;
               Dimension swDim;
               string dimText;
               int k;
               bool boolstatus;

              Part = (ModelDoc2)swApp.ActiveDoc;
              selectMgr = (SelectionMgr)Part.SelectionManager;
              modDocExt = Part.Extension;

              Part.ClearSelection2(true);
              boolstatus = ((DrawingDoc)Part).ActivateView("Drawing View3");
              boolstatus = Part.Extension.SelectByRay(0.107406727925462, 0.259964392021715, 375.00575, 0, 0, -1, 0.00193314752083778, 1,  false, 0, 0);
              entityArray[0] = selectMgr.GetSelectedObject6(1, -1);

              boolstatus = Part.Extension.SelectByRay(0.135835367937783, 0.281001585630832, 375.00575, 0, 0, -1, 0.00193314752083778, 1,  false, 0, 0);
              entityArray[1] = selectMgr.GetSelectedObject6(2, -1);

              boolstatus = Part.Extension.SelectByRay(0.140383950339754, 0.25598438241999, 375.00575, 0, 0, -1, 0.00193314752083778, 1,  false, 0, 0);
              entityArray[2] = selectMgr.GetSelectedObject6(3, -1);

              boolstatus = Part.Extension.SelectByRay(0.176772609555524, 0.221301441604959, 375.00275, 0, 0, -1, 0.00193314752083778, 1,   false, 0, 0);
              entityArray[3] = selectMgr.GetSelectedObject6(4, -1);

              varArray = entityArray;

              dimObject = modDocExt.InsertChainDimensions(varArray);

              dimArray = (object[])dimObject;

               if (dimArray.Length > 0)
              {
                   for (k = 0; k <= dimArray.GetUpperBound(0); k++)
                  {
                      myDisplayDim = (DisplayDimension)dimArray[k];
                      swDim = myDisplayDim.GetDimension2(0);
                      dimText = swDim.Value.ToString();
                        Debug.Print(dimText);
                  }
              }
           }

       // The SldWorks swApp variable is pre-assigned for you.
       public  SldWorks swApp;

     }
 }
```
