---
title: "Insert Connection Point Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Connection_Point_Example_VB.htm"
---

# Insert Connection Point Example (VBA)

This example shows how to create a connection point for a tube for routing.

```
'---------------------------------------------------
' Preconditions:
' 1. Load the SOLIDWORKS Routing Add-in (click
'    Tools > Add-Ins > SOLIDWORKS Routing).
' 2. Verify that the specified part document to open
'    exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates a connection point for a tube
'    using the selected edge.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because this part document is used elsewhere,
' do not save changes.
'---------------------------------------------------
```

```vb
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatMgr As SldWorks.FeatureManager
Dim errors As Long
Dim warnings As Long
Dim status As Boolean

Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\routing-pipes\fittings\filter.sldprt", swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension

' Select the edge for the connection point;
' remember to specify a value of 1 for
' the Mark parameter for a circular edge for
' a tube's connection point
status = swModelDocExt.SelectByID2("", "EDGE", 0.001425156111225, 0.1755840982619, -0.09117938337181, False, 1, Nothing, 0)

' Insert a connection point for a tube
Set swFeatMgr = swModel.FeatureManager
Debug.Print "Connection point for tube created? " & swFeatMgr.InsertConnectionPoint(swConnectionPoint_Tube, 0, True, 25.4 / 1000, 0.1, 0.2, 0.3, 0.4, "", 0, 0, False, "Specification", "")
```

```vb
End Sub
```
