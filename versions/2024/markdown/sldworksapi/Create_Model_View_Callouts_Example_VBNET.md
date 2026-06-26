---
title: "Create a Callout in a Model View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Model_View_Callouts_Example_VBNET.htm"
---

# Create a Callout in a Model View Example (VB.NET)

This example shows how to create a callout in a model view.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document.
 ' 2. Select:
 '    Project > Add Reference > .NET > SolidWorks.Interop.swpublished
 ' 3. Copy #Class1: to a class named CalloutHandler.
 '
 ' Postconditions:
 ' 1. A callout with one row is created in the first model view.
 ' 2. Press F5 three more times to add a callout to three other model views.

 ' NOTE: Because the model is used elsewhere,
 ' do not save changes when closing it.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System

 Partial Class SolidWorksMacro

     Dim swModelDoc As ModelDoc2
     Dim swModelDocExtn As ModelDocExtension
     Dim ViewMgr As ModelViewManager
     Dim swModelView As ModelView
     Dim Viewcallout As Callout
     Dim handle As New CalloutHandler

     Sub main()

         swModelDoc = swApp.ActiveDoc
         swModelDocExtn = swModelDoc.Extension

         ViewMgr = swModelDoc.ModelViewManager
         ViewMgr.ViewportDisplay = swViewportDisplay_e.swViewportFourView
         swModelDoc.GetModelViewCount()
         swModelView = swModelDoc.GetFirstModelView
         While (Not swModelView Is Nothing)
             Viewcallout = swModelView.CreateCallout(1, handle)
             Viewcallout.Label2(0) =  "TEST"
             Viewcallout.SkipColon =  False
             Viewcallout.ValueInactive(0) = True
             Call Viewcallout.SetTargetPoint(0, 0.0#, 0.0#, 0.0#)
             Viewcallout.Display(True)
             Stop
             swModelView = swModelView.GetNext
         End While

     End Sub

     Public swApp As SldWorks

 End  Class

Class1:
```

```vb
Imports SolidWorks.Interop.swpublished
 Imports System
 Imports System.Runtime.InteropServices
 Imports System.Diagnostics
 <ComVisibleAttribute(True)> _
 Public Class CalloutHandler
     Implements SwCalloutHandler

     Public Function OnStringValueChanged(ByVal pManipulator As Object, ByVal RowID As Integer, ByVal Text As String) As Boolean Implements SolidWorks.Interop.swpublished.SwCalloutHandler.OnStringValueChanged

         Debug.Print("Text: " & Text)
         Debug.Print("Row: " & RowID)

         Return True

     End Function

 End  Class
```
