---
title: "List Custom Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/List_Custom_Properties_Example_VB.htm"
---

# List Custom Properties Example (VBA)

This example shows how to list the custom properties for a configuration.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a model document to which custom properties
'    are assigned.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Iterates through the configurations and
'    prints configuration-specific and nonconfiguration-
'    specific custom property values to the
'    Immediate window.
' 2. Examine the Immediate window.
'--------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim vConfigNameArr As Variant
    Dim vConfigName As Variant
    Dim vCustInfoNameArr As Variant
    Dim vCustInfoName As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    vConfigNameArr = swModel.GetConfigurationNames
```

```
    ' Is empty if a drawing because configurations not supported in drawings
    If IsEmpty(vConfigNameArr) Then
        ReDim vConfigNameArr(0)
        vConfigNameArr(0) = ""
    Else
        ' Add a blank string for the nonconfiguration-specific custom properties
        ReDim Preserve vConfigNameArr(UBound(vConfigNameArr) + 1)
    End If
```

```
    For Each vConfigName In vConfigNameArr
        Debug.Print vConfigName
        vCustInfoNameArr = swModel.GetCustomInfoNames2(vConfigName)
        If Not IsEmpty(vCustInfoNameArr) Then
            For Each vCustInfoName In vCustInfoNameArr
                Debug.Print "  " & vCustInfoName
                Debug.Print "      Type = " & swModel.GetCustomInfoType3(vConfigName, vCustInfoName)
                Debug.Print "      Value = " & swModel.GetCustomInfoValue(vConfigName, vCustInfoName)
                Debug.Print "      Text = " & swModel.CustomInfo2(vConfigName, vCustInfoName)
            Next
        End If
        Debug.Print "  ---------------------------"
    Next
```

```
End Sub
```
