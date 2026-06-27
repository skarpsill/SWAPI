---
title: "Get Annotations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Annotations_Example_VBNET.htm"
---

# Get Annotations Example (VB.NET)

This example shows how to get the annotations of a model.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model with one or more annotations.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: All the annotations are printed in the Immediate window.
 '----------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swAnnotation As Annotation
         Dim iAnnoCnt As Integer
         Dim arrAnnotation As Object
         Dim i As  Integer
         Dim IAnnoType As Integer

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension

         iAnnoCnt = swModelDocExt.GetAnnotationCount()

         If iAnnoCnt > 0 Then
             arrAnnotation = swModelDocExt.GetAnnotations()

             For i = LBound(arrAnnotation) To UBound(arrAnnotation)

                 swAnnotation = arrAnnotation(i)

                 IAnnoType = swAnnotation.GetType()

                 Select Case IAnnoType

                     Case 1
                         Debug.Print("Annotation: Thread")

                     Case 2
                         Debug.Print("Annotation: Datum Tag")

                     Case 3
                         Debug.Print("Annotation: Datum Target Symbol")

                     Case 4
                         Debug.Print("Annotation: Display Diamension")

                     Case 5
                         Debug.Print("Annotation: Gtol")

                     Case 6
                         Debug.Print("Annotation: Note")

                     Case 7
                         Debug.Print("Annotation: SFS Symbol")

                     Case 8
                         Debug.Print("Annotation: Weld Symbol")

                     Case 9
                         Debug.Print("Annotation: Custom Symbol")

                     Case 10
                         Debug.Print("Annotation: Dowel Symbol")

                     Case 11
                         Debug.Print("Annotation: Leader")

                     Case 12
                         Debug.Print("Annotation: Block")

                     Case 13
                         Debug.Print("Annotation: Center Mark symbol")

                     Case 14
                         Debug.Print("Annotation: Table Annotation")

                     Case 15
                         Debug.Print("Annotation: Center Line ")

                     Case 16
                         Debug.Print("Annotation: Datum Origin")

                 End Select
             Next
         End If
     End Sub

     Public swApp As SldWorks

 End  Class
```
