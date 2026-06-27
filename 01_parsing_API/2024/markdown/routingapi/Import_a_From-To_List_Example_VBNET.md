---
title: "Import a From-to List Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Import_a_From-To_List_Example_VBNET.htm"
---

# Import a From-to List Example (VB.NET)

This example shows how to import a from-to connection list.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add SOLIDWORKS Routing as an add-in
  '      (in SOLIDWORKS, select Tools > Add-Ins > SOLIDWORKS Routing).
 ' 2. Add Solidworks.Interop.SwRoutingLib.dll as a reference
  '      (in the IDE right-click the project,
  '      select Add Reference, and browse  install_dir\api\redist).
 ' 3. In Tools > Options > System Options > Routing > Routing File Locations,
  '      add locations of your SOLIDWORKS Routing files.
 ' 4. Open:
 '    public_documents\samples\tutorial\routing\electrical\top_assy.sldasm.
 ' 5. Ensure that the specified files exist.
 ' 6. Open an Immediate Window.
 '
 ' Postconditions:
 ' 1. Position the components in the harness by clicking the housing wall
 '    five (5) times. If at any time the mate toolbar displays,
 '    click the green checkmark to continue.
 ' 2. Click Yes in the message box.
 ' 3. Click the green checkmark in the Route Properties PropertyManager page
 '    to accept the defaults.
 '    Guidelines display in the electronic housing.
 '    The Auto Route PropertyManager page displays.
 ' 4. Click the green checkmark to accept the defaults.
 ' 5. Stop editing the route.
 ' 6. Stop editing the assembly.
 ' 7. Harness_1-top_assy appears in the FeatureManager design tree.
 '
 ' NOTE: Because the assembly is used elsewhere,
  '  do not save any changes when you close it.
 '---------------------------------------------------------------------------

  Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.SWRoutingLib
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swTopLevelAssembly As AssemblyDoc
         Dim rtRouteManager As RouteManager
         Dim fromtoListFileName As String
         fromtoListFileName =  "public_documents\tutorial\routing\electrical\from-to list.xlsx"
         Dim compoLibFilename As String
         compoLibFilename =  "install_dir\data\design library\routing\electrical\components.xml"
         Dim cableWireLibFilename As String
         cableWireLibFilename =  "C:\ProgramData\SOLIDWORKS\SOLIDWORKS 20nn\design library\routing\electrical\cable.xml"
         Dim useExistingAssembly As Boolean
         useExistingAssembly =  False
         Dim overwriteData As Boolean
         overwriteData =  True
         Dim searchAllSubAssemblies As Boolean
         searchAllSubAssemblies =  True
         Dim boolstatus As Boolean

         swModel = swApp.ActiveDoc
         swTopLevelAssembly = swModel

         ' Get the RouteManager from the top-level assembly
         rtRouteManager = swTopLevelAssembly.GetRouteManager
         If rtRouteManager Is Nothing Then
             Debug.Print("No RouteManager found in top-level document.")
             Exit Sub
         End If

         boolstatus = rtRouteManager.ImportFromToList(fromtoListFileName, compoLibFilename, cableWireLibFilename, useExistingAssembly, overwriteData, searchAllSubAssemblies)

     End Sub

     Public swApp As SldWorks

 End  Class
```
