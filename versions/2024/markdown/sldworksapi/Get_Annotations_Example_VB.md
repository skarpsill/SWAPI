---
title: "Get Annotations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Annotations_Example_VB.htm"
---

# Get Annotations Example (VBA)

This example shows how to get the annotations of a model.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model with one or more annotations.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: All the annotations are printed in the Immediate window.
 '----------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swAnnotation As SldWorks.Annotation
 Dim iAnnoCnt As Integer
 Dim arrAnnotation As Variant
 Dim i As Integer
 Dim IAnnoType As Integer
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension

    iAnnoCnt = swModelDocExt.GetAnnotationCount()

    If iAnnoCnt > 0 Then

    arrAnnotation = swModelDocExt.GetAnnotations()

        For i = LBound(arrAnnotation) To UBound(arrAnnotation)

            Set swAnnotation = arrAnnotation(i)

            IAnnoType = swAnnotation.GetType()

            Select Case IAnnoType

                Case 1
                     Debug.Print "Annotation: Thread"

                Case 2
                     Debug.Print "Annotation: Datum Tag"

                Case 3
                     Debug.Print "Annotation: Datum Target Symbol"

                Case 4
                     Debug.Print "Annotation: Display Diamension"

                Case 5
                      Debug.Print "Annotation: Gtol"

                Case 6
                      Debug.Print "Annotation: Note"

                Case 7
                      Debug.Print "Annotation: SFS Symbol"

                Case 8
                      Debug.Print "Annotation: Weld Symbol"

                Case 9
                      Debug.Print "Annotation: Custom Symbol"

                Case 10
                      Debug.Print "Annotation: Dowel Symbol"

                Case 11
                      Debug.Print "Annotation: Leader"

                Case 12
                      Debug.Print "Annotation: Block"

                Case 13
                      Debug.Print "Annotation: Center Mark symbol"

                Case 14
                      Debug.Print "Annotation: Table Annotation"

                Case 15
                      Debug.Print "Annotation: Center Line"

                Case 16
                      Debug.Print "Annotation: Datum Origin"

              End Select

        Next

    End If
End Sub
```
