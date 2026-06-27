---
title: "Export Tube Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Export_Tube_Data_Example_VB.htm"
---

# Export Tube Data Example (VBA)

This example shows how to export routing tube data.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add SOLIDWORKS Routing as an add-in
 '   (in SOLIDWORKS select Tools > Add-Ins > SOLIDWORKS Routing).
 ' 2. Add the SOLIDWORKS <version> Routing Type Library as a reference
 '   (in the IDE select Tools > References).
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
 '    add locations of your SOLIDWORKS Routing files.
 ' 4. Open public_documents\samples\tutorial\api\tubing.sldasm.
 ' 5. In the FeatureManager design tree select Tube1^Tubing assembly.
 ' 6. Open an Immediate Window.
 ' 7. Ensure that c:\temp exists.
 '
 ' Postconditions: Tangent bend data is exported to c:\temp\default.html.
 '--------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Option Explicit

 Sub main()
```

```vb
Dim swModel As SldWorks.ModelDoc2
Dim swTopLevelAssembly As SldWorks.AssemblyDoc
Dim rtRouteManager As SWRoutingLib.RouteManager
Dim resultCode As Long
Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swTopLevelAssembly = swModel
' Get the RouteManager from the top-level assembly
Set rtRouteManager = swTopLevelAssembly.GetRouteManager
If rtRouteManager Is Nothing Then
Debug.Print "No RouteManager found in top-level document."
Exit Sub
End If
resultCode = rtRouteManager.ExportTubeData("c:\temp.html", 1, 0)
```

```vb
 End Sub
```
