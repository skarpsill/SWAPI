---
title: "Create Triad Manipulator Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swpublishedapi/Create_Triad_Manipulator_Example_CSharp.htm"
---

# Create Triad Manipulator Example (C#)

This example shows how to create a triad manipulator.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Right-click the project name in the Project Explorer and click
 //    Add Reference.
 // 2. On the Browse tab, navigate to install_dir\api\redist, click
 //    SolidWorks.Interop.swpublished.dll, and click OK.
  // 3. Right-click the project name in the Project Explorer and click
 //    Add > Class.
 // 4. Type swDragManipHdlr.cs in Name and click OK.
 // 5. Copy Module to SolidWorksMacro.cs.
 // 6. Copy Class module to swDragManipHdlr.cs.
 // 7. Click Tools > Options and ensure that Stop VSTA debugger on macro exit
 //    is not selected.
 // 8. Open a model document and select a face.
 // 9. Open an Immediate window.
 //
 // Postconditions:
  // 1. Creates a triad manipulator whose origin is the point
 //    selected on the face.
  // 2. Drag a triad manipulator handle and inspect the Immediate window.
  //----------------------------------------------------------------------------
  //Module
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace CreateTriadManipulator_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         swDragManipHdlr swDragHdlr;

         public void Main()
         {
             Manipulator swManip = default(Manipulator);
             TriadManipulator swTriad = default(TriadManipulator);
             Face2 swFace = default(Face2);
             MathUtility swMathUtil = default(MathUtility);
             ModelDoc2 swModel = default(ModelDoc2);
             ModelViewManager swModViewMgr = default(ModelViewManager);
             SelectionMgr swSelMgr = default(SelectionMgr);
             object vPickPt = null;
             MathPoint swPickPt = default(MathPoint);

             swDragHdlr = new swDragManipHdlr();

             swMathUtil = (MathUtility)swApp.GetMathUtility();
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFace = (Face2)swSelMgr.GetSelectedObject6(1, -1);

             vPickPt = swSelMgr.GetSelectionPoint2(1, -1);
             swPickPt = (MathPoint)swMathUtil.CreatePoint((vPickPt));
             swModViewMgr = swModel.ModelViewManager;

             swManip = swModViewMgr.CreateManipulator((int)swManipulatorType_e.swTriadManipulator, swDragHdlr);
             swTriad = (TriadManipulator)swManip.GetSpecificManipulator();
             swTriad.Origin = swPickPt;
             swManip.Show(swModel);

         }

         public SldWorks swApp;
     }
 }
 Back to top
  //Class module
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.swpublished;
 using SolidWorks.Interop.swconst;
 using System.Runtime;

 [System.Runtime.InteropServices.ComVisibleAttribute(true)]
 public class swDragManipHdlr : SwManipulatorHandler2
 {

     public bool OnDelete(object pManipulator)
     {
         Debug.Print("Manipulator deleted");
         return true;
     }

     public void OnDirectionFlipped(object pManipulator)
     {
         Debug.Print("Direction flipped");
     }

     public bool OnDoubleValueChanged(object pManipulator, int handleIndex, ref double Value)
     {
         Debug.Print("Double value changed");
         Debug.Print("  Value = " + Value);
         return true;
     }

     public void OnEndNoDrag(object pManipulator, int handleIndex)
     {
         Debug.Print("Mouse button released");
     }

     public void OnEndDrag(object pManipulator, int handleIndex)
     {
         Debug.Print("Mouse button released after dragging a manipulator handle");
     }

     public void OnHandleRmbSelected(object pManipulator, int handleIndex)
     {
         Debug.Print("Right-mouse button clicked");
         Debug.Print("  HandleIndex = " + handleIndex);
     }

     public void OnHandleSelected(object pManipulator, int handleIndex)
     {
         Debug.Print("Manipulator handle selected");
         Debug.Print("  HandleIndex = " + handleIndex);
     }

     public void OnItemSetFocus(object pManipulator, int Id)
     {
         Debug.Print("Focus set on item");
         Debug.Print("  Item ID = " + Id);
     }

     public bool OnHandleLmbSelected(object pManipulator)
     {
         Debug.Print("Left-mouse button clicked");
         return true;
     }

     public bool OnStringValueChanged(object pManipulator, int handleIndex, ref string Value)
     {
         Debug.Print("String value changed");
         Debug.Print("  String value  = " + Value);
         return true;
     }

     public void OnUpdateDrag(object pManipulator, int handleIndex, object newPosMathPt)
     {
         Debug.Print("Manipulator handle moved while left- or right-mouse button depressed");
         Debug.Print("  HandleIndex = " + handleIndex);
     }

 }
 Back to top
```
