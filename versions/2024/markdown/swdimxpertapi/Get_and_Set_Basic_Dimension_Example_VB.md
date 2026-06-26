---
title: "Insert Basic Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_and_Set_Basic_Dimension_Example_VB.htm"
---

# Insert Basic Dimension Example (VBA)

This example shows how to insert a DimXpert distance-between dimension.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Ensure that the part to open exists.
 ' 2. Reference SOLIDWORKS version DimXpert type library:
 '    a. Click Tools > References > Browse.
 '    b. Select install_dir\swdimxpert.tlb.
 '    c. Click Open.
 '
 ' Postconditions: Inspect the graphics view and the DimXpertManager pane.
 '
 ' NOTE: Because the part is used elsewhere, do not save any changes.
 '----------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim swConfig As SldWorks.Configuration
 Dim swDimXPertMgr As SldWorks.DimXpertManager
 Dim swDimXPertPart As SwDimXpert.DimXpertPart
 Dim swDimXPertDimOpt As SwDimXpert.DimXpertDimensionOption
 Dim dblDimXPertTextPos(2) As Double
 Dim varDimXPertTextPos As Variant
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks

    Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2017\Simulation Examples\actuator_casing.sldprt", 1, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "actuator_casing.sldprt", False, longstatus
     Set Part = swApp.ActiveDoc

    Part.ShowNamedView2 "*Isometric", 7

    Set swConfig = Part.ConfigurationManager.ActiveConfiguration
     Set swDimXPertMgr = Part.Extension.DimXpertManager(swConfig.Name, True)
     Set swDimXPertPart = swDimXPertMgr.DimXpertPart
     Set swDimXPertDimOpt = swDimXPertPart.GetDimOption
     boolstatus = Part.Extension.SelectByID2("", "FACE", 8.32566935649766E-02, 1.41096473029049E-02, 1.43449005094567E-02, False, 0, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", 7.51728497303361E-02, 8.95850622406916E-04, 1.90499999998792E-02, True, 0, Nothing, 0)
     dblDimXPertTextPos(0) = 0.083208
     dblDimXPertTextPos(1) = 0.045464
     dblDimXPertTextPos(2) = 0.019052
     varDimXPertTextPos = dblDimXPertTextPos
     swDimXPertDimOpt.TextPosition = varDimXPertTextPos
     boolstatus = swDimXPertPart.InsertBasicDimension(swDimXPertDimOpt)
End Sub
```
