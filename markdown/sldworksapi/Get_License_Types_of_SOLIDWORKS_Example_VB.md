---
title: "Get License Type of SOLIDWORKS Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_License_Types_of_SOLIDWORKS_Example_VB.htm"
---

# Get License Type of SOLIDWORKS Example (VBA)

This example shows how to get the type of SOLIDWORKS license used when the
model was created.

```
'----------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part document.
' 2. Gets the type of SOLIDWORKS license used when
'    the model was created.
' 3. Examine the Immediate window.
'----------------------------------------------------------
Option Explicit
```

```
Sub GetLicense(swApp As SldWorks.SldWorks, ltype As Long)
        Select Case ltype
        Case swLicenseType_e.swLicenseType_Educational
            Debug.Print "  Educational"
        Case swLicenseType_e.swLicenseType_Student
            Debug.Print "  Student"
        Case swLicenseType_e.swLicenseType_StudentDesignKit
            Debug.Print "  Student Design Kit"
        Case swLicenseType_e.swLicenseType_PersonalEdition
            Debug.Print "  Personal Edition"
        Case swLicenseType_e.swLicenseType_Full_Office
            Debug.Print "  Office"
        Case swLicenseType_e.swLicenseType_Full_Professional
            Debug.Print "  Professional"
        Case swLicenseType_e.swLicenseType_Full_Premium
            Debug.Print "  Premium"
        Case swLicenseType_e.swLicenseType_Full
            Debug.Print "  Standard"
    End Select
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim licenseType As Long
    Dim errors As Long
    Dim warnings As Long
    Dim fileName As String
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    licenseType = swModelDocExt.GetLicenseType
    Debug.Print "Type of SOLIDWORKS license used when the model was created:"
    GetLicense swApp, licenseType
```

```
End Sub
```
