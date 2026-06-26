---
title: "Get Original Body from Pattern Body (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Original_Body_from_Pattern_Body_Example_VBNET.htm"
---

# Get Original Body from Pattern Body (VB.NET)

This example shows how to get the original body from a pattern body.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document that contains a pattern of solid bodies.
 ' 2. Select a pattern body from the Solid Bodies folder.
 '
 ' Postconditions:
 ' 1. The original body from which the pattern was generated is hidden from view.
 ' 2. Click F5 to display the original body.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swDoc As ModelDoc2
     Dim swSm As SelectionMgr
     Dim selType As Integer
     Dim swBody As Body2
     Dim swOriBody As Body2
     Dim swMathTrans As MathTransform

     Sub main()

         swDoc = swApp.ActiveDoc
         swSm = swDoc.SelectionManager

         selType = swSm.GetSelectedObjectType3(1, -1)
         swBody = swSm.GetSelectedObject6(1, -1)
         Debug.Print("Number of edges in pattern body: " & swBody.GetEdgeCount)

         If (swBody Is Nothing) Then
             MsgBox("Select body from 'Solid Bodies' folder")
         Else
             swDoc.ClearSelection()
             swOriBody = swBody.GetOriginalPatternedBody(swMathTrans)

             If Not (swOriBody Is Nothing) Then
                 swOriBody.HideBody(True)

                 Stop

                 swOriBody.HideBody(False)
                 swOriBody = Nothing
             End If
             swBody =  Nothing
         End If

     End Sub

     Public swApp As SldWorks

 End Class
```
