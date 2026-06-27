---
title: "Get Centers of Mass in Drawing Views Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Centers_of_Mass_in_Drawing_Views_Example_VBNET.htm"
---

# Get Centers of Mass in Drawing Views Example (VB.NET)

This example shows how to get the centers of mass in drawing views.

```vb
 '----------------------------------------------------------------------
 ' Preconditions: Open a drawing that has one or more centers of mass.
 '
 ' Postconditions: Inspect the Immediate window for the coordinates of
 ' all of the centers of mass in all of the views of the
 ' drawing.
 '----------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swDrawDoc As DrawingDoc
     Dim swView As View
     Dim swCenterOfMass As CenterOfMass
     Dim swAnnotation As Annotation
     Dim sheetCount As Integer
     Dim viewCount As Integer
     Dim ss As Object
     Dim vv As Object
     Dim coord As Object

     Sub main()

         swModel = swApp.ActiveDoc
         swDrawDoc = swModel

         viewCount = swDrawDoc.GetViewCount
         ss = swDrawDoc.GetViews

         For sheetCount = LBound(ss) To UBound(ss)
             vv = ss(sheetCount)
             For viewCount = 1 To UBound(vv)
                 Debug.Print(vv(viewCount).GetName2())
                 swView = vv(viewCount)
                 swCenterOfMass = swView.GetFirstCenterOfMass
                 If Not swCenterOfMass Is Nothing Then
                     swAnnotation = swCenterOfMass.GetAnnotation
                     If Not swAnnotation Is Nothing Then
                         Debug.Print("  Annotation name: " & swAnnotation.GetName)
                     End If
                     coord = swCenterOfMass.GetCoordinates
                     Debug.Print("  Center of mass coordinates: X: " & coord(0) & ", Y: " & coord(1) & ", and Z: " & coord(2))

                     While Not (swCenterOfMass.GetNext Is  Nothing)
                         swCenterOfMass = swCenterOfMass.GetNext
                         If Not swCenterOfMass Is Nothing Then
                             swAnnotation = swCenterOfMass.GetAnnotation
                             If Not swAnnotation Is Nothing Then
                                 Debug.Print("  Annotation name: " & swAnnotation.GetName)
                             End If
                             coord = swCenterOfMass.GetCoordinates
                             Debug.Print("  Center of mass coordinates: X: " & coord(0) & ", Y: " & coord(1) & ", and Z: " & coord(2))
                         End If
                     End While
                 End If
             Next viewCount

         Next sheetCount

     End Sub

     Public swApp As SldWorks

 End  Class
```
