---
title: "Export SOLIDWORKS MBD to STEP 242 Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Export_SOLIDWORKS_MBD_to_STEP_242_Example_VB.htm"
---

# Export SOLIDWORKS MBD to STEP 242 Example (VBA)

This example shows how to export a SOLIDWORKS MBD part to a STEP 242 file.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that:
'    * specified part,
'    * SOLIDWORKS MBD 3D PDF theme, and
'    * c:\temp exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part.
' 2. Gets the MBD3DPdfData object.
' 3. Sets the path and file name for the SOLIDWORKS MBD PDF.
' 4. Sets the theme for the SOLIDWORKS MBD 3D PDF.
' 5. Sets the standard views for the SOLIDWORKS MBD 3D PDF.
' 6. Publishes the part to SOLIDWORKS MBD PDF.
' 7. Exports the SOLIDWORKS MBD part document to STEP 242.
' 8. Examine the Immediate window and c:\temp.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMBDPdfData As SldWorks.MBD3DPdfData
Dim fileName As String
Dim standardViews As Variant
Dim viewIDs(2) As Long
Dim status As Long
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Get MBD3DPdfData object
    Set swMBDPdfData = swModelDocExt.GetMBD3DPdfData

    'Set path and file name for SOLIDWORKS MBD 3D PDF
    swMBDPdfData.FilePath = "c:\temp\MyBlockMBD.PDF"
```

```
    'Set SOLIDWORKS MBD 3D PDF theme
    swMBDPdfData.ThemeName = "c:\Program Files\SolidWorks Corp\SOLIDWORKS\data\themes\simple part (a4, portrait)\theme.xml"
```

```
    'Set standard views for SOLIDWORKS MBD 3D PDF
    viewIDs(0) = swStandardViews_e.swFrontView
    viewIDs(1) = swStandardViews_e.swTopView
    viewIDs(2) = swStandardViews_e.swDimetricView
    standardViews = viewIDs
    swMBDPdfData.SetStandardViews (standardViews)
```

```
    'Publish part document to SOLIDWORKS MBD 3D PDF
    status = swModelDocExt.PublishTo3DPDF(swMBDPdfData)
    Debug.Print ("Status of publishing part to SOLIDWORKS MBD 3D PDF (0 = success): " & status)
```

```
    'Export SOLIDWORKS MBD part to STEP 242
    status = swModelDocExt.PublishSTEP242File("c:\temp\MyStepBlock.STP")
    Debug.Print ("Status of exporting SOLIDWORKS MBD part to STEP 242 (0 = success): " & status)

End Sub
```
