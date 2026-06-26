---
title: "Create a Drawing for a Pipe Route Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Create_a_Drawing_for_a_Pipe_Route_Example_VB.htm"
---

# Create a Drawing for a Pipe Route Example (VBA)

This example shows how to create a drawing of a pipe assembly.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add SOLIDWORKS Routing as an add-in
 '   (in SOLIDWORKS, select Tools > Add-Ins > SOLIDWORKS routing).
 ' 2. Add the SOLIDWORKS <version> Routing Type Library as a reference
 '   (in the IDE select Tools > References).
 ' 3. Create a piping BOM template named  piping_template.sldbomtbt.
 ' 4. Add a column with header "Length" to the piping BOM template.
 ' 5. Ensure that the specified paths to piping BOM and sheet
 '    format templates exist.
 ' 6. In Tools > Options > Routing > Routing File Locations,
 '    add the locations of your SOLIDWORKS Routing files.
 ' 7. In Tools > Options > File Locations > Sheet formats,
 '    add the location of your sheet format templates.
 ' 8. Open:
 '    public_documents\samples\tutorial\routing-pipes\fittings\reducerroute.sldasm.
 '
 ' Postconditions: A drawing of the pipe assembly is created
 ' in a standard format and includes auto balloons, a bill of
 ' materials, and a route sketch.
 '
 ' NOTE: Because this assembly is used elsewhere,
 ' do not save any changes to it.
 '-------------------------------------------------------------------------
Option Explicit

 Sub main()
```

```vb
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.AssemblyDoc
Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc
Dim RouteMgr As SWRoutingLib.RouteManager
Set RouteMgr = Part.GetRouteManager()
Dim bomtemplatepath As String
bomtemplatepath = "Piping_BOM_template_path"
Dim bomtemplatename As String
bomtemplatename = "piping_template.sldbomtbt"
Dim sheettemplatepath As String
sheettemplatepath = "install_dir\lang\english\sheetformat"
Dim sheettemplatename As String
sheettemplatename = "a - landscape.slddrt"
Dim insertballoons As Boolean
insertballoons = True
Dim insertBOM As Boolean
insertBOM = True
Dim showRouteSketch As Boolean
showRouteSketch = True
Dim subAssembly As Boolean
subAssembly = True
Dim userSheetWidth As Double
userSheetWidth = 500#
Dim userSheetHeight As Double
userSheetHeight = 500#
Dim displayFormat As Boolean
displayFormat = True
Dim dwgTemplates As Long
dwgTemplates = 0
RouteMgr.CreatePipeDrawingforPipeRoute(bomtemplatepath, bomtemplatename, insertballoons, insertBOM, showRouteSketch, subAssembly, userSheetWidth, userSheetHeight, sheettemplatepath, sheettemplatename, displayFormat, dwgTemplates)
```

```vb
End Sub
```
