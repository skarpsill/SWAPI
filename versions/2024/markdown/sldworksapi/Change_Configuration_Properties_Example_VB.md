---
title: "Change Configuration Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Configuration_Properties_Example_VB.htm"
---

# Change Configuration Properties Example (VBA)

This example shows how to change the properties of one or more configurations.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open a part that contains one or more configurations.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Changes the source for the part number and displays XXXX
'    as the part number in each configuration's Bill of Materials.
' 2. Examine the Immediate window.
'------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.PartDoc
Dim Doc As SldWorks.ModelDoc2
Dim SelMgr As SldWorks.SelectionMgr
```

```
Function BOMPartNumber(config As SldWorks.Configuration, document As SldWorks.ModelDoc2) As String
    Select Case config.BOMPartNoSource
    Case SwConst.swBOMPartNumberSource_e.swBOMPartNumber_ConfigurationName
        BOMPartNumber = config.Name
    Case SwConst.swBOMPartNumberSource_e.swBOMPartNumber_DocumentName
        BOMPartNumber = document.GetTitle
    Case SwConst.swBOMPartNumberSource_e.swBOMPartNumber_UserSpecified
        BOMPartNumber = config.AlternateName
    Case SwConst.swBOMPartNumberSource_e.swBOMPartNumber_ParentName
        Dim parentConfig As SldWorks.Configuration
        Set parentConfig = config.GetParent
        If parentConfig.BOMPartNoSource = SwConst.swBOMPartNumberSource_e.swBOMPartNumber_ParentName Then
            BOMPartNumber = BOMPartNumber(parentConfig, document)
        Else
            BOMPartNumber = parentConfig.Name
        End If
    End Select
End Function
```

```
Function InspectConfigurations(Doc As SldWorks.ModelDoc2)
    Dim params As Variant
    params = Doc.GetConfigurationNames
    Dim vName As Variant
    Dim Name As String
    Dim thisConfig As Configuration
    For Each vName In params
        Name = vName
        Set thisConfig = Doc.GetConfigurationByName(Name)
        Debug.Print "Name                      ", thisConfig.Name
        ' Work out what the BOM part number is based on any derived configurations
        Debug.Print "BOMPartNumber             ", BOMPartNumber(thisConfig, Doc)
        Debug.Print "AlternateName             ", thisConfig.AlternateName
        Debug.Print "Comment                   ", thisConfig.Comment
        Debug.Print "Description               ", thisConfig.Description
        Debug.Print "HideNewComponentModels    ", thisConfig.HideNewComponentModels
        Debug.Print "Lock                      ", thisConfig.Lock
        Debug.Print "ShowChildComponentsInBOM  ", thisConfig.ShowChildComponentsInBOM
        Debug.Print "UseAlternateNameInBOM     ", thisConfig.UseAlternateNameInBOM
        Debug.Print "SuppressNewComponentModels", thisConfig.SuppressNewComponentModels
        Debug.Print "SuppressNewFeatures       ", thisConfig.SuppressNewFeatures
        Debug.Print "------------------------------------------------------------------"
    Next vName
End Function
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
    Set Doc = Part
    Set SelMgr = Doc.SelectionManager
```

```
    Call InspectConfigurations(Doc)
```

```
    Dim params As Variant
    params = Doc.GetConfigurationNames
    Dim vName As Variant
    Dim Name As String
    Dim thisConfig As Configuration
    Debug.Print "Modifying the configurations..."
    For Each vName In params
        Name = vName
        Set thisConfig = Doc.GetConfigurationByName(Name)
        Debug.Print "Name                      ", thisConfig.Name
        thisConfig.BOMPartNoSource = swBOMPartNumber_UserSpecified
        thisConfig.AlternateName = "XXXX"
        thisConfig.UseAlternateNameInBOM = True
        thisConfig.AlternateName = "XXXX"
    Next vName
```

```
    Debug.Print "------------------------------------------------------------------"
```

```
    Call InspectConfigurations(Doc)
```

```
End Sub
```
