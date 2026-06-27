---
title: "Insert Chain Dimensions Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Chain_Dimensions_Example_VBNET.htm"
---

# Insert Chain Dimensions Example (VB.NET)

This example shows how to insert chain dimensions in a drawing.

```vb
  '=============================================================================
' Preconditions:
 ' 1. Open install_dir\samples\tutorial\advdrawings\foodprocessor.slddrw.
 ' 2. Select the Sheet2 tab at the bottom.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Observe the chained dimensions in Drawing View3.
 ' 2. Inspect the display dimension values in the Immediate window.
```

'

```vb
 ' NOTE: Because the sample is used elsewhere, do not save changes to it.
  '===========================================================================

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial   Class   SolidWorksMacro

       Dim modDocExt  As   ModelDocExtension
       Dim Part  As  ModelDoc2
       Dim selectMgr  As   SelectionMgr
       Dim dimArray(3)  As   Object
       Dim dimObject  As   Object
       Dim entityArray(3)  As   Object
       Dim varArray  As  Object
       Dim myDisplayDim  As   DisplayDimension
       Dim swDim  As  Dimension
       Dim dimText  As  String
       Dim k  As  Integer
       Dim boolstatus  As   Boolean

       Sub main()

           Part = swApp.ActiveDoc
           selectMgr = Part.SelectionManager
           modDocExt = Part.Extension

           Part.ClearSelection2(True)
           boolstatus = Part.ActivateView("Drawing View3")
           boolstatus = Part.Extension.SelectByRay(0.107406727925462, 0.259964392021715, 375.00575, 0, 0, -1, 0.00193314752083778, 1,   False, 0, 0)
           entityArray(0) = selectMgr.GetSelectedObject6(1, -1)

           boolstatus = Part.Extension.SelectByRay(0.135835367937783, 0.281001585630832, 375.00575, 0, 0, -1, 0.00193314752083778, 1,  False, 0, 0)
           entityArray(1) = selectMgr.GetSelectedObject6(2, -1)

           boolstatus = Part.Extension.SelectByRay(0.140383950339754, 0.25598438241999, 375.00575, 0, 0, -1, 0.00193314752083778, 1,  False, 0, 0)
          entityArray(2) = selectMgr.GetSelectedObject6(3, -1)

           boolstatus = Part.Extension.SelectByRay(0.176772609555524, 0.221301441604959, 375.00275, 0, 0, -1, 0.00193314752083778, 1,  False, 0, 0)
           entityArray(3) = selectMgr.GetSelectedObject6(4, -1)

           varArray = entityArray

           dimObject = modDocExt.InsertChainDimensions(varArray)

           dimArray = dimObject

            If dimArray.Length > 0   Then
               For k = 0  To UBound(dimArray)
                  myDisplayDim = dimArray(k)
                  swDim = myDisplayDim.GetDimension2(0)
                  dimText = swDim.Value
                   Debug.Print(dimText)
               Next k
            End  If

       End  Sub

       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
