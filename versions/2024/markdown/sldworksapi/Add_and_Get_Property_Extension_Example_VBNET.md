---
title: "Add and Get Property Extensions Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Get_Property_Extension_Example_VBNET.htm"
---

# Add and Get Property Extensions Example (VB.NET)

This example shows how to add and get a property extension on a part.

```
'---------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Adds three property extensions to the part.
' 2. Gets the three property extensions added to the part.
' 3. Examine the Immediate window.
'----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swPart As PartDoc
        Dim retVal As Integer
        Dim objAdded As Object
        Dim objAdded2 As Object
        Dim objAdded3 As Object
        Dim objRetrieved As Object

        swPart = swApp.ActiveDoc

        Debug.Print("Property extensions added:")

        objAdded = "12345PID"
        retVal = swPart.AddPropertyExtension(objAdded)
        Debug.Print(" First property extension: " & objAdded)

        objAdded2 = "6789PID"
        retVal = swPart.AddPropertyExtension(objAdded2)
        Debug.Print(" Second property extension: " & objAdded2)

        objAdded3 = "00000PDID"
        retVal = swPart.AddPropertyExtension(objAdded3)
        Debug.Print(" Third property extension: " & objAdded3)

        Debug.Print("Property extensions retrieved:")

        objRetrieved = swPart.GetPropertyExtension(retVal - 3)
        Debug.Print(" First property extension: " & objRetrieved)

        objRetrieved = swPart.GetPropertyExtension(retVal - 2)
        Debug.Print(" Second property extension: " & objRetrieved)

        objRetrieved = swPart.GetPropertyExtension(retVal - 1)
        Debug.Print(" Third property extension: " & objRetrieved)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
