---
title: "Get and Set Hole Callout Variables Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm"
---

# Get and Set Hole Callout Variables Example (VB.NET)

This example shows how to get and set hole callout variables.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a drawing document containing a hole callout.
' 2. Select the hole callout.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Iterates through the variables in the hole callout and
'    gets any angle, length, and string callout
'    variables.
' 2. If the hole callout variable is a length variable,
'    then sets its precision and tolerance type.
' 3. Examine the Immediate window.
'--------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swDisplayDimension As DisplayDimension
        Dim swCalloutLengthVariable As CalloutLengthVariable
        Dim swCalloutAngleVariable As CalloutAngleVariable
        Dim swCalloutStringVariable As CalloutStringVariable
        Dim swCalloutVariable As CalloutVariable
        Dim i As Integer
        Dim vType As Integer
        Dim holeVariables As Object
        Dim str1 As String
        Dim str2 As String

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager

        'Get the selected hole callout
        swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
        holeVariables = swDisplayDimension.GetHoleCalloutVariables
        Debug.Print("Number of hole callout variables = " & UBound(holeVariables) + 1)
        Debug.Print("")

        'Determine type of hole callout variable and get and set some values
        For i = 0 To UBound(holeVariables)
            swCalloutVariable = holeVariables(i)
            str1 = "  Callout variable name = " & swCalloutVariable.VariableName
            str2 = "  Callout variable name as it appears in Dimension PropertyManager page = " & swCalloutVariable.UserReadableVariableName
            vType = swCalloutVariable.Type
            If vType = swCalloutVariableType_e.swCalloutVariableType_Length Then
                swCalloutLengthVariable = swCalloutVariable
                Debug.Print("Callout variable(" & i & ")'s" & " type = length")
                Debug.Print(str1)
                Debug.Print(str2)
                Debug.Print("  Length = " & swCalloutLengthVariable.Length)
                Debug.Print("  Precision = " & swCalloutLengthVariable.Precision)
                Debug.Print("  Tolerance precision = " & swCalloutLengthVariable.TolerancePrecision)
                swCalloutLengthVariable.Precision = swCalloutLengthVariable.Precision - 1 - i
                Debug.Print("  Changed precision = " & swCalloutLengthVariable.Precision)
                swCalloutVariable.ToleranceType = swTolType_e.swTolBILAT
            ElseIf vType = swCalloutVariableType_e.swCalloutVariableType_Angle Then
                swCalloutAngleVariable = swCalloutVariable
                Debug.Print("Callout variable(" & i & ")'s" & " type = angle")
                Debug.Print(str1)
                Debug.Print(str2)
                Debug.Print("  Angle = " & swCalloutAngleVariable.Angle)
            ElseIf vType = swCalloutVariableType_e.swCalloutVariableType_String Then
                swCalloutStringVariable = swCalloutVariable
                Debug.Print("Callout variable(" & i & ")'s" & " type = string")
                Debug.Print(str1)
                Debug.Print(str2)
                Debug.Print("  String = '" & swCalloutStringVariable.String & "'")
            End If
        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
