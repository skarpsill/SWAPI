---
title: "Traverse Hierarchy of Configurations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Hierarchy_of_Configurations_Example_VB.htm"
---

# Traverse Hierarchy of Configurations Example (VBA)

This examples shows how to traverse a hierarchy of configurations.

```
'-------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Traverses the configurations and prints
'    each configuration's information to the
'    Immediate window.
' 2. Examine the Immediate window.
'--------------------------------------------
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
    Dim swConfig As SldWorks.Configuration
    Dim swParentConfig As SldWorks.Configuration
    Dim swConfMgr As SldWorks.ConfigurationManager
    Dim vChildConfigArr As Variant
    Dim vChildConfig  As Variant
    Dim swChildConfig As SldWorks.Configuration
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swConfMgr = swModel.ConfigurationManager
    Set swConfig = swConfMgr.ActiveConfiguration
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Active configuration = " & swConfig.Name
    Debug.Print ""
```

```
    ' Always at least one configuration exists
    vConfigNameArr = swModel.GetConfigurationNames
    For Each vConfigName In vConfigNameArr
        Set swConfig = swModel.GetConfigurationByName(vConfigName)
        Debug.Print "  Configuration name = " & swConfig.Name
        Debug.Print "    Description = " & swConfig.Description
        Debug.Print "    Comment = " & swConfig.Comment
        Debug.Print "    Use alternate name om BOM? " & swConfig.UseAlternateNameInBOM; ""
        Debug.Print "    Alternate name = " & swConfig.AlternateName
        Debug.Print "    Show child components in BOM? " & swConfig.ShowChildComponentsInBOM
        Debug.Print "    Hide new component models? " & swConfig.HideNewComponentModels
        Debug.Print "    Suppress new component models? " & swConfig.SuppressNewComponentModels
        Debug.Print "    Suppress new features? " & swConfig.SuppressNewFeatures
        Debug.Print "    Stream name = " & swConfig.GetStreamName
        Debug.Print "    Is derived? " & swConfig.IsDerived
```

```
        ' Process parent
        Set swParentConfig = swConfig.GetParent
```

```
        If Not swParentConfig Is Nothing Then
            Debug.Print "      Parent = " & swParentConfig.Name
        End If
```

```
        ' Process children
        vChildConfigArr = swConfig.GetChildren
        If Not IsEmpty(vChildConfigArr) Then
            For Each vChildConfig In vChildConfigArr
                Set swChildConfig = vChildConfig
                Debug.Print "      Child = " & swChildConfig.Name
            Next
        End If
        Debug.Print ""
    Next
```

```
End Sub
```
