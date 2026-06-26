---
title: "Insert Table-driven Pattern Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Table-driven_Pattern_Example_VB.htm"
---

# Insert Table-driven Pattern Example (VBA)

This example shows how to insert a table-driven pattern.

```
'--------------------------------------------------------------------
' Preconditions:
' 1. Verify that c:\temp exists.
' 2. Open public_documents\samples\tutorial\api\tablepattern.sldprt.
' 3. Edit TPattern1.
' 4. Click Save As, browse to c:\temp, type TestTable.sldptab in File name,
'    click Save, and click OK.
' 5. Edit c:\temp\TestTable.sldptab and change:
'    a. 0.01m to 0.04m.
'    b. -0.03m to -0.025m.
' 6. Save c:\temp\TestTable.sldptab.
' 7. Delete TPattern1.
'
' Postconditions:
' 1. Creates TPattern1.
' 2. Examine the FeatureManager design tree and the graphics
'    area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swPatternFeature As SldWorks.Feature
Dim swPatternPoints As Variant
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swFeatureMgr = swModel.FeatureManager
    status = swModelDocExt.SelectByID2("Coordinate System1", "COORDSYS", 0, 0, 0, True, 16, Nothing, 0)
    status = swModelDocExt.SelectByID2("Cut-Extrude1", "BODYFEATURE", 0, 0, 0, True, 4, Nothing, 0)
    Set swPatternPoints = Nothing
    Set swPatternFeature = swFeatureMgr.InsertTableDrivenPattern2("c:\temp\TestTable.sldptab", (swPatternPoints), True, False, True)
```

```
End Sub
```
