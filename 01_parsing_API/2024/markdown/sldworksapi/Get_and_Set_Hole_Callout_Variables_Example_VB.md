---
title: "Get and Set Hole Callout Variables Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Hole_Callout_Variables_Example_VB.htm"
---

# Get and Set Hole Callout Variables Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swDisplayDimension As SldWorks.DisplayDimension
Dim swCalloutLengthVariable As SldWorks.CalloutLengthVariable
Dim swCalloutAngleVariable As SldWorks.CalloutAngleVariable
Dim swCalloutStringVariable As SldWorks.CalloutStringVariable
Dim swCalloutVariable As SldWorks.CalloutVariable
Dim i As Long
Dim vType As Long
Dim holeVariables As Variant
Dim str1 As String
Dim str2 As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    'Get the selected hole callout
    Set swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
    holeVariables = swDisplayDimension.GetHoleCalloutVariables
    Debug.Print "Number of hole callout variables = " & UBound(holeVariables) + 1
    Debug.Print ""
```

```
    'Determine type of hole callout variable and get and set some values
    For i = 0 To UBound(holeVariables)
        Set swCalloutVariable = holeVariables(i)
        str1 = "  Callout variable name = " & swCalloutVariable.VariableName
        str2 = "  Callout variable name as it appears in Dimension PropertyManager page = " & swCalloutVariable.UserReadableVariableName
        vType = swCalloutVariable.Type
        If vType = swCalloutVariableType_e.swCalloutVariableType_Length Then
            Set swCalloutLengthVariable = swCalloutVariable
            Debug.Print "Callout variable(" & i & ")'s" & " type = length"
            Debug.Print str1
            Debug.Print str2
            Debug.Print "  Length = " & swCalloutLengthVariable.Length
            Debug.Print "  Precision = " & swCalloutLengthVariable.precision
            Debug.Print "  Tolerance precision = " & swCalloutLengthVariable.TolerancePrecision
            swCalloutLengthVariable.precision = swCalloutLengthVariable.precision - 1 - i
            Debug.Print "  Changed precision = " & swCalloutLengthVariable.precision
            swCalloutVariable.ToleranceType = swTolType_e.swTolBILAT
        ElseIf vType = swCalloutVariableType_e.swCalloutVariableType_Angle Then
            Set swCalloutAngleVariable = swCalloutVariable
            Debug.Print "Callout variable(" & i & ")'s" & " type = angle"
            Debug.Print str1
            Debug.Print str2
            Debug.Print "  Angle = " & swCalloutAngleVariable.Angle
          ElseIf vType = swCalloutVariableType_e.swCalloutVariableType_String Then
            Set swCalloutStringVariable = swCalloutVariable
            Debug.Print "Callout variable(" & i & ")'s" & " type = string"
            Debug.Print str1
            Debug.Print str2
            Debug.Print "  String = '" & swCalloutStringVariable.String & "'"
        End If
    Next
```

```
End Sub
```
