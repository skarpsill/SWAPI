---
title: "Get Original Body from Pattern Body (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Original_Body_from_Pattern_Body_Example_VB.htm"
---

# Get Original Body from Pattern Body (VBA)

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
Dim swApp As SldWorks.SldWorks
 Dim swDoc As SldWorks.ModelDoc2
 Dim swSm As SldWorks.SelectionMgr
 Dim selType As Long
 Dim swBody As SldWorks.Body2
 Dim swOriBody As SldWorks.Body2
 Dim swMathTrans As SldWorks.MathTransform
 Option Explicit
 Sub main()
Set swApp = Application.SldWorks
 Set swDoc = swApp.ActiveDoc
 Set swSm = swDoc.SelectionManager
selType = swSm.GetSelectedObjectType3(1, -1)
 Set swBody = swSm.GetSelectedObject6(1, -1)
If (swBody Is Nothing) Then
     MsgBox ("Select body from 'Solid Bodies' folder")
 Else
     swDoc.ClearSelection
     Set swOriBody = swBody.GetOriginalPatternedBody(swMathTrans)
    If Not (swOriBody Is Nothing) Then
         swOriBody.HideBody True

        Stop

        swOriBody.HideBody False
         Set swOriBody = Nothing
     End If
     Set swBody = Nothing
 End If
End Sub
```
