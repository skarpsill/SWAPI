---
title: "Get Centers of Mass in Drawing Views Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Centers_of_Mass_in_Drawing_Views_Example_VB.htm"
---

# Get Centers of Mass in Drawing Views Example (VBA)

This example shows how to get the centers of mass in drawing views.

```vb
 '----------------------------------------------------------------------
 ' Preconditions: Open a drawing that has one or more centers of mass.
 '
 ' Postconditions: Inspect the Immediate window for the coordinates of
 ' all of the centers of mass in all of the views of the
 ' drawing.
 '----------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swDrawDoc As SldWorks.DrawingDoc
 Dim swView As SldWorks.View
 Dim swCenterOfMass As SldWorks.CenterOfMass
 Dim swAnnotation As SldWorks.Annotation
 Dim sheetCount As Long
 Dim viewCount As Long
 Dim ss As Variant
 Dim vv As Variant
 Dim coord As Variant
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swDrawDoc = swModel

    viewCount = swDrawDoc.GetViewCount
     ss = swDrawDoc.GetViews

    For sheetCount = LBound(ss) To UBound(ss)
         vv = ss(sheetCount)
         For viewCount = 1 To UBound(vv)
             Debug.Print (vv(viewCount).GetName2())
             Set swView = vv(viewCount)
             Set swCenterOfMass = swView.GetFirstCenterOfMass
             If Not swCenterOfMass Is Nothing Then
                 Set swAnnotation = swCenterOfMass.GetAnnotation
                 If Not swAnnotation Is Nothing Then
                     Debug.Print "  Annotation name: " & swAnnotation.GetName
                 End If
                 coord = swCenterOfMass.GetCoordinates
                 Debug.Print "  Center of mass coordinates: X: " & coord(0) & ", Y: " & coord(1) & ", and Z: " & coord(2)

                While Not (swCenterOfMass.GetNext Is Nothing)
                     Set swCenterOfMass = swCenterOfMass.GetNext
                     If Not swCenterOfMass Is Nothing Then
                         Set swAnnotation = swCenterOfMass.GetAnnotation
                         If Not swAnnotation Is Nothing Then
                             Debug.Print "  Annotation name: " & swAnnotation.GetName
                         End If
                         coord = swCenterOfMass.GetCoordinates
                         Debug.Print "  Center of mass coordinates: X: " & coord(0) & ", Y: " & coord(1) & ", and Z: " & coord(2)
                     End If
                 Wend
             End If
         Next viewCount

    Next sheetCount
End Sub
```
